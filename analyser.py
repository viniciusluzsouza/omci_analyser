from enum import Enum
import struct
import binascii
from pcapfile import savefile
import os
import re

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

    def getAckReq(self):
        return self.ar

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
            # Only analyse downstream packets
            if pkt.getAckReq() != 0x1:
                continue

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
        added_mes = []

        def breakStr(string, every=13):
            return '\\n'.join(string[i:i + every] for i in range(0, len(string), every))

        def appendMeWithPointer(ent, points_to=None):
            if points_to is None:
                return

            ent['pointers'].append(points_to)
            if ent not in mes_with_pointers:
                mes_with_pointers.append(ent)

        implicitly_linked_mes = {}
        implicitly_not_found = []
        for e in self.entities:
            ent_obj = {'me': e.getId(), 'name': e.getName(), 'inst': e.getInstance(), 'pointers': []}
            # print(ent_obj)
            appendMeWithPointer(ent_obj)
            for attr in e.getAttributes():
                attr_pointer = attr.getPointer()
                if attr_pointer is not None:
                    for me_candidate in attr_pointer:
                        val = attr.getValue()
                        if val is None:
                            continue

                        val_int = int.from_bytes(val, 'big')
                        entity = self.findMeInstance(me_candidate, val_int)
                        if entity is not None:
                            e_append = {'me': entity.getId(), 'name': entity.getName(), 'inst': entity.getInstance()}
                            appendMeWithPointer(ent_obj, e_append)
                        else:
                            if me_candidate in ManagedEntity.me_dict and val_int != 0:
                                e_append = {'me': me_candidate, 'name': ManagedEntity.me_dict[me_candidate], 'inst': val_int}
                                appendMeWithPointer(ent_obj, e_append)
                                if e_append not in added_mes:
                                    added_mes.append(e_append)

            imp_link = e.getImplicitlyLinked()
            found_il = False
            for il in imp_link:
                ent = self.findMeInstance(il, e.getInstance())
                if ent is not None:
                    found_il = True
                    imp_key = e.getId() + ent.getId() + e.getInstance()
                    if imp_key not in implicitly_linked_mes:
                        implicitly_linked_mes[imp_key] = {
                            'me1': e.getId(),
                            'name1': e.getName(),
                            'me2': ent.getId(),
                            'name2': ent.getName(),
                            'inst': e.getInstance()
                        }

            if not found_il:
                implicitly_not_found.append(e)

        self.output = 'digraph OmciGraph {\n\tnode [shape="box", style="filled", fillcolor="#dae8fc"]\n'

        for a in added_mes:
            me_num = a['me']
            name = "{}".format(a['name'])
            inst = "({})".format(a['inst'])
            idx = "[{}-{}]".format(me_num, a['inst'])
            name = breakStr(name) + "\\n" + inst + "\\n" + idx
            self.output += '\t"{}" [shape="box", style="filled", fillcolor="#fff2cc"]\n'.format(name)
            for inf in implicitly_not_found:
                if me_num in inf.getImplicitlyLinked():
                    imp_key = inf.getId() + me_num + inf.getInstance()
                    if imp_key not in implicitly_linked_mes:
                        implicitly_linked_mes[imp_key] = {
                            'me1': inf.getId(),
                            'name1': inf.getName(),
                            'me2': me_num,
                            'name2': a['name'],
                            'inst': inf.getInstance()
                        }

        self.output += "\n\n"
        for x in mes_with_pointers:
            for p in x['pointers']:
                name1 = "{}".format(x['name'])
                inst1 = "({})".format(x['inst'])
                idx1 = "[{}-{}]".format(x['me'], x['inst'])
                name1 = breakStr(name1) + "\\n" + inst1 + "\\n" + idx1

                name2 = "{}".format(p['name'])
                inst2 = "({})".format(p['inst'])
                idx2 = "[{}-{}]".format(p['me'], p['inst'])
                name2 = breakStr(name2) + "\\n" + inst2 + "\\n" + idx2

                new_line = '\t"{}" -> "{}"\n'.format(name1, name2)
                if new_line not in self.output:
                    self.output += new_line

        self.output += "\n"

        for il in implicitly_linked_mes.values():
            name1 = "{}".format(il['name1'])
            inst1 = "({})".format(il['inst'])
            idx1 = "[{}-{}]".format(il['me1'], il['inst'])
            name1 = breakStr(name1) + "\\n" + inst1 + "\\n" + idx1

            name2 = "{}".format(il['name2'], il['inst'])
            inst2 = "({})".format(il['inst'])
            idx2 = "[{}-{}]".format(il['me2'], il['inst'])
            name2 = breakStr(name2) + "\\n" + inst2 + "\\n" + idx2

            new_line = '\t"{}" -> "{}" [arrowhead=none, arrowtail=none, style=dotted]\n'.format(name1, name2)
            if new_line not in self.output:
                self.output += new_line

        unlinked_mes = []
        for e in self.entities:
            name = "{}".format(e.getName())
            inst = "({})".format(e.getInstance())
            idx = "[{}-{}]".format(e.getId(), e.getInstance())
            name = breakStr(name) + "\\n" + inst + "\\n" + idx
            if name not in self.output and name not in unlinked_mes:
                unlinked_mes.append(name)

        if len(unlinked_mes):
            self.output += "\n\n\tsubgraph clusterunlinked {\n"
            self.output += "\t\tnode[style=filled, fillcolor=gray]\n"
            self.output += '\t\tlabel="Unlinked MEs"\n'
            self.output += "\t\tcolor=black\n"
            self.output += "\t\t"
            for u in unlinked_mes:
                self.output += '"{}" '.format(u)

            self.output += "\n\t}\n"

        self.output += "}\n"

    def getOutput(self):
        return self.output

    def generateImage(self, name):
        file = "output/" + name
        with open(file, "w") as f:
            f.write(self.output)

        # TODO Change to subprocess
        #os.system("blockdiag %s --no-transparency" % file)
        os.system("dot -Tpng %s -o %s.png" % (file, file))
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

    def showEntity(self, entity):
        me = 0
        inst = 0

        try:
            p = re.compile(r'(\d+)-(\d+)')
            for m in p.finditer(str(entity)):
                me = int(m.group(1))
                inst = int(m.group(2))
        except Exception:
            pass

        if me == 0 and inst == 0:
            print("Invalid syntax")
            return

        e = self.findMeInstance(me, inst)
        if e is None:
            print("Entity doesnt exist")
        else:
            e.printBeauty()