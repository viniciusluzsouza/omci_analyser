import re

SET_POINTERS_METHOD = "    def setPointers(self):"
# pointer_rule="1-11,2-14,3-130,4-134|347,5-266,6-281,7-98,8-117,9-286,11-329,12-162,13-419" },
mes_specific_methods = {
    47: SET_POINTERS_METHOD + """
        tp_type = self.tp_type.getValue()
        tp_type = int.from_bytes(tp_type, 'big') if tp_type is not None else None
        if tp_type == 1:
            self.tp_pointer.setPointer([11])
        elif tp_type == 2:
            self.tp_pointer.setPointer([14])
        elif tp_type == 3:
            self.tp_pointer.setPointer([130])
        elif tp_type == 4:
            self.tp_pointer.setPointer([134, 347])
        elif tp_type == 5:
            self.tp_pointer.setPointer([266])
        elif tp_type == 6:
            self.tp_pointer.setPointer([281])
        elif tp_type == 7:
            self.tp_pointer.setPointer([98])
        elif tp_type == 8:
            self.tp_pointer.setPointer([117])
        elif tp_type == 9:
            self.tp_pointer.setPointer([286])
        elif tp_type == 11:
            self.tp_pointer.setPointer([329])
        elif tp_type == 12:
            self.tp_pointer.setPointer([162])
        elif tp_type == 13:
            self.tp_pointer.setPointer([419])
        else:
            self.tp_pointer.setPointer(None)

        self.bridge_id_pointer.setPointer([45])
        self.outbound_td_pointer.setPointer([280])
        self.inbound_td_pointer.setPointer([280])\n""",

    58: SET_POINTERS_METHOD + """
        self.network_specific_extensions_pointer.setPointer([137])\n""",

    130: SET_POINTERS_METHOD + """
        tp_type = self.tp_type.getValue()
        tp_type = int.from_bytes(tp_type, 'big') if tp_type is not None else None
        if tp_type == 1:
            self.tp_pointer.setPointer([11])
        elif tp_type == 2:
            self.tp_pointer.setPointer([134, 347])
        elif tp_type == 3:
            self.tp_pointer.setPointer([286])
        elif tp_type == 4:
            self.tp_pointer.setPointer([427])
        elif tp_type == 6:
            self.tp_pointer.setPointer([162])
        elif tp_type == 7:
            self.tp_pointer.setPointer([329])
        elif tp_type == 8:
            self.tp_pointer.setPointer([265])
        elif tp_type == 9:
            self.tp_pointer.setPointer([419])
        else:
            self.tp_pointer.setPointer(None)

        self.interwork_tp_pointer_for_p_bit_priority_0.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_1.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_2.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_3.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_4.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_5.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_6.setPointer([266,281,404])
        self.interwork_tp_pointer_for_p_bit_priority_7.setPointer([266,281,404])\n""",

    136: SET_POINTERS_METHOD + """
        self.ip_host_pointer.setPointer([134,347])\n""",

    137: SET_POINTERS_METHOD + """
        self.security_pointer.setPointer([148])
        self.address_pointer.setPointer([157])\n""",

    138: SET_POINTERS_METHOD + """
        self.voip_configuration_address_pointer.setPointer([137])\n""",

    139: SET_POINTERS_METHOD + """
        self.user_protocol_pointer.setPointer([153, 155])
        self.pptp_pointer.setPointer([53])
        self.voip_media_profile_pointer.setPointer([142])\n""",

    142: SET_POINTERS_METHOD + """
        self.voice_service_profile_pointer.setPointer([58])
        self.rtp_profile_pointer.setPointer([143])\n""",

    143: SET_POINTERS_METHOD + """
        self.ip_host_config_pointer.setPointer([134, 347])\n""",

    150: SET_POINTERS_METHOD + """
        self.proxy_server_address_pointer.setPointer([157])
        self.outbound_proxy_address_pointer.setPointer([157])
        self.tcp_udp_pointer.setPointer([136])
        self.redundant_sip_agent_pointer.setPointer([150])\n""",

    153: SET_POINTERS_METHOD + """
        self.sip_agent_pointer.setPointer([150])
        self.network_dial_plan_pointer.setPointer([145])
        self.application_services_profile_pointer.setPointer([146])
        self.feature_code_pointer.setPointer([147])
        self.pptp_pointer.setPointer([53])\n""",

    171: SET_POINTERS_METHOD + """
        ass_type = self.association_type.getValue()
        ass_type = int.from_bytes(ass_type, 'big') if ass_type is not None else None
        if ass_type == 1:
            self.associated_me_pointer.setPointer([130])
        elif ass_type == 2:
            self.associated_me_pointer.setPointer([11])
        elif ass_type == 3:
            self.associated_me_pointer.setPointer([134, 347])
        elif ass_type == 4:
            self.associated_me_pointer.setPointer([427])
        elif ass_type == 5:
            self.associated_me_pointer.setPointer([266])
        elif ass_type == 6:
            self.associated_me_pointer.setPointer([281])
        elif ass_type == 7:
            self.associated_me_pointer.setPointer([162])
        elif ass_type == 9:
            self.associated_me_pointer.setPointer([286])
        elif ass_type == 10:
            self.associated_me_pointer.setPointer([329])
        elif ass_type == 11:
            self.associated_me_pointer.setPointer([333])
        elif ass_type == 12:
            self.associated_me_pointer.setPointer([419])
        else:
            self.associated_me_pointer.setPointer(None)\n""",

    250: SET_POINTERS_METHOD + """
        self.pointer_to_ip_host_config_data_me.setPointer([134, 347])
        self.pointer_to_larg_string_me_pointer_for_username.setPointer([157])
        self.pointer_to_larg_string_me_pointer_for_service_name.setPointer([157])\n""",

    266: SET_POINTERS_METHOD + """
        iw_option = self.interworking_option.getValue()
        iw_option = int.from_bytes(iw_option, 'big') if iw_option is not None else None
        if iw_option == 0:
            self.service_profile_pointer.setPointer([21])
            self.gal_profile_pointer.setPointer(None)
        elif iw_option == 1:
            self.service_profile_pointer.setPointer([45])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 3:
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 4:
            self.service_profile_pointer.setPointer([128])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 5:
            self.service_profile_pointer.setPointer([130])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 6:
            self.service_profile_pointer.setPointer(None)
            self.gal_profile_pointer.setPointer(None)
        elif iw_option == 7:
            self.service_profile_pointer.setPointer([21])
            self.gal_profile_pointer.setPointer(None)
        else:
            self.service_profile_pointer.setPointer(None)
            self.gal_profile_pointer.setPointer(None)
    
        self.gem_port_network_ctp_connectivity_pointer.setPointer([268])
        self.interworking_termination_point_pointer.setPointer([11, 268, 12])\n""",

    268: SET_POINTERS_METHOD + """
        self.t_cont_pointer.setPointer([262])
        self.traffic_management_pointer_for_upstream.setPointer([277, 262])
        self.traffic_descriptor_profile_pointer.setPointer([280])
        self.priority_queue_pointer_for_downstream.setPointer([277])\n""",

    277: SET_POINTERS_METHOD + """
        self.traffic_scheduler_g_pointer.setPointer([278])\n""",

    278: SET_POINTERS_METHOD + """
        self.tcont_pointer.setPointer([262])
        self.traffic_shed_pointer.setPointer([278])\n""",

    279: SET_POINTERS_METHOD + """
        self.working_ani_g_pointer.setPointer([263, 313, 315])
        self.protection_ani_g_pointer.setPointer([263, 313, 315])\n""",

    281: SET_POINTERS_METHOD + """
        iw_option = self.interworking_option.getValue()
        iw_option = int.from_bytes(iw_option, 'big') if iw_option is not None else None
        if iw_option == 0:
            self.service_profile_pointer.setPointer([21])
            self.gal_profile_pointer.setPointer(None)
        elif iw_option == 1:
            self.service_profile_pointer.setPointer([45])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 3:
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 4:
            self.service_profile_pointer.setPointer([128])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 5:
            self.service_profile_pointer.setPointer([130])
            self.gal_profile_pointer.setPointer([272])
        elif iw_option == 6:
            self.service_profile_pointer.setPointer(None)
            self.gal_profile_pointer.setPointer(None)
        elif iw_option == 7:
            self.service_profile_pointer.setPointer([21])
            self.gal_profile_pointer.setPointer(None)
        else:
            self.service_profile_pointer.setPointer(None)
            self.gal_profile_pointer.setPointer(None)

        self.gem_port_network_ctp_connectivity_pointer.setPointer([268])
        self.interworking_termination_point_pointer.setPointer([11, 268, 12])\n""",

    310: SET_POINTERS_METHOD + """
        self.multicast_operations_profile_pointer.setPointer([309])\n""",

    318: SET_POINTERS_METHOD + """
        self.local_file_name_pointer.setPointer([157])
        self.network_address_pointer.setPointer([137])
        self.gem_iwtp_pointer.setPointer([266])\n""",

    329: SET_POINTERS_METHOD + """
        self.multicast_operations_profile_pointer.setPointer([136])\n""",

}

file = open("base.txt", "r")
text = file.read()

mes_classes = """
##################################################
############## ME Class Definitions ##############
##################################################"""

me_block_pattern = re.compile(
    r'\[(\d+)\]...{\s+me_class_name\s+=\s+"(.+)"(.+[\n].+attname="(.+)".+length=(\d+).+setbycreate=(\w+).+mandatory=(\w+))*')

me_dict = "    me_dict = {\n"

mes = {}
for match in me_block_pattern.finditer(text):
    me_id = match.group(1)
    me_id_int = int(me_id)
    me_name = match.group(2)

    me_dict += '        {}: "{}",\n'.format(me_id_int, me_name[:me_name.find('-')].strip() if '-' in me_name else me_name.strip())

    attributes = []
    me_attr_pattern = re.compile(r'attname="(.+)".+length=(\d+).+setbycreate=(\w+).+mandatory=(\w+)')
    for m in me_attr_pattern.finditer(match.group()):
        name_str = m.group(1).lower().replace(' ', '_').replace('-', '_')
        attributes.append({'name_str': name_str, 'name': m.group(1), 'length': m.group(2), 'setbycreate': m.group(3), 'mandatory': m.group(4)})

    imp_link_match = re.search(r'imp_link=\((.+)\)', match.group())
    imp_link = "[{}]".format(imp_link_match.group(1).strip().rstrip(',')) if imp_link_match else "[]"

    # TODO ME NAME with '-' (ANI-G, T-CONT)
    classname = me_name[:me_name.find('-')].strip().title().replace(' ', '') if '-' in me_name else me_name.strip().title().replace(' ', '')
    mes[me_id_int] = classname

    line = """
class {}(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, {}, instance)
        self.name = \"{}\"
        self.imp_link = {}\n""".format(classname, me_id, classname, imp_link)

    for attr in attributes:
        set_by_create = "True" if "true" in attr['setbycreate'].lower() else "False"
        mandatory = "True" if "true" in attr['mandatory'].lower() else "False"
        # is_pointer = "True" if "pointer" in str(attr['name']).lower() else "False"
        line += "        self.{} = MeAttribute(\"{}\", {}, {}, {}, {})\n".format(attr['name_str'], attr['name'], attr['length'], set_by_create, mandatory, "None")

    line += "\n        self.attributes = (\n"
    for attr in attributes:
        line += "            self.{},\n".format(attr['name_str'])

    line = line[0:-1] # Remove last blank line
    line += """
        )\n"""

    line += """
    def getImplicitlyLinked(self):
        return self.imp_link\n\n"""

    if me_id_int in mes_specific_methods.keys():
        line += mes_specific_methods[me_id_int]
    else:
        line += SET_POINTERS_METHOD + "\n        pass\n"

    mes_classes += "\n" + line

attr_class = """
class MeAttribute:
    def __init__(self, name, length, setbycreate, mandatory, points_to=None, value=None):
        self.name = name
        self.length = length
        self.setbycreate = setbycreate
        self.mandatory = mandatory
        self.points_to = points_to
        self.value = value

    def getName(self):
        return self.name

    def getPointer(self):
        return self.points_to

    def setPointer(self, pointer):
        self.points_to = pointer

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getSetByCreate(self):
        return self.setbycreate

    def getLength(self):
        return self.length

    def isMandatory(self):
        return self.mandatory\n
"""

mes_translate = """
class MeTranslate:
    @staticmethod
    def getInstance(me, inst):
        if me == 0:
            return None"""
for mk in mes.keys():
    mes_translate += "\n        elif me == %d:\n            return %s(inst)" % (mk, mes[mk])

mes_translate += "\n        else:\n            return None\n"

me_dict += "    }\n"
me_class = "class ManagedEntity:\n"
me_class += me_dict
me_class += """
    def __init__(self, id, instance):
        self.me_id = id
        self.instance = instance
        self.attributes = ()
        self.name = "Default"

    def getName(self):
        return self.name

    def getId(self):
        return self.me_id

    def getInstance(self):
        return self.instance

    def setInstance(self, value):
        self.instance = value

    def getAttributes(self):
        return self.attributes

    def getAttribute(self, pos):
        if pos > len(self.attributes):
            return None

        return self.attributes[pos]

    def setAttribute(self, attr, value):
        if not len(self.attributes) or attr > len(self.attributes):
            return -1

        self.attributes[attr].setValue(value)
        return 0

    def printBeauty(self):
        line = \"\\n{} ({})\\n\".format(self.name, self.me_id)
        line += \"Instance: {}\\n\".format(self.instance)
        for attr in self.attributes:
            val = attr.getValue()

            if val is not None:
                try:
                    if attr.getLength() > 4:
                        val = val.decode()
                    else:
                        val = int.from_bytes(val, 'big')
                except Exception:
                    pass

            line += \"  {}: {}\\n\".format(attr.getName(), val)

        line += \"\\n\"
        print(line)

    def printout(self):
        line = \"ME {} ({})\\n\".format(self.name, self.me_id)
        for attr in self.attributes:
            line += \"\t{}: {}\\n\".format(attr.getName(), attr.getValue())

        line += \"\\n\"
        print(line)

    # Abstract - will be implemented on each ME, if necessary
    def setPointers(self):
        return True

    def create(self, pkt):
        attributes = pkt[8:]
        it = 0
        for i, attr in enumerate(self.attributes):
            if not attr.getSetByCreate():
                continue

            length = self.attributes[i].getLength()
            self.attributes[i].setValue(attributes[it:it+length])
            it += length

    def setAttributes(self, pkt):
        raw_mask = int.from_bytes(pkt[8:10], \'big\')
        mask = [(raw_mask >> bit) & 1 for bit in range(16 - 1, -1, -1)]
        attributes = pkt[10:]

        it = 0
        for i, attr in enumerate(mask):
            if not attr or i >= len(self.attributes):
                continue

            length = self.attributes[i].getLength()
            self.attributes[i].setValue(attributes[it:it+length])
            it += length\n
"""

with open("me_base.py", "w") as f:
    f.write(attr_class)
    f.write(me_class)
    f.write(mes_classes)
    f.write(mes_translate)
