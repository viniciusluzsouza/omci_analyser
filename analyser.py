from enum import Enum
import struct
import binascii
from pcapfile import savefile
import os

from utils.me_base import *


class MessageType(Enum):
    CREATE = 4
    CREATE_COMPLETE_CONNECTION = 5
    DELETE = 6
    DELETE_COMPLETE_CONNECTION = 7
    SET = 8
    GET = 9
    GET_COMPLETE_CONNECTION = 10
    GET_ALL_ALARMS = 11
    GET_ALL_ALARMS_NEXT = 12
    MIB_UPLOAD = 13
    MIB_UPLOAD_NEXT = 14
    MIB_RESET = 15
    ALARM = 16
    ATTRIBUTE_VALUE_CHANGE = 17
    TEST = 18
    START_SOFTWARE_DOWNLOAD = 19
    DOWNLOAD_SECTION = 20
    END_SOFTWARE_DOWNLOAD = 21
    ACTIVATE_SOFTWARE = 22
    COMMIT_SOFTWARE = 23
    SYNCRONIZE_TIME = 24
    REBOOT = 25
    GET_NEXT = 26
    TEST_RESULT = 27
    GET_CURRENT_DATA = 28

    type_str = {
        4: "Create",
        5: "Create Complete Connection",
        6: "Delete",
        7: "Delete Complete Connection",
        8: "Set",
        9: "Get",
        10: "Get Complete Connection",
        11: "Get All Alarms",
        12: "Get All Alarms Next",
        13: "MIB Upload",
        14: "MIB Upload Next",
        15: "MIB Reset",
        16: "Alarm",
        17: "Attribute Value Change",
        18: "Test",
        19: "Start Software Download",
        20: "Download Section",
        21: "End Software Download",
        22: "Activate Software",
        23: "Commit Software",
        24: "Synchronize Time",
        25: "Reboot",
        26: "Get Next",
        27: "Test Result",
        28: "Get Current Data"
    }

    def __str__(self):
        return '%s' % MessageType.type_str.value[self.value]


class OmciPacket:
    def __init__(self, pkt):
        self.pkt = pkt
        self.trans_corr = None
        self.dest_bit = None
        self.ar = None
        self.ak = None
        self.message_type = None
        self.dev_id = None
        self.me_id = None
        self.me_inst = None
        self.me = None

    def translate(self):
        header = struct.unpack("!2s1s1s2s2s", self.pkt[0][0:8])
        self.trans_corr = int(binascii.hexlify(header[0]), 16)
        self.dest_bit = 0x00  # TODO FIXME
        mt_buf = int(binascii.hexlify(header[1]), 16)
        self.message_type = MessageType(mt_buf & 0b00011111)
        self.ak = (mt_buf & 0b00100000) >> 5
        self.ar = (mt_buf & 0b01000000) >> 6
        self.dev_id = binascii.hexlify(header[2]).decode()
        self.me_id = int(binascii.hexlify(header[3]), 16)
        self.me_inst = int(binascii.hexlify(header[4]), 16)

    def printout(self):
        output = "ME: {}, Inst: {}, MT: {}".format(self.me_id, self.me_inst, self.message_type)
        print(output)

    def getType(self):
        return self.message_type

    def getPkt(self):
        return self.pkt

    def getMeId(self):
        return self.me_id

    def getMeInst(self):
        return self.me_inst

class Analyser:
    def __init__(self, buffer=[]):
        self.buffer = buffer
        self.packets = []
        self.entities = []
        self.output = ""

    def translateAll(self):
        for raw_pkt in self.buffer:
            pkt = OmciPacket(raw_pkt)
            pkt.translate()
            self.packets.append(pkt)

    def printPackets(self):
        for p in self.packets:
            p.printout()


    def findMeInstance(self, me_id, instance):
        for ent in self.entities:
            # print("{} vs {} | {} vs {}".format(me_id, ent.getId(), instance, ent.getInstance()))
            if me_id == ent.getId() and instance == ent.getInstance():
                return ent

        return None

    def analyse(self):
        # self.me = MeTranslate.getInstance(self.me_id, self.me_inst)
        for pkt in self.packets:
            pkt_type = pkt.getType()
            if pkt_type == MessageType.CREATE:
                # TODO: if already there is the me in list?
                me = MeTranslate.getInstance(pkt.getMeId(), pkt.getMeInst())
                me.create(pkt.getPkt()[0])
                self.entities.append(me)
            elif pkt_type == MessageType.SET:
                exist = False
                for e in self.entities:
                    if pkt.getMeId() == e.getId and pkt.getMeInst == e.getInstance():
                        e.setAttributes(pkt.getPkt()[0])
                        exist = True

                if not exist:
                    me = MeTranslate.getInstance(pkt.getMeId(), pkt.getMeInst())
                    me.setAttributes(pkt.getPkt()[0])
                    self.entities.append(me)

        for e in self.entities:
            e.setPointers()

        mes_with_pointers = []

        def appendMeWithPointer(ent, points_to=None):
            if points_to is None:
                return

            ent['pointers'].append(points_to)
            if ent not in mes_with_pointers:
                mes_with_pointers.append(ent)

        for e in self.entities:
            ent_obj = {'me': e.getId(), 'name': e.getName(), 'inst': e.getInstance(), 'pointers': []}
            appendMeWithPointer(ent_obj)
            for attr in e.getAttributes():
                attr_pointer = attr.getPointer()
                if attr_pointer is not None:
                    for me_candidate in attr_pointer:
                        val = attr.getValue()
                        entity = self.findMeInstance(me_candidate, int.from_bytes(val, 'big')) if val is not None else None
                        if entity is not None:
                            e_append = {'me': entity.getId(), 'name': entity.getName(), 'inst': entity.getInstance()}
                            appendMeWithPointer(ent_obj, e_append)

        self.output = "blockdiag {\n"
        control = []
        for x in mes_with_pointers:
            name = "{}{}".format(x['name'], x['inst'])
            if name not in control:
                control.append(x['name'])
                self.output += '\t"{} ({})" [width = 192, height = 64];\n'.format(x['name'], x['inst'])

            for p in x['pointers']:
                name = "{}{}".format(p['name'], p['inst'])
                if name not in control:
                    control.append(p['name'])
                    self.output += '\t"{} ({})" [width = 192, height = 64];\n'.format(p['name'], p['inst'])

        self.output += "\n\n"
        for x in mes_with_pointers:
            for p in x['pointers']:
                self.output += '\t"{} ({})" -> "{} ({})"\n'.format(x['name'], x['inst'], p['name'], p['inst'])

        self.output += "}\n"

    def getOutput(self):
        return self.output

    def generateImage(self, name):
        file = "output/" + name
        with open(file, "w") as f:
            f.write(self.output)

        # TODO Change to subprocess
        os.system("blockdiag %s --no-transparency" % file)
        os.system("rm -rf %s" % file)

    def setBuffer(self, buf):
        self.buffer = buf

    def getBuffer(self):
        return self.buffer

    def loadBuffer(self, file):
        if not os.path.isfile(file):
            print("%s is not a file." % file)
            return False

        try:
            raw_file = open(file, 'rb')
            pcapfile = savefile.load_savefile(raw_file, verbose=False)
            self.buffer = []
            for pkt in pcapfile.packets:
                self.buffer.append((pkt.raw()[14:],))

        except Exception as e:
            print(str(e))
            return False

        return True