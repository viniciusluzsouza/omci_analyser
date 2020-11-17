import socket
import struct
import binascii
import os
from pcapfile import savefile

class Capturator:
    MSGTYPE = {
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

    def __init__(self):
        self.buff = []
        self.buff_omci = []
        self.sock = None

    def __del__(self):
        if self.sock:
            self.sock.close()

    def setInterface(self, interface):
        ifaces = os.listdir('/sys/class/net/')
        if interface not in ifaces:
            raise NameError("Invalid interface")

        self.interface = interface

    def createSock(self):
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x88b5))
        self.sock.bind((self.interface, 0))

    def start(self):
        while True:
            packet = self.sock.recvfrom(2048)
            # eth_header = struct.unpack("!6s6s2s", packet[0][0:14])
            omci = struct.unpack("!2s1s1s2s2s", packet[0][14:22])
            trans_corr = int(binascii.hexlify(omci[0]), 16)
            mt_buf = int(binascii.hexlify(omci[1]), 16)
            mt = Capturator.MSGTYPE[mt_buf & 0b00011111].ljust(26)
            ak = (mt_buf & 0b00100000) >> 5
            ar = (mt_buf & 0b01000000) >> 6
            # dev_id = binascii.hexlify(omci[2]).decode()
            me = str(int(binascii.hexlify(omci[3]), 16)).ljust(5)
            me_inst = str(int(binascii.hexlify(omci[4]), 16)).ljust(5)
            print("%d | Type: %s | AR: %d | AK: %d | ME: %s | Inst: %s" % (trans_corr, mt, ar, ak, me, me_inst))

            p = struct.unpack("!16s16s16s14s", packet[0][0:62])
            self.buff.append([p[0], p[1], p[2], p[3]])

            o = struct.unpack("!48s", packet[0][14:62])
            self.buff_omci.append(o)

    def saveDump(self, file):
        file_str = file + ".pcap" if "pcap" not in file else file

        with open("output/temp.txt", "w") as f:
            for pkt in self.buff:
                line = "\n"
                for i, p in enumerate(pkt):
                    p_str = " ".join("{:02x}".format(ord(chr(c))) for c in p)
                    line += str(i * 10).rjust(4, '0') + ' ' + p_str + '\n'

                f.write(line)

        # TODO: Change to subprocess
        os.system("text2pcap output/temp.txt output/%s -q" % file_str)
        os.system("rm -rf output/temp.txt")

    @staticmethod
    def loadDump(file):
        pkt_buf = []
        if os.path.isfile(file):
            try:
                raw_file = open(file, 'rb')
                pcapfile = savefile.load_savefile(raw_file, verbose=False)
                for pkt in pcapfile.packets:
                    pkt_buf.append((pkt.raw()[14:],))

            except Exception as e:
                print(str(e))
        else:
            print("%s is not a file." % file)

        return pkt_buf

    def clearDump(self):
        self.buff = []
        self.buff_omci = []

    def closeSock(self):
        if self.sock:
            self.sock.close()

    def getBuffer(self):
        return self.buff_omci if self.buff_omci else []

    def hasCapture(self):
        return True if len(self.buff_omci) else False

    def close(self):
        self.clearDump()
        self.closeSock()