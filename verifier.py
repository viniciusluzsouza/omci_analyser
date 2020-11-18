
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

    def verify(self):
        if not len(self.buf_entity):
            if len(self.buf):
                self.buf_entity = Analyser.translateAndCreateEntities(self.buf)
            else:
                print("Nothing to verify!")
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
            print("\n\nMissing Attributes:\n")

            for me in missing_attributes.values():
                attr_str = "\n\t" + ";\n\t".join(me["attributes"])
                print("{} ({}) [{}]: {}\n".format(me["me_name"], me["me_id"], me["me_inst"], attr_str))
