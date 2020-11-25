from socket import socket, AF_PACKET, SOCK_RAW
from time import sleep

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("lo", 0))

try:
    # src_addr = "\xbb\xbb\xbb\xbb\xbb\xbb"
    # dst_addr = "\xaa\xaa\xaa\xaa\xaa\xaa"
    # ethertype = "\x88\xb5"
    # #payload = ("["*30)+"PAYLOAD"+("]"*30)
    # payload = "\x84\x9a\x49\x0a\x00\x0b\x01\x01\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x28\x00\x00\x00\x00"
    # checksum = "\x1a\x2b\x3c\x4d"
    #
    # s.send(dst_addr+src_addr+ethertype+payload+checksum)

    f = open("./cap.txt", "r")
    k = f.read()
    packets = []
    p = ""
    for i, line in enumerate(k.split('\n')):
        k = line.split(' ')
        for l in k:
            m = l.strip()
            if m == '':
                continue

            p += chr(int(m, 16))

        if len(k) == 20:
            packets.append(p)
            p = ""

    end = 0
    while end < 1:
        for pkt in packets:
            print(":".join("{:02x}".format(ord(c)) for c in pkt))
            s.send(pkt.encode('latin1'))
            sleep(0.001)

        end += 1

    print("Sent packets: %d" % (end*len(packets)))

except Exception as e:
    print(str(e))
    print("exiting ... ")
finally:
    s.close()
