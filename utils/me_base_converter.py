import re

# text = """
# [2] = { me_class_name = "ONT Data",
# 	{ attname="MIB Data Sync", length=1, setbycreate=false }},
# -- ADD by Maycon at 2020-08-05
#
# [4] = { me_class_name = "PON IF line card - Doesn't documented at ITU-T file G.984.4",
# 	{ attname="Not_identified", length=4, setbycreate=false },
# 	{ attname="Not_identified", length=4, setbycreate=false },
# 	{ attname="Not_identified", length=4, setbycreate=false },
# 	{ attname="Not_identified", length=4, setbycreate=false },
# 	{ attname="Not_identified", length=4, setbycreate=false },
# 	{ attname="Not_identified", length=4, setbycreate=false }},
#
# [5] = { me_class_name = "Cardholder",
# 	{ attname="Actual Plug-in Unit Type", length=1, setbycreate=false },
# 	{ attname="Expected Plug-in Unit Type", length=1, setbycreate=false },
# 	{ attname="Expected Port Count", length=1, setbycreate=false },
# 	{ attname="Expected Equipment Id", length=20, setbycreate=false },
# 	{ attname="Actual Equipment Id", length=20, setbycreate=false },
# 	{ attname="Protection Profile Pointer", length=1, setbycreate=false },
# 	{ attname="Invoke Protection Switch", length=1, setbycreate=false }},
#
# [6] = { me_class_name = "Circuit Pack",
# 	{ attname="Type", length=1, setbycreate=true },
# 	{ attname="Number of ports", length=1, setbycreate=false },
# 	{ attname="Serial Number", length=8, setbycreate=false },
# 	{ attname="Version", length=14, setbycreate=false },
# 	{ attname="Vendor Id", length=4, setbycreate=false },
# 	{ attname="Administrative State", length=1, setbycreate=true },
# 	{ attname="Operational State", length=1, setbycreate=false },
# 	{ attname="Bridged or IP Ind", length=1, setbycreate=false },
# 	{ attname="Equipment Id", length=20, setbycreate=false },
# 	{ attname="Card Configuration", length=1, setbycreate=true },
# 	{ attname="Total T-CONT Buffer Number", length=1, setbycreate=false },
# 	{ attname="Total Priority Queue Number", length=1, setbycreate=false },
# 	{ attname="Total Traffic Scheduler Number", length=1, setbycreate=false },
# 	{ attname="Power Shed Override", length=4, setbycreate=false }},
#
# [7] = { me_class_name = "Software Image",
# 	{ attname="Version", length=14, setbycreate=false },
# 	{ attname="Is committed", length=1, setbycreate=false },
# 	{ attname="Is active", length=1, setbycreate=false },
# 	{ attname="Is valid", length=1, setbycreate=false }},
#
# [11] = { me_class_name = "PPTP Ethernet UNI",
# 	{attname="Expected Type", length=1, setbycreate=false},
# 	{attname="Sensed Type", length=1, setbycreate=false},
# 	{attname="Auto Detection Configuration", length=1, setbycreate=false},
# 	{attname="Ethernet Loopback Configuration",	length=1, setbycreate=false},
# 	{attname="Administrative State", length=1, setbycreate=false},
# 	{attname="Operational State", length=1, setbycreate=false},
# 	{attname="Configuration Ind", length=1, setbycreate=false},
# 	{attname="Max Frame Size", length=2, setbycreate=false},
# 	{attname="DTE or DCE", length=1, setbycreate=false},
# 	{attname="Pause Time", length=2, setbycreate=false},
# 	{attname="Bridged or IP Ind", length=1, setbycreate=false},
# 	{attname="ARC", length=1, setbycreate=false},
# 	{attname="ARC Interval", length=1, setbycreate=false},
# 	{attname="PPPoE Filter", length=1, setbycreate=false},
# 	{attname="Power Control", length=1, setbycreate=false}},
#
# [24] = { me_class_name = "Ethernet PM History Data",
# 	{ attname="Interval End Time", length=1, setbycreate=false }, -- 1
# 	{ attname="Threshold Data 1/2 Id", length=2, setbycreate=true }, --2
# 	{ attname="FCS errors Drop events", length=4, setbycreate=false }, -- 3
# 	{ attname="Excessive Collision Counter", length=4, setbycreate=false }, -- 4
# 	{ attname="Late Collision Counter", length=4, setbycreate=false }, -- 5
# 	{ attname="Frames too long", length=4, setbycreate=false },
# 	{ attname="Buffer overflows on Receive", length=4, setbycreate=false },
# 	{ attname="Buffer overflows on Transmit", length=4, setbycreate=false },
# 	{ attname="Single Collision Frame Counter", length=4, setbycreate=false },
# 	{ attname="Multiple Collisions Frame Counter", length=4, setbycreate=false },
# 	{ attname="SQE counter", length=4, setbycreate=false },
# 	{ attname="Deferred Transmission Counter", length=4, setbycreate=false },
# 	{ attname="Internal MAC Transmit Error Counter", length=4, setbycreate=false },
# 	{ attname="Carrier Sense Error Counter", length=4, setbycreate=false },
# 	{ attname="Alignment Error Counter", length=4, setbycreate=false },
# 	{ attname="Internal MAC Receive Error Counter", length=4, setbycreate=false}},
#
# -- ADD by Maycon at 2020-08-05
# [40] = { me_class_name = "PON physical path termination point - Doesn't documented at ITU-T file G.984.4",
# 	{ attname="Not_identified", length=4, setbycreate=false }},
#
# [44] = { me_class_name = "Vendor Specific",
# 	{ attname="Sub-Entity", length=1, setbycreate=true },
# 	subentity_attr = {}},
#
# [45] = { me_class_name = "MAC Bridge Service Profile",
# 	{ attname="Spanning tree ind", length=1, setbycreate=true },
# 	{ attname="Learning ind", length=1, setbycreate=true },
# 	{ attname="Port bridging ind", length=1, setbycreate=true },
# 	{ attname="Priority", length=2, setbycreate=true },
# 	{ attname="Max age", length=2, setbycreate=true },
# 	{ attname="Hello time", length=2, setbycreate=true },
# 	{ attname="Forward delay", length=2, setbycreate=true },
# 	{ attname="Unknown MAC address discard", length=1, setbycreate=true },
# 	{ attname="MAC learning depth", length=1, setbycreate=true }},
#
# [47] = { me_class_name = "MAC bridge port configuration data",
# 	{ attname="Bridge id pointer", length=2, setbycreate=true },
# 	{ attname="Port num", length=1, setbycreate=true },
# 	{ attname="TP type", length=1, setbycreate=true },
# 	{ attname="TP pointer", length=2, setbycreate=true },
# 	{ attname="Port priority", length=2, setbycreate=true },
# 	{ attname="Port path cost", length=2, setbycreate=true },
# 	{ attname="Port spanning tree ind", length=1, setbycreate=true },
# 	{ attname="Encapsulation method", length=1, setbycreate=true },
# 	{ attname="LAN FCS ind", length=1, setbycreate=true },
# 	{ attname="Port MAC address", length=6, setbycreate=false },
# 	{ attname="Outbound TD pointer", length=2, setbycreate=false },
# 	{ attname="Inbound TD pointer", length=2, setbycreate=false }},
#
# [48] = { me_class_name = "MAC bridge port designation data",
# 	{ attname="Designated bridge root cost port", length=24, setbycreate=false },
# 	{ attname="Port state", length=1, setbycreate=false }},
#
# [49] = { me_class_name = "MAC bridge port filter table data",
# 	{ attname="MAC filter table", length=8, setbycreate=false }},
#
# [51] = { me_class_name = "MAC Bridge PM History Data",
# 	{ attname="Interval end time", length=1, setbycreate=false },
# 	{ attname="Threshold data 1/2 id", length=2, setbycreate=true },
# 	{ attname="Bridge learning entry discard count", length=4, setbycreate=false }},
#
# """

file = open("base.txt", "r")
text = file.read()

mes_classes = """
##################################################
############## ME Class Definitions ##############
##################################################"""

me_block_pattern = re.compile(
    r'\[(\d+)\]...{\s+me_class_name\s+=\s+"(.+)"(.+[\n].+attname="(.+)".+length=(\d+).+setbycreate=(\w+))*')
for match in me_block_pattern.finditer(text):
    me_id = match.group(1)
    me_name = match.group(2)

    attributes = []
    me_attr_pattern = re.compile(r'attname="(.+)".+length=(\d+).+setbycreate=(\w+)')
    for m in me_attr_pattern.finditer(match.group()):
        name_str = m.group(1).lower().replace(' ', '_').replace('-', '_')
        attributes.append({'name_str': name_str, 'name': m.group(1), 'length': m.group(2), 'setbycreate': m.group(2)})

    classname = me_name[:me_name.find('-')].strip().title().replace(' ', '') if '-' in me_name else me_name.strip().title().replace(' ', '')
    line = "\nclass {}:\n    def __init__(self):\n".format(classname)
    for attr in attributes:
        set_by_create = "True" if attr['setbycreate']  == "true" else "False"
        line += "        self.{} = MeAttribute(\"{}\", {}, {}, False)\n".format(attr['name_str'], attr['name'], attr['length'], set_by_create)

    line += "\n        self.attributes = (\n"
    for attr in attributes:
        line += "            self.{},\n".format(attr['name_str'])

    line = line[0:-1] # Remove last blank line
    line += """
        )
    
    def getAttributes(self):
        return self.attributes

    def getAttribute(self, pos):
        if pos > len(self.attributes):
            return None

        return self.attributes[pos-1]

    def setAttribute(self, attr, value):
        if attr > len(self.attributes):
            return -1

        self.attributes[attr-1].setValue(value)
        return 0
    """

    mes_classes += "\n" + line

attr_class = """
class MeAttribute:
    def __init__(self, name, length, setbycreate, mandatory, value=None):
        self.name = name
        self.length = length
        self.setbycreate = setbycreate
        self.mandatory = mandatory
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self, value):
        return value

"""

with open("me_base.py", "w") as f:
    f.write(attr_class)
    f.write(mes_classes)
