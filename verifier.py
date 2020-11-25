
from analyser import Analyser
from utils.me_base import *

class Verifier:
    def __init__(self):
        self.buf = []
        self.buf_entity = []

    def setPacketBuffer(self, buf):
        self.buf = buf

    def setEntityBuf(self, buf):
        self.buf_entity = buf

    def checkBuffer(self):
        if len(self.buf):
            self.buf_entity = Analyser.translateAndCreateEntities(self.buf)
        else:
            print("Nothing to verify!")
            return False

        return True

    def verifyMandatoryAttributes(self, do_print=True):
        if not self.checkBuffer():
            return

        missing_attributes = {}
        for entity in self.buf_entity:
            for attribute in entity.getAttributes():
                if attribute.isMandatory() and attribute.getValue() is None and attribute.getPermissions() != MeAttribute.READ_PERMISSION:
                    me_id = entity.getId()
                    me_inst = entity.getInstance()
                    key = me_id + me_inst
                    if key not in missing_attributes.keys():
                        missing_attributes[key] = {
                            "me_id": me_id,
                            "me_inst": me_inst,
                            "me_name": entity.getName(),
                            "attributes": [attribute.getName()]
                        }
                    else:
                        attr_name = attribute.getName()
                        if attr_name not in missing_attributes[key]["attributes"]:
                            missing_attributes[key]["attributes"].append(attr_name)

        if len(missing_attributes):
            printout = "\n\nMissing Attributes:\n"

            for me in missing_attributes.values():
                attr_str = "\n\t" + ";\n\t".join(me["attributes"])
                printout += "\n{} ({}) [{}]: {}\n".format(me["me_name"], me["me_id"], me["me_inst"], attr_str)

        else:
            printout = "\n\nNot found missing attributes.\n"

        if do_print:
            print(printout)
        else:
            return printout

    def checkAttrLength(self, val):
        count = len(val)
        for v in reversed(val):
            if v != 0x00:
                break

            count = count - 1

        return count

    def verifyEntitiesLength(self, do_print=True):
        if not self.checkBuffer():
            return

        invalid_received_len = []
        for entity in self.buf_entity:
            expected_len = 0
            received_len = 0
            for attribute in entity.getAttributes():
                val = attribute.getValue()
                if val is not None:
                    exp_len = attribute.getLength()
                    expected_len += exp_len
                    rec_len = self.checkAttrLength(val)
                    received_len += rec_len
                    # received_len += rec_len + 1 if rec_len != 0 and rec_len != exp_len else exp_len

            if expected_len != received_len:
                invalid_received_len.append({
                    "me_id": entity.getId(),
                    "me_inst": entity.getInstance(),
                    "me_name": entity.getName(),
                    "expected": expected_len,
                    "received": received_len
                })

        if len(invalid_received_len):
            printout = "\n\nConflicting Lengths:\n"

            for irl in invalid_received_len:
                expected_str = "\n\tExpected: {}\n\tReceived: {}".format(irl["expected"], irl["received"])
                printout += "\n{} ({}) [{}]: {}\n".format(irl["me_name"], irl["me_id"], irl["me_inst"], expected_str)

        else:
            printout = "\n\nNot found conflicting length in MEs sent by OLT.\n"

        if do_print:
            print(printout)
        else:
            return printout

    def verifySetWithoutPermission(self, do_print=True):
        if not self.checkBuffer():
            return

        mes_set_without_permission = {}
        for entity in self.buf_entity:
            for attribute in entity.getAttributes():
                if attribute.getValue() is not None and attribute.getPermissions() == MeAttribute.READ_PERMISSION:
                    me_id = entity.getId()
                    me_inst = entity.getInstance()
                    key = me_id + me_inst
                    if key not in mes_set_without_permission.keys():
                        mes_set_without_permission[key] = {
                            "me_id": me_id,
                            "me_inst": me_inst,
                            "me_name": entity.getName(),
                            "attributes": [attribute.getName()]
                        }
                    else:
                        attr_name = attribute.getName()
                        if attr_name not in mes_set_without_permission[key]["attributes"]:
                            mes_set_without_permission[key]["attributes"].append(attr_name)

        if len(mes_set_without_permission):
            printout = "\n\nAttributes configured without permission:\n"

            for me in mes_set_without_permission.values():
                attr_str = "\n\t" + ";\n\t".join(me["attributes"])
                printout += "\n{} ({}) [{}]: {}\n".format(me["me_name"], me["me_id"], me["me_inst"], attr_str)

        else:
            printout = "\n\nNot found configured attributes without permission.\n"

        if do_print:
            print(printout)
        else:
            return printout

    def runAll(self):
        printout = """
#################################################
################ Verifier Output ################
#################################################
"""

        printout += "\n#################################################\n"
        printout += "1) Check mandatory attributes"
        printout += self.verifyMandatoryAttributes(do_print=False)
        printout += "\n\n#################################################\n"
        printout += "2) Check ME lengths"
        printout += self.verifyEntitiesLength(do_print=False)
        printout += "\n\n#################################################\n"
        printout += "3) Check configured attributes without permission"
        printout += self.verifySetWithoutPermission(do_print=False)

        printout += "\n"
        return printout

    def runAllAndGenerateReport(self, reportfile=None, location=None):
        printout = False
        try:
            if reportfile is None:
                printout = True
                while True:
                    reportfile = input("Report file name: ")
                    if reportfile != "":
                        if not reportfile.startswith('/'):
                            reportfile = location + '/' + reportfile

                        break

            output = self.runAll()

            reportfile = reportfile + ".txt" if "txt" not in reportfile else reportfile
            with open(reportfile, "w") as f:
                f.write(output)

            if printout:
                print("\nReport successfully generated.\n")

        except KeyboardInterrupt:
            return
        except Exception as e:
            print(str(e))
            return

