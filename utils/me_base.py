
class MeAttribute:
    READ_PERMISSION = 1
    WRITE_PERMISSION = 2
    READ_WRITE_PERMISSION = 3

    def __init__(self, name, length, setbycreate, mandatory, permissions, points_to=None, value=None):
        self.name = name
        self.length = length
        self.setbycreate = setbycreate
        self.mandatory = mandatory
        self.points_to = points_to
        self.value = value
        self.permissions = permissions

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
        return self.mandatory

    def getPermissions(self):
        return self.permissions

class ManagedEntity:
    me_dict = {
        2: "ONT Data",
        4: "PON IF line card",
        5: "Cardholder",
        6: "Circuit Pack",
        7: "Software Image",
        11: "PPTP Ethernet UNI",
        24: "Ethernet PM History Data",
        40: "PON physical path termination point",
        44: "Vendor Specific",
        45: "MAC Bridge Service Profile",
        47: "MAC bridge port configuration data",
        48: "MAC bridge port designation data",
        49: "MAC bridge port filter table data",
        51: "MAC Bridge PM History Data",
        52: "MAC Bridge Port PM History Data",
        53: "Physical path termination point POTS UNI",
        58: "Voice service profile",
        79: "MAC bridge port filter preassign table",
        82: "PPTP Video UNI",
        84: "VLAN tagging filter data",
        89: "Ethernet PM History Data 2",
        90: "PPTP Video ANI",
        130: "IEEE 8021P Mapper Service Profile",
        131: "OLT",
        133: "ONT Power Shedding",
        134: "IP host config data",
        136: "TCP UDP config data",
        137: "Network address",
        138: "VoIP config data",
        139: "VoIP voice CTP",
        141: "VoIP line status",
        142: "VoIP media profile",
        143: "RTP profile data",
        148: "Authentication security method",
        150: "SIP agent config data",
        153: "SIP user data",
        157: "Large string",
        158: "ONT remote debug",
        159: "Equipment protection profile",
        160: "Equipment extension package",
        171: "Extended VLAN tagging operation configuration data",
        250: "PPPoE BY GCOM",
        255: "Ethernet performance monitoring history data 4",
        256: "ONT",
        257: "ONT2",
        261: "PON TC adapter",
        262: "TCONT",
        263: "ANIG",
        264: "UNI",
        266: "GEM interworking Termination Point",
        267: "GEM Port PM History Data",
        268: "GEM Port Network CTP",
        271: "GAL TDM profile",
        272: "GAL Ethernet profile",
        273: "Threshold Data 1",
        274: "Threshold Data 2",
        275: "GAL TDM PM History Data",
        276: "GAL Ethernet PM History Data",
        277: "Priority queue",
        278: "Traffic Scheduler",
        279: "Protection data",
        281: "Multicast GEM interworking termination point",
        287: "OMCI",
        290: "Dot1X Port Extension Package",
        291: "Dot1X configuration profile",
        296: "Ethernet PM History Data 3",
        297: "Port mapping package",
        309: "Multicast operations profile",
        310: "Multicast subscriber config info",
        311: "Multicast Subscriber Monitor",
        312: "FEC PM History Data",
        318: "File transfer controller",
        321: "Ethernet Frame PM History Data DS",
        322: "Ethernet Frame PM History Data US",
        329: "Virtual Ethernet interface point",
        340: "BBF TR",
        341: "GEM port network CTP performance monitoring history data",
        65303: "PPPoE INTELBRAS OLT 8820i 110Gi",
        65320: "Wan Extended Config FH",
        65321: "WAN Profile File FH",
        65322: "WAN Mode FH",
        65323: "WAN CONFIG FH",
        65324: "WAN PORT BIND FH",
        65329: "WAN WAN Profile FH",
        65326: "Wifi General Config",
        65327: "Wifi Advance Config",
        65338: "WAN Extended VLAN FH",
        65529: "ONU Capability",
        65530: "LOID Authentication",
        999999: "DEFAULT",
    }

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
        line = "\n{} ({})\n".format(self.name, self.me_id)
        line += "Instance: {}\n".format(self.instance)
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

            line += "  {}: {}\n".format(attr.getName(), val)

        line += "\n"
        print(line)

    def printout(self):
        line = "ME {} ({})\n".format(self.name, self.me_id)
        for attr in self.attributes:
            line += "	{}: {}\n".format(attr.getName(), attr.getValue())

        line += "\n"
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
        raw_mask = int.from_bytes(pkt[8:10], 'big')
        mask = [(raw_mask >> bit) & 1 for bit in range(16 - 1, -1, -1)]
        attributes = pkt[10:]

        it = 0
        for i, attr in enumerate(mask):
            if not attr or i >= len(self.attributes):
                continue

            length = self.attributes[i].getLength()
            self.attributes[i].setValue(attributes[it:it+length])
            it += length


##################################################
############## ME Class Definitions ##############
##################################################

class OntData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 2, instance)
        self.name = "OntData"
        self.imp_link = []

        self.attributes = (
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PonIfLineCard(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 4, instance)
        self.name = "PonIfLineCard"
        self.imp_link = []

        self.attributes = (
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Cardholder(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 5, instance)
        self.name = "Cardholder"
        self.imp_link = []
        self.actual_plug_in_unit_type = MeAttribute("Actual Plug-in Unit Type", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.expected_plug_in_unit_type = MeAttribute("Expected Plug-in Unit Type", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.expected_port_count = MeAttribute("Expected Port Count", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.expected_equipment_id = MeAttribute("Expected Equipment Id", 20, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.actual_equipment_id = MeAttribute("Actual Equipment Id", 20, False, False, MeAttribute.READ_PERMISSION, None)
        self.protection_profile_pointer = MeAttribute("Protection Profile Pointer", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.invoke_protection_switch = MeAttribute("Invoke Protection Switch", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.actual_plug_in_unit_type,
            self.expected_plug_in_unit_type,
            self.expected_port_count,
            self.expected_equipment_id,
            self.actual_equipment_id,
            self.protection_profile_pointer,
            self.invoke_protection_switch,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class CircuitPack(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 6, instance)
        self.name = "CircuitPack"
        self.imp_link = []
        self.type = MeAttribute("Type", 1, True, True, MeAttribute.READ_PERMISSION, None)
        self.number_of_ports = MeAttribute("Number of ports", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.serial_number = MeAttribute("Serial Number", 8, False, True, MeAttribute.READ_PERMISSION, None)
        self.version = MeAttribute("Version", 14, False, True, MeAttribute.READ_PERMISSION, None)
        self.vendor_id = MeAttribute("Vendor Id", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.administrative_state = MeAttribute("Administrative State", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.bridged_or_ip_ind = MeAttribute("Bridged or IP Ind", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.equipment_id = MeAttribute("Equipment Id", 20, False, False, MeAttribute.READ_PERMISSION, None)
        self.card_configuration = MeAttribute("Card Configuration", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.total_t_cont_buffer_number = MeAttribute("Total T-CONT Buffer Number", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.total_priority_queue_number = MeAttribute("Total Priority Queue Number", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.total_traffic_scheduler_number = MeAttribute("Total Traffic Scheduler Number", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.power_shed_override = MeAttribute("Power Shed Override", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.type,
            self.number_of_ports,
            self.serial_number,
            self.version,
            self.vendor_id,
            self.administrative_state,
            self.operational_state,
            self.bridged_or_ip_ind,
            self.equipment_id,
            self.card_configuration,
            self.total_t_cont_buffer_number,
            self.total_priority_queue_number,
            self.total_traffic_scheduler_number,
            self.power_shed_override,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class SoftwareImage(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 7, instance)
        self.name = "SoftwareImage"
        self.imp_link = []
        self.version = MeAttribute("Version", 14, False, True, MeAttribute.READ_PERMISSION, None)
        self.is_committed = MeAttribute("Is committed", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.is_active = MeAttribute("Is active", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.is_valid = MeAttribute("Is valid", 1, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.version,
            self.is_committed,
            self.is_active,
            self.is_valid,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PptpEthernetUni(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 11, instance)
        self.name = "PptpEthernetUni"
        self.imp_link = []
        self.expected_type = MeAttribute("Expected Type", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sensed_type = MeAttribute("Sensed Type", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.auto_detection_configuration = MeAttribute("Auto Detection Configuration", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ethernet_loopback_configuration = MeAttribute("Ethernet Loopback Configuration", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.administrative_state = MeAttribute("Administrative State", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.configuration_ind = MeAttribute("Configuration Ind", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.max_frame_size = MeAttribute("Max Frame Size", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dte_or_dce = MeAttribute("DTE or DCE", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pause_time = MeAttribute("Pause Time", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.bridged_or_ip_ind = MeAttribute("Bridged or IP Ind", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc = MeAttribute("ARC", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pppoe_filter = MeAttribute("PPPoE Filter", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.power_control = MeAttribute("Power Control", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.expected_type,
            self.sensed_type,
            self.auto_detection_configuration,
            self.ethernet_loopback_configuration,
            self.administrative_state,
            self.operational_state,
            self.configuration_ind,
            self.max_frame_size,
            self.dte_or_dce,
            self.pause_time,
            self.bridged_or_ip_ind,
            self.arc,
            self.arc_interval,
            self.pppoe_filter,
            self.power_control,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EthernetPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 24, instance)
        self.name = "EthernetPmHistoryData"
        self.imp_link = [11]
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.fcs_errors_drop_events = MeAttribute("FCS errors Drop events", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.excessive_collision_counter = MeAttribute("Excessive Collision Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.late_collision_counter = MeAttribute("Late Collision Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.frames_too_long = MeAttribute("Frames too long", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.buffer_overflows_on_receive = MeAttribute("Buffer overflows on Receive", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.buffer_overflows_on_transmit = MeAttribute("Buffer overflows on Transmit", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.single_collision_frame_counter = MeAttribute("Single Collision Frame Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.multiple_collisions_frame_counter = MeAttribute("Multiple Collisions Frame Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.sqe_counter = MeAttribute("SQE counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.deferred_transmission_counter = MeAttribute("Deferred Transmission Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.internal_mac_transmit_error_counter = MeAttribute("Internal MAC Transmit Error Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.carrier_sense_error_counter = MeAttribute("Carrier Sense Error Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.alignment_error_counter = MeAttribute("Alignment Error Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.internal_mac_receive_error_counter = MeAttribute("Internal MAC Receive Error Counter", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.fcs_errors_drop_events,
            self.excessive_collision_counter,
            self.late_collision_counter,
            self.frames_too_long,
            self.buffer_overflows_on_receive,
            self.buffer_overflows_on_transmit,
            self.single_collision_frame_counter,
            self.multiple_collisions_frame_counter,
            self.sqe_counter,
            self.deferred_transmission_counter,
            self.internal_mac_transmit_error_counter,
            self.carrier_sense_error_counter,
            self.alignment_error_counter,
            self.internal_mac_receive_error_counter,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PonPhysicalPathTerminationPoint(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 40, instance)
        self.name = "PonPhysicalPathTerminationPoint"
        self.imp_link = []
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.not_identified,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class VendorSpecific(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 44, instance)
        self.name = "VendorSpecific"
        self.imp_link = []
        self.sub_entity = MeAttribute("Sub-Entity", 1, True, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.sub_entity,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MacBridgeServiceProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 45, instance)
        self.name = "MacBridgeServiceProfile"
        self.imp_link = []
        self.spanning_tree_ind = MeAttribute("Spanning tree ind", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.learning_ind = MeAttribute("Learning ind", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_bridging_ind = MeAttribute("Port bridging ind", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.priority = MeAttribute("Priority", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.max_age = MeAttribute("Max age", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.hello_time = MeAttribute("Hello time", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.forward_delay = MeAttribute("Forward delay", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.unknown_mac_address_discard = MeAttribute("Unknown MAC address discard", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.mac_learning_depth = MeAttribute("MAC learning depth", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.spanning_tree_ind,
            self.learning_ind,
            self.port_bridging_ind,
            self.priority,
            self.max_age,
            self.hello_time,
            self.forward_delay,
            self.unknown_mac_address_discard,
            self.mac_learning_depth,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MacBridgePortConfigurationData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 47, instance)
        self.name = "MacBridgePortConfigurationData"
        self.imp_link = [48, 49, 52, 84, 311, 321, 322]
        self.bridge_id_pointer = MeAttribute("Bridge id pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_num = MeAttribute("Port num", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tp_type = MeAttribute("TP type", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tp_pointer = MeAttribute("TP pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_priority = MeAttribute("Port priority", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_path_cost = MeAttribute("Port path cost", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_spanning_tree_ind = MeAttribute("Port spanning tree ind", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.encapsulation_method = MeAttribute("Encapsulation method", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.lan_fcs_ind = MeAttribute("LAN FCS ind", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.port_mac_address = MeAttribute("Port MAC address", 6, False, False, MeAttribute.READ_PERMISSION, None)
        self.outbound_td_pointer = MeAttribute("Outbound TD pointer", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.inbound_td_pointer = MeAttribute("Inbound TD pointer", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.bridge_id_pointer,
            self.port_num,
            self.tp_type,
            self.tp_pointer,
            self.port_priority,
            self.port_path_cost,
            self.port_spanning_tree_ind,
            self.encapsulation_method,
            self.lan_fcs_ind,
            self.port_mac_address,
            self.outbound_td_pointer,
            self.inbound_td_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
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
        self.inbound_td_pointer.setPointer([280])


class MacBridgePortDesignationData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 48, instance)
        self.name = "MacBridgePortDesignationData"
        self.imp_link = [47]
        self.designated_bridge_root_cost_port = MeAttribute("Designated bridge root cost port", 24, False, True, MeAttribute.READ_PERMISSION, None)
        self.port_state = MeAttribute("Port state", 1, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.designated_bridge_root_cost_port,
            self.port_state,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MacBridgePortFilterTableData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 49, instance)
        self.name = "MacBridgePortFilterTableData"
        self.imp_link = [47]
        self.mac_filter_table = MeAttribute("MAC filter table", 8, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.mac_filter_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MacBridgePmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 51, instance)
        self.name = "MacBridgePmHistoryData"
        self.imp_link = [45]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.bridge_learning_entry_discard_count = MeAttribute("Bridge learning entry discard count", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.bridge_learning_entry_discard_count,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MacBridgePortPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 52, instance)
        self.name = "MacBridgePortPmHistoryData"
        self.imp_link = [47]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.forwarded_frame_counter = MeAttribute("Forwarded frame counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.delay_exceeded_discard_counter = MeAttribute("Delay exceeded discard counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.mtu_exceeded_discard_counter = MeAttribute("MTU exceeded discard counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_frame_counter = MeAttribute("Received frame counter", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_and_discarded_counter = MeAttribute("Received and discarded counter", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.forwarded_frame_counter,
            self.delay_exceeded_discard_counter,
            self.mtu_exceeded_discard_counter,
            self.received_frame_counter,
            self.received_and_discarded_counter,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PhysicalPathTerminationPointPotsUni(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 53, instance)
        self.name = "PhysicalPathTerminationPointPotsUni"
        self.imp_link = []
        self.administrative_state = MeAttribute("Administrative state", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.deprecated = MeAttribute("Deprecated", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc = MeAttribute("ARC", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc_interval = MeAttribute("ARC interval", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.impedance = MeAttribute("Impedance", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.transmission_path = MeAttribute("Transmission path", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.rx_gain = MeAttribute("Rx gain", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tx_gain = MeAttribute("Tx gain", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.hook_state = MeAttribute("Hook state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.pots_holdover_time = MeAttribute("POTS holdover time", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.nominal_feed_voltage = MeAttribute("Nominal feed voltage", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.administrative_state,
            self.deprecated,
            self.arc,
            self.arc_interval,
            self.impedance,
            self.transmission_path,
            self.rx_gain,
            self.tx_gain,
            self.operational_state,
            self.hook_state,
            self.pots_holdover_time,
            self.nominal_feed_voltage,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class VoiceServiceProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 58, instance)
        self.name = "VoiceServiceProfile"
        self.imp_link = []
        self.announcement_type = MeAttribute("Announcement type", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.jitter_target = MeAttribute("Jitter target", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.jitter_buffer_max = MeAttribute("Jitter buffer max", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.echo_cancel_ind = MeAttribute("Echo cancel ind", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pstn_protocol_variant = MeAttribute("PSTN protocol variant", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dtmf_digit_levels = MeAttribute("DTMF digit levels", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dtmf_digit_duration = MeAttribute("DTMF digit duration", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.hook_flash_minimum_time = MeAttribute("Hook flash minimum time", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.hook_flash_maximum_time = MeAttribute("Hook flash maximum time", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tone_pattern_table = MeAttribute("Tone pattern table", 20, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tone_event_table = MeAttribute("Tone event table", 7, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ringing_pattern_table = MeAttribute("Ringing pattern table", 5, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ringing_event_table = MeAttribute("Ringing event table", 7, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.network_specific_extensions_pointer = MeAttribute("Network specific extensions pointer", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.announcement_type,
            self.jitter_target,
            self.jitter_buffer_max,
            self.echo_cancel_ind,
            self.pstn_protocol_variant,
            self.dtmf_digit_levels,
            self.dtmf_digit_duration,
            self.hook_flash_minimum_time,
            self.hook_flash_maximum_time,
            self.tone_pattern_table,
            self.tone_event_table,
            self.ringing_pattern_table,
            self.ringing_event_table,
            self.network_specific_extensions_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.network_specific_extensions_pointer.setPointer([137])


class MacBridgePortFilterPreassignTable(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 79, instance)
        self.name = "MacBridgePortFilterPreassignTable"
        self.imp_link = []
        self.ipv4_multicast_filtering = MeAttribute("IPv4 multicast filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ipv6_multicast_filtering = MeAttribute("IPv6 multicast filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ipv4_broadcast_filtering = MeAttribute("IPv4 broadcast filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.rarp_filtering = MeAttribute("RARP filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ipx_filtering = MeAttribute("IPX filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.netbeui_filtering = MeAttribute("NetBEUI filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.appletalk_filtering = MeAttribute("AppleTalk filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.bridge_management_information_filtering = MeAttribute("Bridge management information filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arp_filtering = MeAttribute("ARP filtering", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.ipv4_multicast_filtering,
            self.ipv6_multicast_filtering,
            self.ipv4_broadcast_filtering,
            self.rarp_filtering,
            self.ipx_filtering,
            self.netbeui_filtering,
            self.appletalk_filtering,
            self.bridge_management_information_filtering,
            self.arp_filtering,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PptpVideoUni(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 82, instance)
        self.name = "PptpVideoUni"
        self.imp_link = []
        self.administrative_state = MeAttribute("Administrative State", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.arc = MeAttribute("ARC", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.power_control = MeAttribute("Power Control", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.administrative_state,
            self.operational_state,
            self.arc,
            self.arc_interval,
            self.power_control,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class VlanTaggingFilterData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 84, instance)
        self.name = "VlanTaggingFilterData"
        self.imp_link = [47]
        self.vlan_filter_list = MeAttribute("VLAN filter list", 24, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.forward_operation = MeAttribute("Forward operation", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.number_of_entries = MeAttribute("Number of entries", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.vlan_filter_list,
            self.forward_operation,
            self.number_of_entries,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EthernetPmHistoryData2(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 89, instance)
        self.name = "EthernetPmHistoryData2"
        self.imp_link = [11]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pppoe_filtered_frame_counter = MeAttribute("PPPoE filtered frame counter", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.pppoe_filtered_frame_counter,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PptpVideoAni(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 90, instance)
        self.name = "PptpVideoAni"
        self.imp_link = []
        self.administrative_state = MeAttribute("Administrative State", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.arc = MeAttribute("ARC", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.frequency_range_low = MeAttribute("Frequency Range Low", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.frequency_range_high = MeAttribute("Frequency Range High", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.signal_capability = MeAttribute("Signal Capability", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.optical_signal_level = MeAttribute("Optical Signal Level", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.pilot_signal_level = MeAttribute("Pilot Signal Level", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.signal_level_min = MeAttribute("Signal Level min", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.signal_level_max = MeAttribute("Signal Level max", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.pilot_frequency = MeAttribute("Pilot Frequency", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.agc_mode = MeAttribute("AGC Mode", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.agc_setting = MeAttribute("AGC Setting", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.video_lower_optical_threshold = MeAttribute("Video Lower Optical Threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.video_upper_optical_threshold = MeAttribute("Video Upper Optical Threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.administrative_state,
            self.operational_state,
            self.arc,
            self.arc_interval,
            self.frequency_range_low,
            self.frequency_range_high,
            self.signal_capability,
            self.optical_signal_level,
            self.pilot_signal_level,
            self.signal_level_min,
            self.signal_level_max,
            self.pilot_frequency,
            self.agc_mode,
            self.agc_setting,
            self.video_lower_optical_threshold,
            self.video_upper_optical_threshold,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Ieee8021PMapperServiceProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 130, instance)
        self.name = "Ieee8021PMapperServiceProfile"
        self.imp_link = []

        self.attributes = (
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
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
        self.interwork_tp_pointer_for_p_bit_priority_7.setPointer([266,281,404])


class Olt(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 131, instance)
        self.name = "Olt"
        self.imp_link = []
        self.olt_vendor_id = MeAttribute("OLT vendor id", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.equipment_id = MeAttribute("Equipment id", 20, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.olt_version = MeAttribute("OLT version", 14, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.olt_vendor_id,
            self.equipment_id,
            self.olt_version,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class OntPowerShedding(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 133, instance)
        self.name = "OntPowerShedding"
        self.imp_link = []
        self.restore_power_timer_reset_interval = MeAttribute("Restore power timer reset interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.data_class_shedding_interval = MeAttribute("Data class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voice_class_shedding_interval = MeAttribute("Voice class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.video_overlay_class_shedding_interval = MeAttribute("Video overlay class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.video_return_class_shedding_interval = MeAttribute("Video return class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dsl_class_shedding_interval = MeAttribute("DSL class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.atm_class_shedding_interval = MeAttribute("ATM class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ces_class_shedding_interval = MeAttribute("CES class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.frame_class_shedding_interval = MeAttribute("Frame class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sonet_class_shedding_interval = MeAttribute("SONET class shedding interval", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.shedding_status = MeAttribute("Shedding status", 2, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.restore_power_timer_reset_interval,
            self.data_class_shedding_interval,
            self.voice_class_shedding_interval,
            self.video_overlay_class_shedding_interval,
            self.video_return_class_shedding_interval,
            self.dsl_class_shedding_interval,
            self.atm_class_shedding_interval,
            self.ces_class_shedding_interval,
            self.frame_class_shedding_interval,
            self.sonet_class_shedding_interval,
            self.shedding_status,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class IpHostConfigData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 134, instance)
        self.name = "IpHostConfigData"
        self.imp_link = []
        self.ip_options = MeAttribute("IP options", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.mac_address = MeAttribute("MAC address", 6, False, True, MeAttribute.READ_PERMISSION, None)
        self.ont_identifier = MeAttribute("Ont identifier", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ip_address = MeAttribute("IP address", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.mask = MeAttribute("Mask", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.gateway = MeAttribute("Gateway", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.primary_dns = MeAttribute("Primary DNS", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.secondary_dns = MeAttribute("Secondary DNS", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.current_address = MeAttribute("Current address", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.current_mask = MeAttribute("Current mask", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.current_gateway = MeAttribute("Current gateway", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.current_primary_dns = MeAttribute("Current primary DNS", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.current_secondary_dns = MeAttribute("Current secondary DNS", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.domain_name = MeAttribute("Domain name", 25, False, True, MeAttribute.READ_PERMISSION, None)
        self.host_name = MeAttribute("Host name", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.ip_options,
            self.mac_address,
            self.ont_identifier,
            self.ip_address,
            self.mask,
            self.gateway,
            self.primary_dns,
            self.secondary_dns,
            self.current_address,
            self.current_mask,
            self.current_gateway,
            self.current_primary_dns,
            self.current_secondary_dns,
            self.domain_name,
            self.host_name,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class TcpUdpConfigData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 136, instance)
        self.name = "TcpUdpConfigData"
        self.imp_link = []
        self.port_id = MeAttribute("Port ID", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.protocol = MeAttribute("Protocol", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tos_diffserv_field = MeAttribute("TOS diffserv field", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ip_host_pointer = MeAttribute("IP host pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.port_id,
            self.protocol,
            self.tos_diffserv_field,
            self.ip_host_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.ip_host_pointer.setPointer([134,347])


class NetworkAddress(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 137, instance)
        self.name = "NetworkAddress"
        self.imp_link = []
        self.security_pointer = MeAttribute("Security pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.address_pointer = MeAttribute("Address pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.security_pointer,
            self.address_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.security_pointer.setPointer([148])
        self.address_pointer.setPointer([157])


class VoipConfigData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 138, instance)
        self.name = "VoipConfigData"
        self.imp_link = []
        self.available_signalling_protocols = MeAttribute("Available signalling protocols", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.signalling_protocol_used = MeAttribute("Signalling protocol used", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.available_voip_configuration_methods = MeAttribute("Available VoIP configuration methods", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_configuration_method_used = MeAttribute("VoIP configuration method used", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voip_configuration_address_pointer = MeAttribute("VoIP configuration address pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voip_configuration_state = MeAttribute("VoIP configuration state", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.retrieve_profile = MeAttribute("Retrieve profile", 1, False, True, MeAttribute.WRITE_PERMISSION, None)
        self.profile_version = MeAttribute("Profile version", 25, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.available_signalling_protocols,
            self.signalling_protocol_used,
            self.available_voip_configuration_methods,
            self.voip_configuration_method_used,
            self.voip_configuration_address_pointer,
            self.voip_configuration_state,
            self.retrieve_profile,
            self.profile_version,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.voip_configuration_address_pointer.setPointer([137])


class VoipVoiceCtp(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 139, instance)
        self.name = "VoipVoiceCtp"
        self.imp_link = []
        self.user_protocol_pointer = MeAttribute("User protocol pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pptp_pointer = MeAttribute("PPTP pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voip_media_profile_pointer = MeAttribute("VoIP media profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.signalling_code = MeAttribute("Signalling code", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.user_protocol_pointer,
            self.pptp_pointer,
            self.voip_media_profile_pointer,
            self.signalling_code,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.user_protocol_pointer.setPointer([153, 155])
        self.pptp_pointer.setPointer([53])
        self.voip_media_profile_pointer.setPointer([142])


class VoipLineStatus(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 141, instance)
        self.name = "VoipLineStatus"
        self.imp_link = [53]
        self.voip_codec_used = MeAttribute("voip codec used", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_voice_server_status = MeAttribute("voip voice server status", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_port_session_type = MeAttribute("voip port session type", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_call_1_packetperiod = MeAttribute("voip call 1 packetperiod", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_call_2_packetperiod = MeAttribute("voip call 2 packetperiod", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_call_1_dest_addr = MeAttribute("voip call 1 dest addr", 25, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_call_2_dest_addr = MeAttribute("voip call 2 dest addr", 25, False, True, MeAttribute.READ_PERMISSION, None)
        self.voip_line_state = MeAttribute("Voip line state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.emergency_call_status = MeAttribute("Emergency call status", 1, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.voip_codec_used,
            self.voip_voice_server_status,
            self.voip_port_session_type,
            self.voip_call_1_packetperiod,
            self.voip_call_2_packetperiod,
            self.voip_call_1_dest_addr,
            self.voip_call_2_dest_addr,
            self.voip_line_state,
            self.emergency_call_status,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class VoipMediaProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 142, instance)
        self.name = "VoipMediaProfile"
        self.imp_link = []
        self.fax_mode = MeAttribute("Fax mode", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voice_service_profile_pointer = MeAttribute("Voice service profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.codec_selection_first_order = MeAttribute("Codec selection first order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.packet_period_selection_first_order = MeAttribute("Packet period selection first order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.silence_suppression_first_order = MeAttribute("Silence suppression first order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.codec_selection_second_order = MeAttribute("Codec selection second order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.packet_period_selection_second_order = MeAttribute("Packet period selection second order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.silence_suppression_second_order = MeAttribute("Silence suppression second order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.codec_selection_third_order = MeAttribute("Codec selection third order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.packet_period_selection_third_order = MeAttribute("Packet period selection third order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.silence_suppression_fourth_order = MeAttribute("Silence suppression fourth order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.codec_selection_fourth_order = MeAttribute("Codec selection fourth order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.packet_period_selection_fourth_order = MeAttribute("Packet period selection fourth order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.silence_suppression_fourth_order = MeAttribute("Silence suppression fourth order", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.oob_dtmf = MeAttribute("OOB DTMF", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.rtp_profile_pointer = MeAttribute("RTP profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.fax_mode,
            self.voice_service_profile_pointer,
            self.codec_selection_first_order,
            self.packet_period_selection_first_order,
            self.silence_suppression_first_order,
            self.codec_selection_second_order,
            self.packet_period_selection_second_order,
            self.silence_suppression_second_order,
            self.codec_selection_third_order,
            self.packet_period_selection_third_order,
            self.silence_suppression_fourth_order,
            self.codec_selection_fourth_order,
            self.packet_period_selection_fourth_order,
            self.silence_suppression_fourth_order,
            self.oob_dtmf,
            self.rtp_profile_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.voice_service_profile_pointer.setPointer([58])
        self.rtp_profile_pointer.setPointer([143])


class RtpProfileData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 143, instance)
        self.name = "RtpProfileData"
        self.imp_link = []
        self.local_port_min = MeAttribute("Local port min", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.local_port_max = MeAttribute("Local port max", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dscp_mark = MeAttribute("DSCP mark", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.piggyback_events = MeAttribute("Piggyback events", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tone_events = MeAttribute("Tone events", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dtmf_events = MeAttribute("DTMF events", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.cas_events = MeAttribute("CAS events", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ip_host_config_pointer = MeAttribute("IP host config pointer", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.local_port_min,
            self.local_port_max,
            self.dscp_mark,
            self.piggyback_events,
            self.tone_events,
            self.dtmf_events,
            self.cas_events,
            self.ip_host_config_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.ip_host_config_pointer.setPointer([134, 347])


class AuthenticationSecurityMethod(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 148, instance)
        self.name = "AuthenticationSecurityMethod"
        self.imp_link = []
        self.validation_scheme = MeAttribute("Validation scheme", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.username_1 = MeAttribute("Username 1", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.password = MeAttribute("Password", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.realm = MeAttribute("Realm", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.username_2 = MeAttribute("Username 2", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.validation_scheme,
            self.username_1,
            self.password,
            self.realm,
            self.username_2,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class SipAgentConfigData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 150, instance)
        self.name = "SipAgentConfigData"
        self.imp_link = []
        self.proxy_server_address_pointer = MeAttribute("Proxy server address pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.outbound_proxy_address_pointer = MeAttribute("Outbound proxy address pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.primary_sip_dns = MeAttribute("Primary SIP DNS", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.secondary_sip_dns = MeAttribute("Secondary SIP DNS", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tcp_udp_pointer = MeAttribute("TCP UDP pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_reg_exp_time = MeAttribute("SIP reg exp time", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_rereg_head_start_time = MeAttribute("SIP rereg head start time", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.host_part_uri = MeAttribute("Host part URI", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_status = MeAttribute("SIP status", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.sip_registrar = MeAttribute("SIP registrar", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.softswitch = MeAttribute("Softswitch", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_response_table = MeAttribute("SIP response table", 5, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_option_transmit_control = MeAttribute("SIP option transmit control", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_uri_format = MeAttribute("SIP URI format", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.redundant_sip_agent_pointer = MeAttribute("Redundant SIP agent pointer", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.proxy_server_address_pointer,
            self.outbound_proxy_address_pointer,
            self.primary_sip_dns,
            self.secondary_sip_dns,
            self.tcp_udp_pointer,
            self.sip_reg_exp_time,
            self.sip_rereg_head_start_time,
            self.host_part_uri,
            self.sip_status,
            self.sip_registrar,
            self.softswitch,
            self.sip_response_table,
            self.sip_option_transmit_control,
            self.sip_uri_format,
            self.redundant_sip_agent_pointer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.proxy_server_address_pointer.setPointer([157])
        self.outbound_proxy_address_pointer.setPointer([157])
        self.tcp_udp_pointer.setPointer([136])
        self.redundant_sip_agent_pointer.setPointer([150])


class SipUserData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 153, instance)
        self.name = "SipUserData"
        self.imp_link = []
        self.sip_agent_pointer = MeAttribute("SIP agent pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.user_part_aor = MeAttribute("User part AOR", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sip_display_name = MeAttribute("SIP display name", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.username_and_password = MeAttribute("Username and password", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voicemail_server_sip_uri = MeAttribute("Voicemail server SIP URI", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.voicemail_subscription_expiration_time = MeAttribute("Voicemail subscription expiration time", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.network_dial_plan_pointer = MeAttribute("Network dial plan pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.application_services_profile_pointer = MeAttribute("Application services profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.feature_code_pointer = MeAttribute("Feature code pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pptp_pointer = MeAttribute("PPTP pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.release_timer = MeAttribute("Release timer", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.roh_timer = MeAttribute("ROH timer", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.sip_agent_pointer,
            self.user_part_aor,
            self.sip_display_name,
            self.username_and_password,
            self.voicemail_server_sip_uri,
            self.voicemail_subscription_expiration_time,
            self.network_dial_plan_pointer,
            self.application_services_profile_pointer,
            self.feature_code_pointer,
            self.pptp_pointer,
            self.release_timer,
            self.roh_timer,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.sip_agent_pointer.setPointer([150])
        self.network_dial_plan_pointer.setPointer([145])
        self.application_services_profile_pointer.setPointer([146])
        self.feature_code_pointer.setPointer([147])
        self.pptp_pointer.setPointer([53])


class LargeString(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 157, instance)
        self.name = "LargeString"
        self.imp_link = []
        self.number_of_parts = MeAttribute("Number of parts", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.number_of_parts,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class OntRemoteDebug(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 158, instance)
        self.name = "OntRemoteDebug"
        self.imp_link = []
        self.command_format = MeAttribute("Command format", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.command = MeAttribute("Command", 25, False, True, MeAttribute.WRITE_PERMISSION, None)
        self.reply_table = MeAttribute("Reply table", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.command_format,
            self.command,
            self.reply_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EquipmentProtectionProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 159, instance)
        self.name = "EquipmentProtectionProfile"
        self.imp_link = []
        self.protect_slot_1_2 = MeAttribute("Protect slot 1 2", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.working_slot_1_2_3_4_5_6_7_8 = MeAttribute("working slot 1 2 3 4 5 6 7 8", 8, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.protect_status_1_2 = MeAttribute("Protect status 1 2", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.revertive_ind = MeAttribute("Revertive ind", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wait_to_restore_time = MeAttribute("Wait to restore time", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.protect_slot_1_2,
            self.working_slot_1_2_3_4_5_6_7_8,
            self.protect_status_1_2,
            self.revertive_ind,
            self.wait_to_restore_time,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EquipmentExtensionPackage(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 160, instance)
        self.name = "EquipmentExtensionPackage"
        self.imp_link = [256, 5]
        self.environmental_sense = MeAttribute("Environmental sense", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.contact_closure_output = MeAttribute("Contact closure output", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.environmental_sense,
            self.contact_closure_output,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class ExtendedVlanTaggingOperationConfigurationData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 171, instance)
        self.name = "ExtendedVlanTaggingOperationConfigurationData"
        self.imp_link = []
        self.association_type = MeAttribute("Association type", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.received_frame_vlan_tagging_operation_table_max_size = MeAttribute("Received frame VLAN tagging operation table max size", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.input_tpid = MeAttribute("Input TPID", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.output_tpid = MeAttribute("Output TPID", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.downstream_mode = MeAttribute("Downstream mode", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.received_frame_vlan_tagging_operation_table = MeAttribute("Received frame VLAN tagging operation table", 16, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.associated_me_pointer = MeAttribute("Associated ME pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dscp_to_p_bit_mapping = MeAttribute("DSCP to P-bit mapping", 24, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.association_type,
            self.received_frame_vlan_tagging_operation_table_max_size,
            self.input_tpid,
            self.output_tpid,
            self.downstream_mode,
            self.received_frame_vlan_tagging_operation_table,
            self.associated_me_pointer,
            self.dscp_to_p_bit_mapping,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
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
            self.associated_me_pointer.setPointer(None)


class PppoeByGcom(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 250, instance)
        self.name = "PppoeByGcom"
        self.imp_link = []
        self.nat = MeAttribute("NAT", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.auth = MeAttribute("Auth", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.connect = MeAttribute("Connect", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.release_time = MeAttribute("Release Time", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.username = MeAttribute("Username", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.password = MeAttribute("Password", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.attribute7 = MeAttribute("Attribute7", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.nat,
            self.auth,
            self.connect,
            self.release_time,
            self.username,
            self.password,
            self.attribute7,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.pointer_to_ip_host_config_data_me.setPointer([134, 347])
        self.pointer_to_larg_string_me_pointer_for_username.setPointer([157])
        self.pointer_to_larg_string_me_pointer_for_service_name.setPointer([157])


class EthernetPerformanceMonitoringHistoryData4(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 255, instance)
        self.name = "EthernetPerformanceMonitoringHistoryData4"
        self.imp_link = [11]
        self.interval_end_time = MeAttribute("interval_end_time", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_1_2_id = MeAttribute("threshold_data_1_2_id", 2, True, False, MeAttribute.READ_PERMISSION, None)
        self.association_type = MeAttribute("association_type", 1, True, False, MeAttribute.READ_PERMISSION, None)
        self.transmitted_traffic = MeAttribute("transmitted_traffic", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.received_traffic = MeAttribute("received_traffic", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.transmitted_rate = MeAttribute("transmitted_rate", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.received_rate = MeAttribute("received_rate", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.transmitted_octets = MeAttribute("transmitted_octets", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.received_octets = MeAttribute("received_octets", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.transmitted_discarded_counter = MeAttribute("transmitted_discarded_counter", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.received_discarded_counter = MeAttribute("received_discarded_counter", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.transmitted_error_counter = MeAttribute("transmitted_error_counter", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.received_error_counter = MeAttribute("received_error_counter", 4, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_1_2_id,
            self.association_type,
            self.transmitted_traffic,
            self.received_traffic,
            self.transmitted_rate,
            self.received_rate,
            self.transmitted_octets,
            self.received_octets,
            self.transmitted_discarded_counter,
            self.received_discarded_counter,
            self.transmitted_error_counter,
            self.received_error_counter,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Ont(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 256, instance)
        self.name = "Ont"
        self.imp_link = []
        self.vendor_id = MeAttribute("Vendor Id", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.version = MeAttribute("Version", 14, False, True, MeAttribute.READ_PERMISSION, None)
        self.serial_nr = MeAttribute("Serial Nr", 8, False, True, MeAttribute.READ_PERMISSION, None)
        self.traffic_management_option = MeAttribute("Traffic management option", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.vp_vc_cross_connection_function_option = MeAttribute("VP VC cross connection function option", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.battery_backup = MeAttribute("Battery backup", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.administrative_state = MeAttribute("Administrative State", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational State", 1, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.vendor_id,
            self.version,
            self.serial_nr,
            self.traffic_management_option,
            self.vp_vc_cross_connection_function_option,
            self.battery_backup,
            self.administrative_state,
            self.operational_state,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Ont2(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 257, instance)
        self.name = "Ont2"
        self.imp_link = []
        self.equipment_id = MeAttribute("Equipment id", 20, False, False, MeAttribute.READ_PERMISSION, None)
        self.omcc_version = MeAttribute("OMCC version", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.vendor_product_code = MeAttribute("Vendor product code", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.security_capability = MeAttribute("Security capability", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.security_mode = MeAttribute("Security mode", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.total_priority_queue_number = MeAttribute("Total priority queue number", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.total_traffic_scheduler_number = MeAttribute("Total traffic scheduler number", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.mode = MeAttribute("Mode", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.total_gem_port_id_number = MeAttribute("Total GEM port-ID number", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.sysup_time = MeAttribute("SysUp Time", 4, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.equipment_id,
            self.omcc_version,
            self.vendor_product_code,
            self.security_capability,
            self.security_mode,
            self.total_priority_queue_number,
            self.total_traffic_scheduler_number,
            self.mode,
            self.total_gem_port_id_number,
            self.sysup_time,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PonTcAdapter(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 261, instance)
        self.name = "PonTcAdapter"
        self.imp_link = []
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 4, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Tcont(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 262, instance)
        self.name = "Tcont"
        self.imp_link = []
        self.alloc_id = MeAttribute("Alloc-id", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.mode_indicator = MeAttribute("Mode indicator", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.policy = MeAttribute("Policy", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.alloc_id,
            self.mode_indicator,
            self.policy,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Anig(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 263, instance)
        self.name = "Anig"
        self.imp_link = []
        self.sr_indication = MeAttribute("SR indication", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.total_t_cont_number = MeAttribute("Total T-CONT number", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.gem_block_length = MeAttribute("GEM block length", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.piggyback_dba_reporting = MeAttribute("Piggyback DBA reporting", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.whole_ont_dba_reporting = MeAttribute("Whole ONT DBA reporting", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.sf_threshold = MeAttribute("SF threshold", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.sd_threshold = MeAttribute("SD threshold", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc = MeAttribute("ARC", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.arc_interval = MeAttribute("ARC interval", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.optical_signal_level = MeAttribute("Optical signal level", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.lower_optical_threshold = MeAttribute("Lower optical threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.upper_optical_threshold = MeAttribute("Upper optical threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ont_response_time = MeAttribute("ONT response time", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.transmit_optical_level = MeAttribute("Transmit optical level", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.lower_transmit_power_threshold = MeAttribute("Lower transmit power threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.upper_transmit_power_threshold = MeAttribute("Upper transmit power threshold", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.sr_indication,
            self.total_t_cont_number,
            self.gem_block_length,
            self.piggyback_dba_reporting,
            self.whole_ont_dba_reporting,
            self.sf_threshold,
            self.sd_threshold,
            self.arc,
            self.arc_interval,
            self.optical_signal_level,
            self.lower_optical_threshold,
            self.upper_optical_threshold,
            self.ont_response_time,
            self.transmit_optical_level,
            self.lower_transmit_power_threshold,
            self.upper_transmit_power_threshold,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Uni(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 264, instance)
        self.name = "Uni"
        self.imp_link = [11]
        self.config_option_status = MeAttribute("Config option status", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.administrative_state = MeAttribute("Administrative state", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.config_option_status,
            self.administrative_state,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GemInterworkingTerminationPoint(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 266, instance)
        self.name = "GemInterworkingTerminationPoint"
        self.imp_link = []
        self.gem_port_network_ctp_connectivity_pointer = MeAttribute("GEM port network CTP connectivity pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.interworking_option = MeAttribute("Interworking option", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.service_profile_pointer = MeAttribute("Service profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.interworking_termination_point_pointer = MeAttribute("Interworking termination point pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pptp_counter = MeAttribute("PPTP counter", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.operational_state = MeAttribute("Operational state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.gal_profile_pointer = MeAttribute("GAL profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.gal_loopback_configuration = MeAttribute("GAL loopback configuration", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.gem_port_network_ctp_connectivity_pointer,
            self.interworking_option,
            self.service_profile_pointer,
            self.interworking_termination_point_pointer,
            self.pptp_counter,
            self.operational_state,
            self.gal_profile_pointer,
            self.gal_loopback_configuration,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
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
        self.interworking_termination_point_pointer.setPointer([11, 268, 12])


class GemPortPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 267, instance)
        self.name = "GemPortPmHistoryData"
        self.imp_link = [268]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.lost_packets = MeAttribute("Lost packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.misinserted_packets = MeAttribute("Misinserted packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_packets = MeAttribute("Received packets", 5, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_blocks = MeAttribute("Received blocks", 5, False, True, MeAttribute.READ_PERMISSION, None)
        self.transmitted_blocks = MeAttribute("Transmitted blocks", 5, False, True, MeAttribute.READ_PERMISSION, None)
        self.impaired_blocks = MeAttribute("Impaired blocks", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.transmitted_packets = MeAttribute("Transmitted packets", 5, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.lost_packets,
            self.misinserted_packets,
            self.received_packets,
            self.received_blocks,
            self.transmitted_blocks,
            self.impaired_blocks,
            self.transmitted_packets,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GemPortNetworkCtp(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 268, instance)
        self.name = "GemPortNetworkCtp"
        self.imp_link = [267]
        self.port_id_value = MeAttribute("Port id value", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.t_cont_pointer = MeAttribute("T-CONT pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.direction = MeAttribute("Direction", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.traffic_management_pointer_for_upstream = MeAttribute("Traffic management pointer for upstream", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.traffic_descriptor_profile_pointer = MeAttribute("Traffic descriptor profile pointer", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.uni_counter = MeAttribute("UNI counter", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.priority_queue_pointer_for_downstream = MeAttribute("Priority queue pointer for downstream", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.encryption_state = MeAttribute("Encryption state", 1, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.port_id_value,
            self.t_cont_pointer,
            self.direction,
            self.traffic_management_pointer_for_upstream,
            self.traffic_descriptor_profile_pointer,
            self.uni_counter,
            self.priority_queue_pointer_for_downstream,
            self.encryption_state,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.t_cont_pointer.setPointer([262])
        self.traffic_management_pointer_for_upstream.setPointer([277, 262])
        self.traffic_descriptor_profile_pointer.setPointer([280])
        self.priority_queue_pointer_for_downstream.setPointer([277])


class GalTdmProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 271, instance)
        self.name = "GalTdmProfile"
        self.imp_link = []
        self.gem_frame_loss_integration_period = MeAttribute("GEM frame loss integration period", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.gem_frame_loss_integration_period,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GalEthernetProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 272, instance)
        self.name = "GalEthernetProfile"
        self.imp_link = []
        self.maximum_gem_payload_size = MeAttribute("Maximum GEM payload size", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.maximum_gem_payload_size,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class ThresholdData1(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 273, instance)
        self.name = "ThresholdData1"
        self.imp_link = [274]
        self.threshold_value_1 = MeAttribute("Threshold value 1", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_2 = MeAttribute("Threshold value 2", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_3 = MeAttribute("Threshold value 3", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_4 = MeAttribute("Threshold value 4", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_5 = MeAttribute("Threshold value 5", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_6 = MeAttribute("Threshold value 6", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_7 = MeAttribute("Threshold value 7", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.threshold_value_1,
            self.threshold_value_2,
            self.threshold_value_3,
            self.threshold_value_4,
            self.threshold_value_5,
            self.threshold_value_6,
            self.threshold_value_7,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class ThresholdData2(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 274, instance)
        self.name = "ThresholdData2"
        self.imp_link = [273]
        self.threshold_value_8 = MeAttribute("Threshold value 8", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_9 = MeAttribute("Threshold value 9", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_10 = MeAttribute("Threshold value 10", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_11 = MeAttribute("Threshold value 11", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_12 = MeAttribute("Threshold value 12", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_13 = MeAttribute("Threshold value 13", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_14 = MeAttribute("Threshold value 14", 4, True, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.threshold_value_8,
            self.threshold_value_9,
            self.threshold_value_10,
            self.threshold_value_11,
            self.threshold_value_12,
            self.threshold_value_13,
            self.threshold_value_14,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GalTdmPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 275, instance)
        self.name = "GalTdmPmHistoryData"
        self.imp_link = []
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.gem_frame_loss = MeAttribute("GEM frame loss", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.buffer_underflows = MeAttribute("Buffer underflows", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.buffer_overflows = MeAttribute("Buffer overflows", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.gem_frame_loss,
            self.buffer_underflows,
            self.buffer_overflows,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GalEthernetPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 276, instance)
        self.name = "GalEthernetPmHistoryData"
        self.imp_link = [266, 281]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.discarded_frames = MeAttribute("Discarded frames", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.discarded_frames,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PriorityQueue(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 277, instance)
        self.name = "PriorityQueue"
        self.imp_link = []
        self.queue_configuration_option = MeAttribute("Queue Configuration Option", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.maximum_queue_size = MeAttribute("Maximum Queue Size", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.allocated_queue_size = MeAttribute("Allocated Queue Size", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.discard_block_counter_reset_interval = MeAttribute("Discard-block Counter Reset Interval", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.threshold_value_for_discarded_blocks_due_to_buffer_overflow = MeAttribute("Threshold Value For Discarded Blocks Due To Buffer Overflow", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.related_port = MeAttribute("Related Port", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.traffic_scheduler_g_pointer = MeAttribute("Traffic Scheduler-G Pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.weight = MeAttribute("Weight", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.back_pressure_operation = MeAttribute("Back Pressure Operation", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.back_pressure_time = MeAttribute("Back Pressure Time", 4, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.back_pressure_occur_queue_threshold = MeAttribute("Back Pressure Occur Queue Threshold", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.back_pressure_clear_queue_threshold = MeAttribute("Back Pressure Clear Queue Threshold", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.queue_configuration_option,
            self.maximum_queue_size,
            self.allocated_queue_size,
            self.discard_block_counter_reset_interval,
            self.threshold_value_for_discarded_blocks_due_to_buffer_overflow,
            self.related_port,
            self.traffic_scheduler_g_pointer,
            self.weight,
            self.back_pressure_operation,
            self.back_pressure_time,
            self.back_pressure_occur_queue_threshold,
            self.back_pressure_clear_queue_threshold,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.traffic_scheduler_g_pointer.setPointer([278])


class TrafficScheduler(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 278, instance)
        self.name = "TrafficScheduler"
        self.imp_link = []
        self.tcont_pointer = MeAttribute("TCONT pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.traffic_shed_pointer = MeAttribute("traffic shed pointer", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.policy = MeAttribute("policy", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.priority_weight = MeAttribute("priority weight", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.tcont_pointer,
            self.traffic_shed_pointer,
            self.policy,
            self.priority_weight,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.tcont_pointer.setPointer([262])
        self.traffic_shed_pointer.setPointer([278])


class ProtectionData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 279, instance)
        self.name = "ProtectionData"
        self.imp_link = []
        self.working_ani_g_pointer = MeAttribute("Working ANI-G pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.protection_ani_g_pointer = MeAttribute("Protection ANI-G pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.protection_type = MeAttribute("Protection type", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.revertive_ind = MeAttribute("Revertive ind", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wait_to_restore_time = MeAttribute("Wait to restore time", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.switching_guard_time = MeAttribute("Switching guard time", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.working_ani_g_pointer,
            self.protection_ani_g_pointer,
            self.protection_type,
            self.revertive_ind,
            self.wait_to_restore_time,
            self.switching_guard_time,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.working_ani_g_pointer.setPointer([263, 313, 315])
        self.protection_ani_g_pointer.setPointer([263, 313, 315])


class MulticastGemInterworkingTerminationPoint(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 281, instance)
        self.name = "MulticastGemInterworkingTerminationPoint"
        self.imp_link = []
        self.gem_port_network_ctp_connectivity_pointer = MeAttribute("GEM port network CTP connectivity pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.interworking_option = MeAttribute("Interworking option", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.service_profile_pointer = MeAttribute("Service profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.interworking_termination_point_pointer = MeAttribute("Interworking termination point pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.pptp_counter = MeAttribute("PPTP counter", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.operational_state = MeAttribute("Operational state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.gal_profile_pointer = MeAttribute("GAL profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.gal_loopback_configuration = MeAttribute("GAL loopback configuration", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.multicast_address_table = MeAttribute("Multicast address table", 12, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.gem_port_network_ctp_connectivity_pointer,
            self.interworking_option,
            self.service_profile_pointer,
            self.interworking_termination_point_pointer,
            self.pptp_counter,
            self.operational_state,
            self.gal_profile_pointer,
            self.gal_loopback_configuration,
            self.multicast_address_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
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
        self.interworking_termination_point_pointer.setPointer([11, 268, 12])


class Omci(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 287, instance)
        self.name = "Omci"
        self.imp_link = []
        self.me_type_table = MeAttribute("ME Type Table", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.message_type_table = MeAttribute("Message Type Table", 2, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.me_type_table,
            self.message_type_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Dot1XPortExtensionPackage(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 290, instance)
        self.name = "Dot1XPortExtensionPackage"
        self.imp_link = []
        self.dot1x_enable = MeAttribute("Dot1x Enable", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.action_register = MeAttribute("Action Register", 1, False, True, MeAttribute.WRITE_PERMISSION, None)
        self.authenticator_pae_state = MeAttribute("Authenticator PAE State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.backend_authentication_state = MeAttribute("Backend Authentication State", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.admin_controlled_directions = MeAttribute("Admin Controlled Directions", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_controlled_directions = MeAttribute("Operational Controlled Directions", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.authenticator_controlled_port_status = MeAttribute("Authenticator Controlled Port Status", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.quiet_period = MeAttribute("Quiet Period", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.server_timeout_period = MeAttribute("Server Timeout Period", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.reauthentication_period = MeAttribute("Reauthentication Period", 2, False, False, MeAttribute.READ_PERMISSION, None)
        self.reauthentication_enabled = MeAttribute("Reauthentication Enabled", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.key_transmission_enabled = MeAttribute("Key transmission Enabled", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.dot1x_enable,
            self.action_register,
            self.authenticator_pae_state,
            self.backend_authentication_state,
            self.admin_controlled_directions,
            self.operational_controlled_directions,
            self.authenticator_controlled_port_status,
            self.quiet_period,
            self.server_timeout_period,
            self.reauthentication_period,
            self.reauthentication_enabled,
            self.key_transmission_enabled,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Dot1XConfigurationProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 291, instance)
        self.name = "Dot1XConfigurationProfile"
        self.imp_link = []
        self.circuit_id_prefix = MeAttribute("Circuit ID prefix", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.fallback_policy = MeAttribute("Fallback policy", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.auth_server_1 = MeAttribute("Auth server 1", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.shared_secret_auth1 = MeAttribute("Shared secret auth1", 25, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.auth_server_2 = MeAttribute("Auth server 2", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.shared_secret_auth2 = MeAttribute("Shared secret auth2", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.auth_server_3 = MeAttribute("Auth server 3", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.shared_secret_auth3 = MeAttribute("Shared secret auth3", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.olt_proxy_address = MeAttribute("OLT proxy address", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.circuit_id_prefix,
            self.fallback_policy,
            self.auth_server_1,
            self.shared_secret_auth1,
            self.auth_server_2,
            self.shared_secret_auth2,
            self.auth_server_3,
            self.shared_secret_auth3,
            self.olt_proxy_address,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EthernetPmHistoryData3(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 296, instance)
        self.name = "EthernetPmHistoryData3"
        self.imp_link = [11]
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.drop_events = MeAttribute("Drop events", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.octets = MeAttribute("Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets = MeAttribute("Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.fragments = MeAttribute("Fragments", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.jabbers = MeAttribute("Jabbers", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.drop_events,
            self.octets,
            self.packets,
            self.broadcast_packets,
            self.multicast_packets,
            self.undersize_packets,
            self.fragments,
            self.jabbers,
            self.packets_64_octets,
            self.packets_65_to_127_octets,
            self.packets_128_to_255_octets,
            self.packets_256_to_511_octets,
            self.packets_512_to_1023_octets,
            self.packets_1024_to_1518_octets,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PortMappingPackage(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 297, instance)
        self.name = "PortMappingPackage"
        self.imp_link = []
        self.max_ports = MeAttribute("Max ports", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.port_list_1 = MeAttribute("Port list 1", 16, False, True, MeAttribute.READ_PERMISSION, None)
        self.port_list_2 = MeAttribute("Port list 2", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_3 = MeAttribute("Port list 3", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_4 = MeAttribute("Port list 4", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_5 = MeAttribute("Port list 5", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_6 = MeAttribute("Port list 6", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_7 = MeAttribute("Port list 7", 16, False, False, MeAttribute.READ_PERMISSION, None)
        self.port_list_8 = MeAttribute("Port list 8", 16, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.max_ports,
            self.port_list_1,
            self.port_list_2,
            self.port_list_3,
            self.port_list_4,
            self.port_list_5,
            self.port_list_6,
            self.port_list_7,
            self.port_list_8,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MulticastOperationsProfile(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 309, instance)
        self.name = "MulticastOperationsProfile"
        self.imp_link = []
        self.igmp_version = MeAttribute("IGMP version", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.igmp_function = MeAttribute("IGMP function", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.immediate_leave = MeAttribute("Immediate leave", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.upstream_igmp_tci = MeAttribute("Upstream IGMP TCI", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.upstream_igmp_tag_control = MeAttribute("Upstream IGMP tag control", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.upstream_igmp_rate = MeAttribute("Upstream IGMP rate", 4, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dynamic_access_control_list_table = MeAttribute("Dynamic access control list table", 24, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.static_access_control_list_table = MeAttribute("Static access control list table", 24, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.lost_groups_list_table = MeAttribute("Lost groups list table", 10, False, False, MeAttribute.READ_PERMISSION, None)
        self.robustness = MeAttribute("Robustness", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.querier_ip_address = MeAttribute("Querier IP address", 4, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.query_interval = MeAttribute("Query interval", 4, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.query_max_response_time = MeAttribute("Query max response time", 4, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.last_member_query_interval = MeAttribute("Last member query interval", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.igmp_version,
            self.igmp_function,
            self.immediate_leave,
            self.upstream_igmp_tci,
            self.upstream_igmp_tag_control,
            self.upstream_igmp_rate,
            self.dynamic_access_control_list_table,
            self.static_access_control_list_table,
            self.lost_groups_list_table,
            self.robustness,
            self.querier_ip_address,
            self.query_interval,
            self.query_max_response_time,
            self.last_member_query_interval,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class MulticastSubscriberConfigInfo(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 310, instance)
        self.name = "MulticastSubscriberConfigInfo"
        self.imp_link = [47, 130]
        self.me_type = MeAttribute("ME type", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.multicast_operations_profile_pointer = MeAttribute("Multicast operations profile pointer", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.max_simultaneous_groups = MeAttribute("Max simultaneous groups", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.max_multicast_bandwidth = MeAttribute("Max multicast bandwidth", 4, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.bandwidth_enforcement = MeAttribute("Bandwidth enforcement", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.me_type,
            self.multicast_operations_profile_pointer,
            self.max_simultaneous_groups,
            self.max_multicast_bandwidth,
            self.bandwidth_enforcement,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.multicast_operations_profile_pointer.setPointer([309])


class MulticastSubscriberMonitor(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 311, instance)
        self.name = "MulticastSubscriberMonitor"
        self.imp_link = [47, 130]
        self.me_type = MeAttribute("ME type", 1, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.current_multicast_bandwidth = MeAttribute("Current multicast bandwidth", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.max_join_messages_counter = MeAttribute("Max Join messages counter", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.bandwidth_exceeded_counter = MeAttribute("Bandwidth exceeded counter", 4, False, False, MeAttribute.READ_PERMISSION, None)
        self.active_group_list_table = MeAttribute("Active group list table", 24, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.me_type,
            self.current_multicast_bandwidth,
            self.max_join_messages_counter,
            self.bandwidth_exceeded_counter,
            self.active_group_list_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class FecPmHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 312, instance)
        self.name = "FecPmHistoryData"
        self.imp_link = [263]
        self.interval_end_time = MeAttribute("Interval end time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.corrected_bytes = MeAttribute("Corrected bytes", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.corrected_code_words = MeAttribute("Corrected code words", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.uncorrectable_code_words = MeAttribute("Uncorrectable code words", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.total_code_words = MeAttribute("Total code words", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.fec_seconds = MeAttribute("FEC seconds", 2, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.corrected_bytes,
            self.corrected_code_words,
            self.uncorrectable_code_words,
            self.total_code_words,
            self.fec_seconds,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class FileTransferController(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 318, instance)
        self.name = "FileTransferController"
        self.imp_link = []
        self.supported_transfer_protocols = MeAttribute("Supported transfer protocols", 2, False, True, MeAttribute.READ_PERMISSION, None)
        self.file_type = MeAttribute("File type", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.file_instance = MeAttribute("File instance", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.local_file_name_pointer = MeAttribute("Local file name pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.network_address_pointer = MeAttribute("Network address pointer", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.file_transfer_trigger = MeAttribute("File transfer trigger", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.file_transfer_status = MeAttribute("File transfer status", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.gem_iwtp_pointer = MeAttribute("GEM IWTP pointer", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.undersize_packets = MeAttribute("Undersize Packets", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.vlan = MeAttribute("VLAN", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.file_size = MeAttribute("File size", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.directory_listing_table = MeAttribute("Directory listing table", 25, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.supported_transfer_protocols,
            self.file_type,
            self.file_instance,
            self.local_file_name_pointer,
            self.network_address_pointer,
            self.file_transfer_trigger,
            self.file_transfer_status,
            self.gem_iwtp_pointer,
            self.undersize_packets,
            self.vlan,
            self.file_size,
            self.directory_listing_table,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.local_file_name_pointer.setPointer([157])
        self.network_address_pointer.setPointer([137])
        self.gem_iwtp_pointer.setPointer([266])


class EthernetFramePmHistoryDataDs(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 321, instance)
        self.name = "EthernetFramePmHistoryDataDs"
        self.imp_link = []
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.drop_events = MeAttribute("Drop events", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.octets = MeAttribute("Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets = MeAttribute("Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.crc_errored_packets = MeAttribute("CRC Errored Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.oversize_packets = MeAttribute("Oversize Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.drop_events,
            self.octets,
            self.packets,
            self.broadcast_packets,
            self.multicast_packets,
            self.crc_errored_packets,
            self.undersize_packets,
            self.oversize_packets,
            self.packets_64_octets,
            self.packets_65_to_127_octets,
            self.packets_128_to_255_octets,
            self.packets_256_to_511_octets,
            self.packets_512_to_1023_octets,
            self.packets_1024_to_1518_octets,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class EthernetFramePmHistoryDataUs(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 322, instance)
        self.name = "EthernetFramePmHistoryDataUs"
        self.imp_link = [47]
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.drop_events = MeAttribute("Drop events", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.octets = MeAttribute("Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets = MeAttribute("Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.crc_errored_packets = MeAttribute("CRC Errored Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.oversize_packets = MeAttribute("Oversize Packets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.drop_events,
            self.octets,
            self.packets,
            self.broadcast_packets,
            self.multicast_packets,
            self.crc_errored_packets,
            self.undersize_packets,
            self.oversize_packets,
            self.packets_64_octets,
            self.packets_65_to_127_octets,
            self.packets_128_to_255_octets,
            self.packets_256_to_511_octets,
            self.packets_512_to_1023_octets,
            self.packets_1024_to_1518_octets,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class VirtualEthernetInterfacePoint(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 329, instance)
        self.name = "VirtualEthernetInterfacePoint"
        self.imp_link = []
        self.administrative_state = MeAttribute("Administrative state", 14, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.operational_state = MeAttribute("Operational state", 1, False, False, MeAttribute.READ_PERMISSION, None)
        self.interdomain_name = MeAttribute("Interdomain name", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tcp_udp_pointer = MeAttribute("TCP UDP pointer", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.iana_assigned_port = MeAttribute("IANA assigned port", 2, False, True, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.administrative_state,
            self.operational_state,
            self.interdomain_name,
            self.tcp_udp_pointer,
            self.iana_assigned_port,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        self.multicast_operations_profile_pointer.setPointer([136])


class BbfTr(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 340, instance)
        self.name = "BbfTr"
        self.imp_link = []
        self.administrative_state = MeAttribute("Administrative state", 1, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.acs_network_address = MeAttribute("ACS network address", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.associated_tag = MeAttribute("Associated tag", 2, False, True, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.administrative_state,
            self.acs_network_address,
            self.associated_tag,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class GemPortNetworkCtpPerformanceMonitoringHistoryData(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 341, instance)
        self.name = "GemPortNetworkCtpPerformanceMonitoringHistoryData"
        self.imp_link = [268]
        self.interval_end_time = MeAttribute("Interval end time", 1, True, True, MeAttribute.READ_PERMISSION, None)
        self.threshold_data_id = MeAttribute("Threshold data ID", 2, True, True, MeAttribute.READ_WRITE_PERMISSION, None)
        self.transmitted_gem_frames = MeAttribute("Transmitted GEM frames", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_gem_frames = MeAttribute("Received GEM frames", 4, False, True, MeAttribute.READ_PERMISSION, None)
        self.received_payload_bytes = MeAttribute("Received payload bytes", 8, False, True, MeAttribute.READ_PERMISSION, None)
        self.transmitted_payload_bytes = MeAttribute("Transmitted payload bytes", 8, False, True, MeAttribute.READ_PERMISSION, None)
        self.encryption_key_errors = MeAttribute("Encryption key errors", 4, False, False, MeAttribute.READ_PERMISSION, None)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.transmitted_gem_frames,
            self.received_gem_frames,
            self.received_payload_bytes,
            self.transmitted_payload_bytes,
            self.encryption_key_errors,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class PppoeIntelbrasOlt8820I110Gi(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65303, instance)
        self.name = "PppoeIntelbrasOlt8820I110Gi"
        self.imp_link = []
        self.wan_type = MeAttribute("Wan-Type", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.user = MeAttribute("User", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.password = MeAttribute("Password", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.mppe = MeAttribute("MPPE", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.service_name = MeAttribute("Service Name", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.wan_type,
            self.user,
            self.password,
            self.mppe,
            self.service_name,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanExtendedConfigFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65320, instance)
        self.name = "WanExtendedConfigFh"
        self.imp_link = []
        self.wan_number = MeAttribute("WAN Number", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_index = MeAttribute("WAN Index", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_1 = MeAttribute("WAN name 1", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_2_dns = MeAttribute("WAN name 2 DNS", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_3_dns = MeAttribute("WAN name 3 DNS", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_4 = MeAttribute("WAN name 4", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_uppir = MeAttribute("WAN UPPIR", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_downpir = MeAttribute("WAN DOWNPIR", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.wan_number,
            self.wan_index,
            self.wan_name_1,
            self.wan_name_2_dns,
            self.wan_name_3_dns,
            self.wan_name_4,
            self.wan_uppir,
            self.wan_downpir,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanProfileFileFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65321, instance)
        self.name = "WanProfileFileFh"
        self.imp_link = []
        self.create_or_delete_wan_ipv4 = MeAttribute("Create-or-Delete WAN IPV4", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.create_or_delete_wan_ipv6 = MeAttribute("Create-or-Delete WAN IPV6", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.create_or_delete_wan_ipv4,
            self.create_or_delete_wan_ipv6,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanModeFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65322, instance)
        self.name = "WanModeFh"
        self.imp_link = []
        self.wan_index = MeAttribute("WAN INDEX", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_1 = MeAttribute("WAN name 1", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_2 = MeAttribute("WAN name 2", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_3 = MeAttribute("WAN name 3", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_name_4 = MeAttribute("WAN name 4", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_conected_mode = MeAttribute("WAN Conected Mode", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_conected_type = MeAttribute("WAN Conected Type", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.vlan = MeAttribute("VLAN", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.cos = MeAttribute("COS", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.nat = MeAttribute("NAT", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ip_mode = MeAttribute("IP MODE", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.qos_enable = MeAttribute("QoS Enable", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.conect_status = MeAttribute("Conect Status", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.gem_port_point = MeAttribute("GEM PORT POINT", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dhcp_remote_id = MeAttribute("DHCP REMOTE ID", 10, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.active_flag = MeAttribute("ACTIVE FLAG", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.wan_index,
            self.wan_name_1,
            self.wan_name_2,
            self.wan_name_3,
            self.wan_name_4,
            self.wan_conected_mode,
            self.wan_conected_type,
            self.vlan,
            self.cos,
            self.nat,
            self.ip_mode,
            self.qos_enable,
            self.conect_status,
            self.gem_port_point,
            self.dhcp_remote_id,
            self.active_flag,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanConfigFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65323, instance)
        self.name = "WanConfigFh"
        self.imp_link = []
        self.proxy_enable = MeAttribute("Proxy Enable", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.userppoe1 = MeAttribute("Userppoe1", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.userppoe2 = MeAttribute("Userppoe2", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.passwordppoe1 = MeAttribute("Passwordppoe1", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.passwordppoe2 = MeAttribute("Passwordppoe2", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.service_name_1 = MeAttribute("Service Name 1", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.service_name_2 = MeAttribute("Service Name 2", 16, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.dail_parther = MeAttribute("Dail Parther", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.authentic_mode = MeAttribute("Authentic Mode", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.auto_drop_time = MeAttribute("Auto Drop Time", 2, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.proxy_enable,
            self.userppoe1,
            self.userppoe2,
            self.passwordppoe1,
            self.passwordppoe2,
            self.service_name_1,
            self.service_name_2,
            self.dail_parther,
            self.authentic_mode,
            self.auto_drop_time,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanPortBindFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65324, instance)
        self.name = "WanPortBindFh"
        self.imp_link = []
        self.lan_bind = MeAttribute("LAN Bind", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ssid_bind = MeAttribute("SSID Bind", 1, True, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.lan_bind,
            self.ssid_bind,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanWanProfileFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65329, instance)
        self.name = "WanWanProfileFh"
        self.imp_link = []
        self.wan_ip_host_ip_addr = MeAttribute("WAN IP HOST IP ADDR", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_mask = MeAttribute("WAN IP HOST MASK", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_gateway = MeAttribute("WAN IP HOST Gateway", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_primary_dns = MeAttribute("WAN IP HOST Primary DNS", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_secondary_dns = MeAttribute("WAN IP HOST Secondary DNS", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_static_ipv6 = MeAttribute("WAN IP HOST Static IPv6", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_ipv6_gateway = MeAttribute("WAN IP HOST IPv6 Gateway", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_ipv6_primary_dns_static_ipv6 = MeAttribute("WAN IP HOST IPV6 Primary DNS Static IPv6", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_ipv6_secondary_dns_static_ipv6 = MeAttribute("WAN IP HOST IPV6 Secondary DNS Static IPv6", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_wan_protocol = MeAttribute("WAN IP HOST WAN Protocol", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_static_prefix = MeAttribute("WAN IP HOST Static Prefix", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_prefix_pool = MeAttribute("WAN IP HOST Prefix Pool", 19, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_address_source = MeAttribute("WAN IP HOST Address Source", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wan_ip_host_mac_address_source = MeAttribute("WAN IP HOST MAC Address Source", 6, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.wan_ip_host_ip_addr,
            self.wan_ip_host_mask,
            self.wan_ip_host_gateway,
            self.wan_ip_host_primary_dns,
            self.wan_ip_host_secondary_dns,
            self.wan_ip_host_static_ipv6,
            self.wan_ip_host_ipv6_gateway,
            self.wan_ip_host_ipv6_primary_dns_static_ipv6,
            self.wan_ip_host_ipv6_secondary_dns_static_ipv6,
            self.wan_ip_host_wan_protocol,
            self.wan_ip_host_static_prefix,
            self.wan_ip_host_prefix_pool,
            self.wan_ip_host_address_source,
            self.wan_ip_host_mac_address_source,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WifiGeneralConfig(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65326, instance)
        self.name = "WifiGeneralConfig"
        self.imp_link = []
        self.wifi_std = MeAttribute("wifi_std", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_auth = MeAttribute("wifi_auth", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_cryp = MeAttribute("wifi_cryp", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_pass = MeAttribute("wifi_pass", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_ssid = MeAttribute("wifi_ssid", 25, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_enabled = MeAttribute("wifi_enabled", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.wifi_std,
            self.wifi_auth,
            self.wifi_cryp,
            self.not_identified,
            self.not_identified,
            self.wifi_pass,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.wifi_ssid,
            self.not_identified,
            self.wifi_enabled,
            self.not_identified,
            self.not_identified,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WifiAdvanceConfig(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65327, instance)
        self.name = "WifiAdvanceConfig"
        self.imp_link = []
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_channel = MeAttribute("wifi_channel", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_tx_pwr = MeAttribute("wifi_tx_pwr", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_country = MeAttribute("wifi_country", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.wifi_freq_bandwidth = MeAttribute("wifi_freq_bandwidth", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.wifi_channel,
            self.wifi_tx_pwr,
            self.wifi_country,
            self.not_identified,
            self.wifi_freq_bandwidth,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class WanExtendedVlanFh(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65338, instance)
        self.name = "WanExtendedVlanFh"
        self.imp_link = []
        self.vlan_mode = MeAttribute("VLAN Mode", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tranlation_enable = MeAttribute("Tranlation Enable", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.tranlation__vid = MeAttribute("Tranlation  VID", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.vlan_cos = MeAttribute("VLAN CoS", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.qinq_enable = MeAttribute("QinQ Enable", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.vlan_tpid = MeAttribute("VLAN TPID", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.slan_id = MeAttribute("SLAN ID", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.slan_cos = MeAttribute("SLAN CoS", 2, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.vlan_mode,
            self.tranlation_enable,
            self.tranlation__vid,
            self.vlan_cos,
            self.qinq_enable,
            self.vlan_tpid,
            self.slan_id,
            self.slan_cos,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class OnuCapability(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65529, instance)
        self.name = "OnuCapability"
        self.imp_link = []
        self.operator_id = MeAttribute("operator_id", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.ctc_spec_version = MeAttribute("ctc_spec_version", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.onu_type = MeAttribute("onu_type", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.onu_tx_power_supply_control = MeAttribute("onu_tx_power_supply_control", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.operator_id,
            self.ctc_spec_version,
            self.onu_type,
            self.onu_tx_power_supply_control,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class LoidAuthentication(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 65530, instance)
        self.name = "LoidAuthentication"
        self.imp_link = []
        self.operator_id = MeAttribute("operator_id", 4, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.loid = MeAttribute("loid", 24, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.password = MeAttribute("password", 12, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.authentication_status = MeAttribute("authentication_status", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.operator_id,
            self.loid,
            self.password,
            self.authentication_status,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass


class Default(ManagedEntity):
    def __init__(self, instance):
        ManagedEntity.__init__(self, 999999, instance)
        self.name = "Default"
        self.imp_link = []
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)
        self.not_identified = MeAttribute("Not_identified", 1, False, False, MeAttribute.READ_WRITE_PERMISSION, None)

        self.attributes = (
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
        )

    def getImplicitlyLinked(self):
        return self.imp_link

    def setPointers(self):
        pass

class MeTranslate:
    @staticmethod
    def getInstance(me, inst):
        if me == 0:
            return None
        elif me == 2:
            return OntData(inst)
        elif me == 4:
            return PonIfLineCard(inst)
        elif me == 5:
            return Cardholder(inst)
        elif me == 6:
            return CircuitPack(inst)
        elif me == 7:
            return SoftwareImage(inst)
        elif me == 11:
            return PptpEthernetUni(inst)
        elif me == 24:
            return EthernetPmHistoryData(inst)
        elif me == 40:
            return PonPhysicalPathTerminationPoint(inst)
        elif me == 44:
            return VendorSpecific(inst)
        elif me == 45:
            return MacBridgeServiceProfile(inst)
        elif me == 47:
            return MacBridgePortConfigurationData(inst)
        elif me == 48:
            return MacBridgePortDesignationData(inst)
        elif me == 49:
            return MacBridgePortFilterTableData(inst)
        elif me == 51:
            return MacBridgePmHistoryData(inst)
        elif me == 52:
            return MacBridgePortPmHistoryData(inst)
        elif me == 53:
            return PhysicalPathTerminationPointPotsUni(inst)
        elif me == 58:
            return VoiceServiceProfile(inst)
        elif me == 79:
            return MacBridgePortFilterPreassignTable(inst)
        elif me == 82:
            return PptpVideoUni(inst)
        elif me == 84:
            return VlanTaggingFilterData(inst)
        elif me == 89:
            return EthernetPmHistoryData2(inst)
        elif me == 90:
            return PptpVideoAni(inst)
        elif me == 130:
            return Ieee8021PMapperServiceProfile(inst)
        elif me == 131:
            return Olt(inst)
        elif me == 133:
            return OntPowerShedding(inst)
        elif me == 134:
            return IpHostConfigData(inst)
        elif me == 136:
            return TcpUdpConfigData(inst)
        elif me == 137:
            return NetworkAddress(inst)
        elif me == 138:
            return VoipConfigData(inst)
        elif me == 139:
            return VoipVoiceCtp(inst)
        elif me == 141:
            return VoipLineStatus(inst)
        elif me == 142:
            return VoipMediaProfile(inst)
        elif me == 143:
            return RtpProfileData(inst)
        elif me == 148:
            return AuthenticationSecurityMethod(inst)
        elif me == 150:
            return SipAgentConfigData(inst)
        elif me == 153:
            return SipUserData(inst)
        elif me == 157:
            return LargeString(inst)
        elif me == 158:
            return OntRemoteDebug(inst)
        elif me == 159:
            return EquipmentProtectionProfile(inst)
        elif me == 160:
            return EquipmentExtensionPackage(inst)
        elif me == 171:
            return ExtendedVlanTaggingOperationConfigurationData(inst)
        elif me == 250:
            return PppoeByGcom(inst)
        elif me == 255:
            return EthernetPerformanceMonitoringHistoryData4(inst)
        elif me == 256:
            return Ont(inst)
        elif me == 257:
            return Ont2(inst)
        elif me == 261:
            return PonTcAdapter(inst)
        elif me == 262:
            return Tcont(inst)
        elif me == 263:
            return Anig(inst)
        elif me == 264:
            return Uni(inst)
        elif me == 266:
            return GemInterworkingTerminationPoint(inst)
        elif me == 267:
            return GemPortPmHistoryData(inst)
        elif me == 268:
            return GemPortNetworkCtp(inst)
        elif me == 271:
            return GalTdmProfile(inst)
        elif me == 272:
            return GalEthernetProfile(inst)
        elif me == 273:
            return ThresholdData1(inst)
        elif me == 274:
            return ThresholdData2(inst)
        elif me == 275:
            return GalTdmPmHistoryData(inst)
        elif me == 276:
            return GalEthernetPmHistoryData(inst)
        elif me == 277:
            return PriorityQueue(inst)
        elif me == 278:
            return TrafficScheduler(inst)
        elif me == 279:
            return ProtectionData(inst)
        elif me == 281:
            return MulticastGemInterworkingTerminationPoint(inst)
        elif me == 287:
            return Omci(inst)
        elif me == 290:
            return Dot1XPortExtensionPackage(inst)
        elif me == 291:
            return Dot1XConfigurationProfile(inst)
        elif me == 296:
            return EthernetPmHistoryData3(inst)
        elif me == 297:
            return PortMappingPackage(inst)
        elif me == 309:
            return MulticastOperationsProfile(inst)
        elif me == 310:
            return MulticastSubscriberConfigInfo(inst)
        elif me == 311:
            return MulticastSubscriberMonitor(inst)
        elif me == 312:
            return FecPmHistoryData(inst)
        elif me == 318:
            return FileTransferController(inst)
        elif me == 321:
            return EthernetFramePmHistoryDataDs(inst)
        elif me == 322:
            return EthernetFramePmHistoryDataUs(inst)
        elif me == 329:
            return VirtualEthernetInterfacePoint(inst)
        elif me == 340:
            return BbfTr(inst)
        elif me == 341:
            return GemPortNetworkCtpPerformanceMonitoringHistoryData(inst)
        elif me == 65303:
            return PppoeIntelbrasOlt8820I110Gi(inst)
        elif me == 65320:
            return WanExtendedConfigFh(inst)
        elif me == 65321:
            return WanProfileFileFh(inst)
        elif me == 65322:
            return WanModeFh(inst)
        elif me == 65323:
            return WanConfigFh(inst)
        elif me == 65324:
            return WanPortBindFh(inst)
        elif me == 65329:
            return WanWanProfileFh(inst)
        elif me == 65326:
            return WifiGeneralConfig(inst)
        elif me == 65327:
            return WifiAdvanceConfig(inst)
        elif me == 65338:
            return WanExtendedVlanFh(inst)
        elif me == 65529:
            return OnuCapability(inst)
        elif me == 65530:
            return LoidAuthentication(inst)
        elif me == 999999:
            return Default(inst)
        else:
            return None
