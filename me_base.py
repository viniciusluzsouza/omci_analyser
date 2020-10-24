
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


##################################################
############## ME Class Definitions ##############
##################################################

class OntData:
    def __init__(self):
        self.mib_data_sync = MeAttribute("MIB Data Sync", 1, False, False)

        self.attributes = (
            self.mib_data_sync,
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
    

class PonIfLineCard:
    def __init__(self):
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)

        self.attributes = (
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
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
    

class Cardholder:
    def __init__(self):
        self.actual_plug_in_unit_type = MeAttribute("Actual Plug-in Unit Type", 1, False, False)
        self.expected_plug_in_unit_type = MeAttribute("Expected Plug-in Unit Type", 1, False, False)
        self.expected_port_count = MeAttribute("Expected Port Count", 1, False, False)
        self.expected_equipment_id = MeAttribute("Expected Equipment Id", 20, False, False)
        self.actual_equipment_id = MeAttribute("Actual Equipment Id", 20, False, False)
        self.protection_profile_pointer = MeAttribute("Protection Profile Pointer", 1, False, False)
        self.invoke_protection_switch = MeAttribute("Invoke Protection Switch", 1, False, False)

        self.attributes = (
            self.actual_plug_in_unit_type,
            self.expected_plug_in_unit_type,
            self.expected_port_count,
            self.expected_equipment_id,
            self.actual_equipment_id,
            self.protection_profile_pointer,
            self.invoke_protection_switch,
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
    

class CircuitPack:
    def __init__(self):
        self.type = MeAttribute("Type", 1, False, False)
        self.number_of_ports = MeAttribute("Number of ports", 1, False, False)
        self.serial_number = MeAttribute("Serial Number", 8, False, False)
        self.version = MeAttribute("Version", 14, False, False)
        self.vendor_id = MeAttribute("Vendor Id", 4, False, False)
        self.administrative_state = MeAttribute("Administrative State", 1, False, False)
        self.operational_state = MeAttribute("Operational State", 1, False, False)
        self.bridged_or_ip_ind = MeAttribute("Bridged or IP Ind", 1, False, False)
        self.equipment_id = MeAttribute("Equipment Id", 20, False, False)
        self.card_configuration = MeAttribute("Card Configuration", 1, False, False)
        self.total_t_cont_buffer_number = MeAttribute("Total T-CONT Buffer Number", 1, False, False)
        self.total_priority_queue_number = MeAttribute("Total Priority Queue Number", 1, False, False)
        self.total_traffic_scheduler_number = MeAttribute("Total Traffic Scheduler Number", 1, False, False)
        self.power_shed_override = MeAttribute("Power Shed Override", 4, False, False)

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
    

class SoftwareImage:
    def __init__(self):
        self.version = MeAttribute("Version", 14, False, False)
        self.is_committed = MeAttribute("Is committed", 1, False, False)
        self.is_active = MeAttribute("Is active", 1, False, False)
        self.is_valid = MeAttribute("Is valid", 1, False, False)

        self.attributes = (
            self.version,
            self.is_committed,
            self.is_active,
            self.is_valid,
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
    

class PptpEthernetUni:
    def __init__(self):
        self.expected_type = MeAttribute("Expected Type", 1, False, False)
        self.sensed_type = MeAttribute("Sensed Type", 1, False, False)
        self.auto_detection_configuration = MeAttribute("Auto Detection Configuration", 1, False, False)
        self.ethernet_loopback_configuration = MeAttribute("Ethernet Loopback Configuration", 1, False, False)
        self.administrative_state = MeAttribute("Administrative State", 1, False, False)
        self.operational_state = MeAttribute("Operational State", 1, False, False)
        self.configuration_ind = MeAttribute("Configuration Ind", 1, False, False)
        self.max_frame_size = MeAttribute("Max Frame Size", 2, False, False)
        self.dte_or_dce = MeAttribute("DTE or DCE", 1, False, False)
        self.pause_time = MeAttribute("Pause Time", 2, False, False)
        self.bridged_or_ip_ind = MeAttribute("Bridged or IP Ind", 1, False, False)
        self.arc = MeAttribute("ARC", 1, False, False)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False)
        self.pppoe_filter = MeAttribute("PPPoE Filter", 1, False, False)
        self.power_control = MeAttribute("Power Control", 1, False, False)

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
    

class EthernetPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, False, False)
        self.fcs_errors_drop_events = MeAttribute("FCS errors Drop events", 4, False, False)
        self.excessive_collision_counter = MeAttribute("Excessive Collision Counter", 4, False, False)
        self.late_collision_counter = MeAttribute("Late Collision Counter", 4, False, False)
        self.frames_too_long = MeAttribute("Frames too long", 4, False, False)
        self.buffer_overflows_on_receive = MeAttribute("Buffer overflows on Receive", 4, False, False)
        self.buffer_overflows_on_transmit = MeAttribute("Buffer overflows on Transmit", 4, False, False)
        self.single_collision_frame_counter = MeAttribute("Single Collision Frame Counter", 4, False, False)
        self.multiple_collisions_frame_counter = MeAttribute("Multiple Collisions Frame Counter", 4, False, False)
        self.sqe_counter = MeAttribute("SQE counter", 4, False, False)
        self.deferred_transmission_counter = MeAttribute("Deferred Transmission Counter", 4, False, False)
        self.internal_mac_transmit_error_counter = MeAttribute("Internal MAC Transmit Error Counter", 4, False, False)
        self.carrier_sense_error_counter = MeAttribute("Carrier Sense Error Counter", 4, False, False)
        self.alignment_error_counter = MeAttribute("Alignment Error Counter", 4, False, False)
        self.internal_mac_receive_error_counter = MeAttribute("Internal MAC Receive Error Counter", 4, False, False)

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
    

class PonPhysicalPathTerminationPoint:
    def __init__(self):
        self.not_identified = MeAttribute("Not_identified", 4, False, False)

        self.attributes = (
            self.not_identified,
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
    

class VendorSpecific:
    def __init__(self):
        self.sub_entity = MeAttribute("Sub-Entity", 1, False, False)

        self.attributes = (
            self.sub_entity,
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
    

class MacBridgeServiceProfile:
    def __init__(self):
        self.spanning_tree_ind = MeAttribute("Spanning tree ind", 1, False, False)
        self.learning_ind = MeAttribute("Learning ind", 1, False, False)
        self.port_bridging_ind = MeAttribute("Port bridging ind", 1, False, False)
        self.priority = MeAttribute("Priority", 2, False, False)
        self.max_age = MeAttribute("Max age", 2, False, False)
        self.hello_time = MeAttribute("Hello time", 2, False, False)
        self.forward_delay = MeAttribute("Forward delay", 2, False, False)
        self.unknown_mac_address_discard = MeAttribute("Unknown MAC address discard", 1, False, False)
        self.mac_learning_depth = MeAttribute("MAC learning depth", 1, False, False)

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
    

class MacBridgePortConfigurationData:
    def __init__(self):
        self.bridge_id_pointer = MeAttribute("Bridge id pointer", 2, False, False)
        self.port_num = MeAttribute("Port num", 1, False, False)
        self.tp_type = MeAttribute("TP type", 1, False, False)
        self.tp_pointer = MeAttribute("TP pointer", 2, False, False)
        self.port_priority = MeAttribute("Port priority", 2, False, False)
        self.port_path_cost = MeAttribute("Port path cost", 2, False, False)
        self.port_spanning_tree_ind = MeAttribute("Port spanning tree ind", 1, False, False)
        self.encapsulation_method = MeAttribute("Encapsulation method", 1, False, False)
        self.lan_fcs_ind = MeAttribute("LAN FCS ind", 1, False, False)
        self.port_mac_address = MeAttribute("Port MAC address", 6, False, False)
        self.outbound_td_pointer = MeAttribute("Outbound TD pointer", 2, False, False)
        self.inbound_td_pointer = MeAttribute("Inbound TD pointer", 2, False, False)

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
    

class MacBridgePortDesignationData:
    def __init__(self):
        self.designated_bridge_root_cost_port = MeAttribute("Designated bridge root cost port", 24, False, False)
        self.port_state = MeAttribute("Port state", 1, False, False)

        self.attributes = (
            self.designated_bridge_root_cost_port,
            self.port_state,
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
    

class MacBridgePortFilterTableData:
    def __init__(self):
        self.mac_filter_table = MeAttribute("MAC filter table", 8, False, False)

        self.attributes = (
            self.mac_filter_table,
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
    

class MacBridgePmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.bridge_learning_entry_discard_count = MeAttribute("Bridge learning entry discard count", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.bridge_learning_entry_discard_count,
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
    

class MacBridgePortPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.forwarded_frame_counter = MeAttribute("Forwarded frame counter", 4, False, False)
        self.delay_exceeded_discard_counter = MeAttribute("Delay exceeded discard counter", 4, False, False)
        self.mtu_exceeded_discard_counter = MeAttribute("MTU exceeded discard counter", 4, False, False)
        self.received_frame_counter = MeAttribute("Received frame counter", 4, False, False)
        self.received_and_discarded_counter = MeAttribute("Received and discarded counter", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.forwarded_frame_counter,
            self.delay_exceeded_discard_counter,
            self.mtu_exceeded_discard_counter,
            self.received_frame_counter,
            self.received_and_discarded_counter,
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
    

class PhysicalPathTerminationPointPotsUni:
    def __init__(self):
        self.administrative_state = MeAttribute("Administrative state", 1, False, False)
        self.deprecated = MeAttribute("Deprecated", 2, False, False)
        self.arc = MeAttribute("ARC", 1, False, False)
        self.arc_interval = MeAttribute("ARC interval", 1, False, False)
        self.impedance = MeAttribute("Impedance", 1, False, False)
        self.transmission_path = MeAttribute("Transmission path", 1, False, False)
        self.rx_gain = MeAttribute("Rx gain", 1, False, False)
        self.tx_gain = MeAttribute("Tx gain", 1, False, False)
        self.operational_state = MeAttribute("Operational state", 1, False, False)
        self.hook_state = MeAttribute("Hook state", 1, False, False)
        self.pots_holdover_time = MeAttribute("POTS holdover time", 2, False, False)
        self.nominal_feed_voltage = MeAttribute("Nominal feed voltage", 1, False, False)

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
    

class VoiceServiceProfile:
    def __init__(self):
        self.announcement_type = MeAttribute("Announcement type", 1, False, False)
        self.jitter_target = MeAttribute("Jitter target", 2, False, False)
        self.jitter_buffer_max = MeAttribute("Jitter buffer max", 2, False, False)
        self.echo_cancel_ind = MeAttribute("Echo cancel ind", 1, False, False)
        self.pstn_protocol_variant = MeAttribute("PSTN protocol variant", 2, False, False)
        self.dtmf_digit_levels = MeAttribute("DTMF digit levels", 2, False, False)
        self.dtmf_digit_duration = MeAttribute("DTMF digit duration", 2, False, False)
        self.hook_flash_minimum_time = MeAttribute("Hook flash minimum time", 2, False, False)
        self.hook_flash_maximum_time = MeAttribute("Hook flash maximum time", 2, False, False)
        self.tone_pattern_table = MeAttribute("Tone pattern table", 20, False, False)
        self.tone_event_table = MeAttribute("Tone event table", 7, False, False)
        self.ringing_pattern_table = MeAttribute("Ringing pattern table", 5, False, False)
        self.ringing_event_table = MeAttribute("Ringing event table", 7, False, False)
        self.network_specific_extensions_pointer = MeAttribute("Network specific extensions pointer", 2, False, False)

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
    

class MacBridgePortFilterPreassignTable:
    def __init__(self):
        self.ipv4_multicast_filtering = MeAttribute("IPv4 multicast filtering", 1, False, False)
        self.ipv6_multicast_filtering = MeAttribute("IPv6 multicast filtering", 1, False, False)
        self.ipv4_broadcast_filtering = MeAttribute("IPv4 broadcast filtering", 1, False, False)
        self.rarp_filtering = MeAttribute("RARP filtering", 1, False, False)
        self.ipx_filtering = MeAttribute("IPX filtering", 1, False, False)
        self.netbeui_filtering = MeAttribute("NetBEUI filtering", 1, False, False)
        self.appletalk_filtering = MeAttribute("AppleTalk filtering", 1, False, False)
        self.bridge_management_information_filtering = MeAttribute("Bridge management information filtering", 1, False, False)
        self.arp_filtering = MeAttribute("ARP filtering", 1, False, False)

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
    

class PptpVideoUni:
    def __init__(self):
        self.administrative_state = MeAttribute("Administrative State", 1, False, False)
        self.operational_state = MeAttribute("Operational State", 1, False, False)
        self.arc = MeAttribute("ARC", 1, False, False)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False)
        self.power_control = MeAttribute("Power Control", 1, False, False)

        self.attributes = (
            self.administrative_state,
            self.operational_state,
            self.arc,
            self.arc_interval,
            self.power_control,
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
    

class VlanTaggingFilterData:
    def __init__(self):
        self.vlan_filter_list = MeAttribute("VLAN filter list", 24, False, False)
        self.forward_operation = MeAttribute("Forward operation", 1, False, False)
        self.number_of_entries = MeAttribute("Number of entries", 1, False, False)

        self.attributes = (
            self.vlan_filter_list,
            self.forward_operation,
            self.number_of_entries,
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
    

class EthernetPmHistoryData2:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.pppoe_filtered_frame_counter = MeAttribute("PPPoE filtered frame counter", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.pppoe_filtered_frame_counter,
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
    

class PptpVideoAni:
    def __init__(self):
        self.administrative_state = MeAttribute("Administrative State", 1, False, False)
        self.operational_state = MeAttribute("Operational State", 1, False, False)
        self.arc = MeAttribute("ARC", 1, False, False)
        self.arc_interval = MeAttribute("ARC Interval", 1, False, False)
        self.frequency_range_low = MeAttribute("Frequency Range Low", 1, False, False)
        self.frequency_range_high = MeAttribute("Frequency Range High", 1, False, False)
        self.signal_capability = MeAttribute("Signal Capability", 1, False, False)
        self.optical_signal_level = MeAttribute("Optical Signal Level", 1, False, False)
        self.pilot_signal_level = MeAttribute("Pilot Signal Level", 1, False, False)
        self.signal_level_min = MeAttribute("Signal Level min", 1, False, False)
        self.signal_level_max = MeAttribute("Signal Level max", 1, False, False)
        self.pilot_frequency = MeAttribute("Pilot Frequency", 4, False, False)
        self.agc_mode = MeAttribute("AGC Mode", 1, False, False)
        self.agc_setting = MeAttribute("AGC Setting", 1, False, False)
        self.video_lower_optical_threshold = MeAttribute("Video Lower Optical Threshold", 1, False, False)
        self.video_upper_optical_threshold = MeAttribute("Video Upper Optical Threshold", 1, False, False)

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
    

class PMapperServiceProfile8021:
    def __init__(self):
        self.tp_pointer = MeAttribute("TP Pointer", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_0 = MeAttribute("Interwork TP pointer for P-bit priority 0", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_1 = MeAttribute("Interwork TP pointer for P-bit priority 1", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_2 = MeAttribute("Interwork TP pointer for P-bit priority 2", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_3 = MeAttribute("Interwork TP pointer for P-bit priority 3", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_4 = MeAttribute("Interwork TP pointer for P-bit priority 4", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_5 = MeAttribute("Interwork TP pointer for P-bit priority 5", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_6 = MeAttribute("Interwork TP pointer for P-bit priority 6", 2, False, False)
        self.interwork_tp_pointer_for_p_bit_priority_7 = MeAttribute("Interwork TP pointer for P-bit priority 7", 2, False, False)
        self.unmarked_frame_option = MeAttribute("Unmarked frame option", 1, False, False)
        self.dscp_to_p_bit_mapping = MeAttribute("DSCP to P-bit mapping", 24, False, False)
        self.default_p_bit_marking = MeAttribute("Default P-bit marking", 1, False, False)
        self.tp_type = MeAttribute("TP Type", 1, False, False)

        self.attributes = (
            self.tp_pointer,
            self.interwork_tp_pointer_for_p_bit_priority_0,
            self.interwork_tp_pointer_for_p_bit_priority_1,
            self.interwork_tp_pointer_for_p_bit_priority_2,
            self.interwork_tp_pointer_for_p_bit_priority_3,
            self.interwork_tp_pointer_for_p_bit_priority_4,
            self.interwork_tp_pointer_for_p_bit_priority_5,
            self.interwork_tp_pointer_for_p_bit_priority_6,
            self.interwork_tp_pointer_for_p_bit_priority_7,
            self.unmarked_frame_option,
            self.dscp_to_p_bit_mapping,
            self.default_p_bit_marking,
            self.tp_type,
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
    

class Olt:
    def __init__(self):
        self.olt_vendor_id = MeAttribute("OLT vendor id", 4, False, False)
        self.equipment_id = MeAttribute("Equipment id", 20, False, False)
        self.olt_version = MeAttribute("OLT version", 14, False, False)

        self.attributes = (
            self.olt_vendor_id,
            self.equipment_id,
            self.olt_version,
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
    

class OntPowerShedding:
    def __init__(self):
        self.restore_power_timer_reset_interval = MeAttribute("Restore power timer reset interval", 2, False, False)
        self.data_class_shedding_interval = MeAttribute("Data class shedding interval", 2, False, False)
        self.voice_class_shedding_interval = MeAttribute("Voice class shedding interval", 2, False, False)
        self.video_overlay_class_shedding_interval = MeAttribute("Video overlay class shedding interval", 2, False, False)
        self.video_return_class_shedding_interval = MeAttribute("Video return class shedding interval", 2, False, False)
        self.dsl_class_shedding_interval = MeAttribute("DSL class shedding interval", 2, False, False)
        self.atm_class_shedding_interval = MeAttribute("ATM class shedding interval", 2, False, False)
        self.ces_class_shedding_interval = MeAttribute("CES class shedding interval", 2, False, False)
        self.frame_class_shedding_interval = MeAttribute("Frame class shedding interval", 2, False, False)
        self.sonet_class_shedding_interval = MeAttribute("SONET class shedding interval", 2, False, False)
        self.shedding_status = MeAttribute("Shedding status", 2, False, False)

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
    

class IpHostConfigData:
    def __init__(self):
        self.ip_options = MeAttribute("IP options", 1, False, False)
        self.mac_address = MeAttribute("MAC address", 6, False, False)
        self.ont_identifier = MeAttribute("Ont identifier", 25, False, False)
        self.ip_address = MeAttribute("IP address", 4, False, False)
        self.mask = MeAttribute("Mask", 4, False, False)
        self.gateway = MeAttribute("Gateway", 4, False, False)
        self.primary_dns = MeAttribute("Primary DNS", 4, False, False)
        self.secondary_dns = MeAttribute("Secondary DNS", 4, False, False)
        self.current_address = MeAttribute("Current address", 4, False, False)
        self.current_mask = MeAttribute("Current mask", 4, False, False)
        self.current_gateway = MeAttribute("Current gateway", 4, False, False)
        self.current_primary_dns = MeAttribute("Current primary DNS", 4, False, False)
        self.current_secondary_dns = MeAttribute("Current secondary DNS", 4, False, False)
        self.domain_name = MeAttribute("Domain name", 25, False, False)
        self.host_name = MeAttribute("Host name", 25, False, False)

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
    

class TcpUdpConfigData:
    def __init__(self):
        self.port_id = MeAttribute("Port ID", 2, False, False)
        self.protocol = MeAttribute("Protocol", 1, False, False)
        self.tos_diffserv_field = MeAttribute("TOS diffserv field", 1, False, False)
        self.ip_host_pointer = MeAttribute("IP host pointer", 2, False, False)

        self.attributes = (
            self.port_id,
            self.protocol,
            self.tos_diffserv_field,
            self.ip_host_pointer,
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
    

class NetworkAddress:
    def __init__(self):
        self.security_pointer = MeAttribute("Security pointer", 2, False, False)
        self.address_pointer = MeAttribute("Address pointer", 2, False, False)

        self.attributes = (
            self.security_pointer,
            self.address_pointer,
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
    

class VoipConfigData:
    def __init__(self):
        self.available_signalling_protocols = MeAttribute("Available signalling protocols", 1, False, False)
        self.signalling_protocol_used = MeAttribute("Signalling protocol used", 1, False, False)
        self.available_voip_configuration_methods = MeAttribute("Available VoIP configuration methods", 4, False, False)
        self.voip_configuration_method_used = MeAttribute("VoIP configuration method used", 1, False, False)
        self.voip_configuration_address_pointer = MeAttribute("VoIP configuration address pointer", 2, False, False)
        self.voip_configuration_state = MeAttribute("VoIP configuration state", 1, False, False)
        self.retrieve_profile = MeAttribute("Retrieve profile", 1, False, False)
        self.profile_version = MeAttribute("Profile version", 25, False, False)

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
    

class VoipVoiceCtp:
    def __init__(self):
        self.user_protocol_pointer = MeAttribute("User protocol pointer", 2, False, False)
        self.pptp_pointer = MeAttribute("PPTP pointer", 2, False, False)
        self.voip_media_profile_pointer = MeAttribute("VoIP media profile pointer", 2, False, False)
        self.signalling_code = MeAttribute("Signalling code", 1, False, False)

        self.attributes = (
            self.user_protocol_pointer,
            self.pptp_pointer,
            self.voip_media_profile_pointer,
            self.signalling_code,
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
    

class VoipLineStatus:
    def __init__(self):
        self.voip_codec_used = MeAttribute("voip codec used", 2, False, False)
        self.voip_voice_server_status = MeAttribute("voip voice server status", 1, False, False)
        self.voip_port_session_type = MeAttribute("voip port session type", 1, False, False)
        self.voip_call_1_packetperiod = MeAttribute("voip call 1 packetperiod", 2, False, False)
        self.voip_call_2_packetperiod = MeAttribute("voip call 2 packetperiod", 2, False, False)
        self.voip_call_1_dest_addr = MeAttribute("voip call 1 dest addr", 25, False, False)
        self.voip_call_2_dest_addr = MeAttribute("voip call 2 dest addr", 25, False, False)
        self.voip_line_state = MeAttribute("Voip line state", 1, False, False)
        self.emergency_call_status = MeAttribute("Emergency call status", 1, False, False)

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
    

class VoipMediaProfile:
    def __init__(self):
        self.fax_mode = MeAttribute("Fax mode", 1, False, False)
        self.voice_service_profile_pointer = MeAttribute("Voice service profile pointer", 2, False, False)
        self.codec_selection_first_order = MeAttribute("Codec selection first order", 1, False, False)
        self.packet_period_selection_first_order = MeAttribute("Packet period selection first order", 1, False, False)
        self.silence_suppression_first_order = MeAttribute("Silence suppression first order", 1, False, False)
        self.codec_selection_second_order = MeAttribute("Codec selection second order", 1, False, False)
        self.packet_period_selection_second_order = MeAttribute("Packet period selection second order", 1, False, False)
        self.silence_suppression_second_order = MeAttribute("Silence suppression second order", 1, False, False)
        self.codec_selection_third_order = MeAttribute("Codec selection third order", 1, False, False)
        self.packet_period_selection_third_order = MeAttribute("Packet period selection third order", 1, False, False)
        self.silence_suppression_fourth_order = MeAttribute("Silence suppression fourth order", 1, False, False)
        self.codec_selection_fourth_order = MeAttribute("Codec selection fourth order", 1, False, False)
        self.packet_period_selection_fourth_order = MeAttribute("Packet period selection fourth order", 1, False, False)
        self.silence_suppression_fourth_order = MeAttribute("Silence suppression fourth order", 1, False, False)
        self.oob_dtmf = MeAttribute("OOB DTMF", 1, False, False)
        self.rtp_profile_pointer = MeAttribute("RTP profile pointer", 2, False, False)

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
    

class RtpProfileData:
    def __init__(self):
        self.local_port_min = MeAttribute("Local port min", 2, False, False)
        self.local_port_max = MeAttribute("Local port max", 2, False, False)
        self.dscp_mark = MeAttribute("DSCP mark", 1, False, False)
        self.piggyback_events = MeAttribute("Piggyback events", 1, False, False)
        self.tone_events = MeAttribute("Tone events", 1, False, False)
        self.dtmf_events = MeAttribute("DTMF events", 1, False, False)
        self.cas_events = MeAttribute("CAS events", 1, False, False)
        self.ip_host_config_pointer = MeAttribute("IP host config pointer", 2, False, False)

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
    

class AuthenticationSecurityMethod:
    def __init__(self):
        self.validation_scheme = MeAttribute("Validation scheme", 1, False, False)
        self.username_1 = MeAttribute("Username 1", 25, False, False)
        self.password = MeAttribute("Password", 25, False, False)
        self.realm = MeAttribute("Realm", 25, False, False)
        self.username_2 = MeAttribute("Username 2", 25, False, False)

        self.attributes = (
            self.validation_scheme,
            self.username_1,
            self.password,
            self.realm,
            self.username_2,
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
    

class SipAgentConfigData:
    def __init__(self):
        self.proxy_server_address_pointer = MeAttribute("Proxy server address pointer", 2, False, False)
        self.outbound_proxy_address_pointer = MeAttribute("Outbound proxy address pointer", 2, False, False)
        self.primary_sip_dns = MeAttribute("Primary SIP DNS", 4, False, False)
        self.secondary_sip_dns = MeAttribute("Secondary SIP DNS", 4, False, False)
        self.tcp_udp_pointer = MeAttribute("TCP UDP pointer", 2, False, False)
        self.sip_reg_exp_time = MeAttribute("SIP reg exp time", 4, False, False)
        self.sip_rereg_head_start_time = MeAttribute("SIP rereg head start time", 4, False, False)
        self.host_part_uri = MeAttribute("Host part URI", 2, False, False)
        self.sip_status = MeAttribute("SIP status", 1, False, False)
        self.sip_registrar = MeAttribute("SIP registrar", 2, False, False)
        self.softswitch = MeAttribute("Softswitch", 4, False, False)
        self.sip_response_table = MeAttribute("SIP response table", 5, False, False)
        self.sip_option_transmit_control = MeAttribute("SIP option transmit control", 1, False, False)
        self.sip_uri_format = MeAttribute("SIP URI format", 1, False, False)
        self.redundant_sip_agent_pointer = MeAttribute("Redundant SIP agent pointer", 2, False, False)

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
    

class SipUserData:
    def __init__(self):
        self.sip_agent_pointer = MeAttribute("SIP agent pointer", 2, False, False)
        self.user_part_aor = MeAttribute("User part AOR", 2, False, False)
        self.sip_display_name = MeAttribute("SIP display name", 25, False, False)
        self.username_and_password = MeAttribute("Username and password", 2, False, False)
        self.voicemail_server_sip_uri = MeAttribute("Voicemail server SIP URI", 2, False, False)
        self.voicemail_subscription_expiration_time = MeAttribute("Voicemail subscription expiration time", 4, False, False)
        self.network_dial_plan_pointer = MeAttribute("Network dial plan pointer", 2, False, False)
        self.application_services_profile_pointer = MeAttribute("Application services profile pointer", 2, False, False)
        self.feature_code_pointer = MeAttribute("Feature code pointer", 2, False, False)
        self.pptp_pointer = MeAttribute("PPTP pointer", 2, False, False)
        self.release_timer = MeAttribute("Release timer", 1, False, False)
        self.roh_timer = MeAttribute("ROH timer", 1, False, False)

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
    

class LargeString:
    def __init__(self):
        self.number_of_parts = MeAttribute("Number of parts", 1, False, False)

        self.attributes = (
            self.number_of_parts,
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
    

class OntRemoteDebug:
    def __init__(self):
        self.command_format = MeAttribute("Command format", 1, False, False)
        self.command = MeAttribute("Command", 25, False, False)
        self.reply_table = MeAttribute("Reply table", 4, False, False)

        self.attributes = (
            self.command_format,
            self.command,
            self.reply_table,
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
    

class EquipmentProtectionProfile:
    def __init__(self):
        self.protect_slot_1,protect_slot_2 = MeAttribute("Protect slot 1,protect slot 2", 2, False, False)
        self.working_slot_1,working_slot_2,working_slot_3,working_slot_4,working_slot_5,working_slot_6,working_slot_7,working_slot_8 = MeAttribute("working slot 1,working slot 2,working slot 3,working slot 4,working slot 5,working slot 6,working slot 7,working slot 8", 8, False, False)
        self.protect_status_1,protect_status_2 = MeAttribute("Protect status 1,protect status 2", 2, False, False)
        self.revertive_ind = MeAttribute("Revertive ind", 1, False, False)
        self.wait_to_restore_time = MeAttribute("Wait to restore time", 1, False, False)

        self.attributes = (
            self.protect_slot_1,protect_slot_2,
            self.working_slot_1,working_slot_2,working_slot_3,working_slot_4,working_slot_5,working_slot_6,working_slot_7,working_slot_8,
            self.protect_status_1,protect_status_2,
            self.revertive_ind,
            self.wait_to_restore_time,
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
    

class EquipmentExtensionPackage:
    def __init__(self):
        self.environmental_sense = MeAttribute("Environmental sense", 2, False, False)
        self.contact_closure_output = MeAttribute("Contact closure output", 2, False, False)

        self.attributes = (
            self.environmental_sense,
            self.contact_closure_output,
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
    

class ExtendedVlanTaggingOperationConfigurationData:
    def __init__(self):
        self.association_type = MeAttribute("Association type", 1, False, False)
        self.received_frame_vlan_tagging_operation_table_max_size = MeAttribute("Received frame VLAN tagging operation table max size", 2, False, False)
        self.input_tpid = MeAttribute("Input TPID", 2, False, False)
        self.output_tpid = MeAttribute("Output TPID", 2, False, False)
        self.downstream_mode = MeAttribute("Downstream mode", 1, False, False)
        self.received_frame_vlan_tagging_operation_table = MeAttribute("Received frame VLAN tagging operation table", 16, False, False)
        self.associated_me_pointer = MeAttribute("Associated ME pointer", 2, False, False)
        self.dscp_to_p_bit_mapping = MeAttribute("DSCP to P-bit mapping", 24, False, False)

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
    

class PppoeByGcom:
    def __init__(self):
        self.nat = MeAttribute("NAT", 1, False, False)
        self.auth = MeAttribute("Auth", 1, False, False)
        self.connect = MeAttribute("Connect", 1, False, False)
        self.release_time = MeAttribute("Release Time", 2, False, False)
        self.username = MeAttribute("Username", 25, False, False)
        self.password = MeAttribute("Password", 25, False, False)
        self.attribute7 = MeAttribute("Attribute7", 1, False, False)
        self.attribute8 = MeAttribute("Attribute8", 1, False, False)
        self.pointer_to_ip_host_config_data_me = MeAttribute("Pointer to IP Host Config Data ME", 2, False, False)
        self.pointer_to_larg_string_me_pointer_for_username = MeAttribute("Pointer to Larg String ME Pointer for Username", 2, False, False)
        self.pointer_to_larg_string_me_pointer_for_service_name = MeAttribute("Pointer to Larg String ME Pointer for Service Name", 2, False, False)

        self.attributes = (
            self.nat,
            self.auth,
            self.connect,
            self.release_time,
            self.username,
            self.password,
            self.attribute7,
            self.attribute8,
            self.pointer_to_ip_host_config_data_me,
            self.pointer_to_larg_string_me_pointer_for_username,
            self.pointer_to_larg_string_me_pointer_for_service_name,
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
    

class EthernetPerformanceMonitoringHistoryData4:
    def __init__(self):
        self.interval_end_time = MeAttribute("interval_end_time", 1, False, False)
        self.threshold_data_1_2_id = MeAttribute("threshold_data_1_2_id", 2, False, False)
        self.association_type = MeAttribute("association_type", 1, False, False)
        self.transmitted_traffic = MeAttribute("transmitted_traffic", 4, False, False)
        self.received_traffic = MeAttribute("received_traffic", 4, False, False)
        self.transmitted_rate = MeAttribute("transmitted_rate", 4, False, False)
        self.received_rate = MeAttribute("received_rate", 4, False, False)
        self.transmitted_octets = MeAttribute("transmitted_octets", 4, False, False)
        self.received_octets = MeAttribute("received_octets", 4, False, False)
        self.transmitted_discarded_counter = MeAttribute("transmitted_discarded_counter", 4, False, False)
        self.received_discarded_counter = MeAttribute("received_discarded_counter", 4, False, False)
        self.transmitted_error_counter = MeAttribute("transmitted_error_counter", 4, False, False)
        self.received_error_counter = MeAttribute("received_error_counter", 4, False, False)

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
    

class Ont:
    def __init__(self):
        self.vendor_id = MeAttribute("Vendor Id", 4, False, False)
        self.version = MeAttribute("Version", 14, False, False)
        self.serial_nr = MeAttribute("Serial Nr", 8, False, False)
        self.traffic_management_option = MeAttribute("Traffic management option", 1, False, False)
        self.vp_vc_cross_connection_function_option = MeAttribute("VP VC cross connection function option", 1, False, False)
        self.battery_backup = MeAttribute("Battery backup", 1, False, False)
        self.administrative_state = MeAttribute("Administrative State", 1, False, False)
        self.operational_state = MeAttribute("Operational State", 1, False, False)

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
    

class Ont2:
    def __init__(self):
        self.equipment_id = MeAttribute("Equipment id", 20, False, False)
        self.omcc_version = MeAttribute("OMCC version", 1, False, False)
        self.vendor_product_code = MeAttribute("Vendor product code", 2, False, False)
        self.security_capability = MeAttribute("Security capability", 1, False, False)
        self.security_mode = MeAttribute("Security mode", 1, False, False)
        self.total_priority_queue_number = MeAttribute("Total priority queue number", 2, False, False)
        self.total_traffic_scheduler_number = MeAttribute("Total traffic scheduler number", 1, False, False)
        self.mode = MeAttribute("Mode", 1, False, False)
        self.total_gem_port_id_number = MeAttribute("Total GEM port-ID number", 2, False, False)
        self.sysup_time = MeAttribute("SysUp Time", 4, False, False)

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
    

class PonTcAdapter:
    def __init__(self):
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)
        self.not_identified = MeAttribute("Not_identified", 4, False, False)

        self.attributes = (
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
            self.not_identified,
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
    

class T:
    def __init__(self):
        self.alloc_id = MeAttribute("Alloc-id", 2, False, False)
        self.mode_indicator = MeAttribute("Mode indicator", 1, False, False)
        self.policy = MeAttribute("Policy", 1, False, False)

        self.attributes = (
            self.alloc_id,
            self.mode_indicator,
            self.policy,
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
    

class Ani:
    def __init__(self):
        self.sr_indication = MeAttribute("SR indication", 1, False, False)
        self.total_t_cont_number = MeAttribute("Total T-CONT number", 2, False, False)
        self.gem_block_length = MeAttribute("GEM block length", 2, False, False)
        self.piggyback_dba_reporting = MeAttribute("Piggyback DBA reporting", 1, False, False)
        self.whole_ont_dba_reporting = MeAttribute("Whole ONT DBA reporting", 1, False, False)
        self.sf_threshold = MeAttribute("SF threshold", 1, False, False)
        self.sd_threshold = MeAttribute("SD threshold", 1, False, False)
        self.arc = MeAttribute("ARC", 1, False, False)
        self.arc_interval = MeAttribute("ARC interval", 1, False, False)
        self.optical_signal_level = MeAttribute("Optical signal level", 2, False, False)
        self.lower_optical_threshold = MeAttribute("Lower optical threshold", 1, False, False)
        self.upper_optical_threshold = MeAttribute("Upper optical threshold", 1, False, False)
        self.ont_response_time = MeAttribute("ONT response time", 2, False, False)
        self.transmit_optical_level = MeAttribute("Transmit optical level", 2, False, False)
        self.lower_transmit_power_threshold = MeAttribute("Lower transmit power threshold", 1, False, False)
        self.upper_transmit_power_threshold = MeAttribute("Upper transmit power threshold", 1, False, False)

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
    

class Uni:
    def __init__(self):
        self.config_option_status = MeAttribute("Config option status", 2, False, False)
        self.administrative_state = MeAttribute("Administrative state", 1, False, False)

        self.attributes = (
            self.config_option_status,
            self.administrative_state,
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
    

class GemInterworkingTerminationPoint:
    def __init__(self):
        self.gem_port_network_ctp_connectivity_pointer = MeAttribute("GEM port network CTP connectivity pointer", 2, False, False)
        self.interworking_option = MeAttribute("Interworking option", 1, False, False)
        self.service_profile_pointer = MeAttribute("Service profile pointer", 2, False, False)
        self.interworking_termination_point_pointer = MeAttribute("Interworking termination point pointer", 2, False, False)
        self.pptp_counter = MeAttribute("PPTP counter", 1, False, False)
        self.operational_state = MeAttribute("Operational state", 1, False, False)
        self.gal_profile_pointer = MeAttribute("GAL profile pointer", 2, False, False)
        self.gal_loopback_configuration = MeAttribute("GAL loopback configuration", 1, False, False)

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
    

class GemPortPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.lost_packets = MeAttribute("Lost packets", 4, False, False)
        self.misinserted_packets = MeAttribute("Misinserted packets", 4, False, False)
        self.received_packets = MeAttribute("Received packets", 5, False, False)
        self.received_blocks = MeAttribute("Received blocks", 5, False, False)
        self.transmitted_blocks = MeAttribute("Transmitted blocks", 5, False, False)
        self.impaired_blocks = MeAttribute("Impaired blocks", 4, False, False)
        self.transmitted_packets = MeAttribute("Transmitted packets", 5, False, False)

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
    

class GemPortNetworkCtp:
    def __init__(self):
        self.port_id_value = MeAttribute("Port id value", 2, False, False)
        self.t_cont_pointer = MeAttribute("T-CONT pointer", 2, False, False)
        self.direction = MeAttribute("Direction", 1, False, False)
        self.traffic_management_pointer_for_upstream = MeAttribute("Traffic management pointer for upstream", 2, False, False)
        self.traffic_descriptor_profile_pointer = MeAttribute("Traffic descriptor profile pointer", 2, False, False)
        self.uni_counter = MeAttribute("UNI counter", 1, False, False)
        self.priority_queue_pointer_for_downstream = MeAttribute("Priority queue pointer for downstream", 2, False, False)
        self.encryption_state = MeAttribute("Encryption state", 1, False, False)

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
    

class GalTdmProfile:
    def __init__(self):
        self.gem_frame_loss_integration_period = MeAttribute("GEM frame loss integration period", 2, False, False)

        self.attributes = (
            self.gem_frame_loss_integration_period,
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
    

class GalEthernetProfile:
    def __init__(self):
        self.maximum_gem_payload_size = MeAttribute("Maximum GEM payload size", 2, False, False)

        self.attributes = (
            self.maximum_gem_payload_size,
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
    

class ThresholdData1:
    def __init__(self):
        self.threshold_value_1 = MeAttribute("Threshold value 1", 4, False, False)
        self.threshold_value_2 = MeAttribute("Threshold value 2", 4, False, False)
        self.threshold_value_3 = MeAttribute("Threshold value 3", 4, False, False)
        self.threshold_value_4 = MeAttribute("Threshold value 4", 4, False, False)
        self.threshold_value_5 = MeAttribute("Threshold value 5", 4, False, False)
        self.threshold_value_6 = MeAttribute("Threshold value 6", 4, False, False)
        self.threshold_value_7 = MeAttribute("Threshold value 7", 4, False, False)

        self.attributes = (
            self.threshold_value_1,
            self.threshold_value_2,
            self.threshold_value_3,
            self.threshold_value_4,
            self.threshold_value_5,
            self.threshold_value_6,
            self.threshold_value_7,
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
    

class ThresholdData2:
    def __init__(self):
        self.threshold_value_8 = MeAttribute("Threshold value 8", 4, False, False)
        self.threshold_value_9 = MeAttribute("Threshold value 9", 4, False, False)
        self.threshold_value_10 = MeAttribute("Threshold value 10", 4, False, False)
        self.threshold_value_11 = MeAttribute("Threshold value 11", 4, False, False)
        self.threshold_value_12 = MeAttribute("Threshold value 12", 4, False, False)
        self.threshold_value_13 = MeAttribute("Threshold value 13", 4, False, False)
        self.threshold_value_14 = MeAttribute("Threshold value 14", 4, False, False)

        self.attributes = (
            self.threshold_value_8,
            self.threshold_value_9,
            self.threshold_value_10,
            self.threshold_value_11,
            self.threshold_value_12,
            self.threshold_value_13,
            self.threshold_value_14,
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
    

class GalTdmPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.gem_frame_loss = MeAttribute("GEM frame loss", 4, False, False)
        self.buffer_underflows = MeAttribute("Buffer underflows", 4, False, False)
        self.buffer_overflows = MeAttribute("Buffer overflows", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.gem_frame_loss,
            self.buffer_underflows,
            self.buffer_overflows,
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
    

class GalEthernetPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.discarded_frames = MeAttribute("Discarded frames", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.discarded_frames,
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
    

class PriorityQueue:
    def __init__(self):
        self.queue_configuration_option = MeAttribute("Queue Configuration Option", 1, False, False)
        self.maximum_queue_size = MeAttribute("Maximum Queue Size", 2, False, False)
        self.allocated_queue_size = MeAttribute("Allocated Queue Size", 2, False, False)
        self.discard_block_counter_reset_interval = MeAttribute("Discard-block Counter Reset Interval", 2, False, False)
        self.threshold_value_for_discarded_blocks_due_to_buffer_overflow = MeAttribute("Threshold Value For Discarded Blocks Due To Buffer Overflow", 2, False, False)
        self.related_port = MeAttribute("Related Port", 4, False, False)
        self.traffic_scheduler_g_pointer = MeAttribute("Traffic Scheduler-G Pointer", 2, False, False)
        self.weight = MeAttribute("Weight", 1, False, False)
        self.back_pressure_operation = MeAttribute("Back Pressure Operation", 2, False, False)
        self.back_pressure_time = MeAttribute("Back Pressure Time", 4, False, False)
        self.back_pressure_occur_queue_threshold = MeAttribute("Back Pressure Occur Queue Threshold", 2, False, False)
        self.back_pressure_clear_queue_threshold = MeAttribute("Back Pressure Clear Queue Threshold", 2, False, False)

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
    

class TrafficScheduler:
    def __init__(self):
        self.tcont_pointer = MeAttribute("TCONT pointer", 2, False, False)
        self.traffic_shed_pointer = MeAttribute("traffic shed pointer", 2, False, False)
        self.policy = MeAttribute("policy", 1, False, False)
        self.priority_weight = MeAttribute("priority weight", 1, False, False)

        self.attributes = (
            self.tcont_pointer,
            self.traffic_shed_pointer,
            self.policy,
            self.priority_weight,
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
    

class ProtectionData:
    def __init__(self):
        self.working_ani_g_pointer = MeAttribute("Working ANI-G pointer", 2, False, False)
        self.protection_ani_g_pointer = MeAttribute("Protection ANI-G pointer", 2, False, False)
        self.protection_type = MeAttribute("Protection type", 2, False, False)
        self.revertive_ind = MeAttribute("Revertive ind", 1, False, False)
        self.wait_to_restore_time = MeAttribute("Wait to restore time", 1, False, False)
        self.switching_guard_time = MeAttribute("Switching guard time", 2, False, False)

        self.attributes = (
            self.working_ani_g_pointer,
            self.protection_ani_g_pointer,
            self.protection_type,
            self.revertive_ind,
            self.wait_to_restore_time,
            self.switching_guard_time,
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
    

class MulticastGemInterworkingTerminationPoint:
    def __init__(self):
        self.gem_port_network_ctp_connectivity_pointer = MeAttribute("GEM port network CTP connectivity pointer", 2, False, False)
        self.interworking_option = MeAttribute("Interworking option", 1, False, False)
        self.service_profile_pointer = MeAttribute("Service profile pointer", 2, False, False)
        self.interworking_termination_point_pointer = MeAttribute("Interworking termination point pointer", 2, False, False)
        self.pptp_counter = MeAttribute("PPTP counter", 1, False, False)
        self.operational_state = MeAttribute("Operational state", 1, False, False)
        self.gal_profile_pointer = MeAttribute("GAL profile pointer", 2, False, False)
        self.gal_loopback_configuration = MeAttribute("GAL loopback configuration", 1, False, False)
        self.multicast_address_table = MeAttribute("Multicast address table", 12, False, False)

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
    

class Omci:
    def __init__(self):
        self.me_type_table = MeAttribute("ME Type Table", 2, False, False)
        self.message_type_table = MeAttribute("Message Type Table", 2, False, False)

        self.attributes = (
            self.me_type_table,
            self.message_type_table,
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
    

class Dot1XPortExtensionPackage:
    def __init__(self):
        self.dot1x_enable = MeAttribute("Dot1x Enable", 1, False, False)
        self.action_register = MeAttribute("Action Register", 1, False, False)
        self.authenticator_pae_state = MeAttribute("Authenticator PAE State", 1, False, False)
        self.backend_authentication_state = MeAttribute("Backend Authentication State", 1, False, False)
        self.admin_controlled_directions = MeAttribute("Admin Controlled Directions", 1, False, False)
        self.operational_controlled_directions = MeAttribute("Operational Controlled Directions", 1, False, False)
        self.authenticator_controlled_port_status = MeAttribute("Authenticator Controlled Port Status", 1, False, False)
        self.quiet_period = MeAttribute("Quiet Period", 2, False, False)
        self.server_timeout_period = MeAttribute("Server Timeout Period", 2, False, False)
        self.reauthentication_period = MeAttribute("Reauthentication Period", 2, False, False)
        self.reauthentication_enabled = MeAttribute("Reauthentication Enabled", 1, False, False)
        self.key_transmission_enabled = MeAttribute("Key transmission Enabled", 1, False, False)

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
    

class Dot1XConfigurationProfile:
    def __init__(self):
        self.circuit_id_prefix = MeAttribute("Circuit ID prefix", 2, False, False)
        self.fallback_policy = MeAttribute("Fallback policy", 1, False, False)
        self.auth_server_1 = MeAttribute("Auth server 1", 2, False, False)
        self.shared_secret_auth1 = MeAttribute("Shared secret auth1", 25, False, False)
        self.auth_server_2 = MeAttribute("Auth server 2", 2, False, False)
        self.shared_secret_auth2 = MeAttribute("Shared secret auth2", 25, False, False)
        self.auth_server_3 = MeAttribute("Auth server 3", 2, False, False)
        self.shared_secret_auth3 = MeAttribute("Shared secret auth3", 25, False, False)
        self.olt_proxy_address = MeAttribute("OLT proxy address", 4, False, False)

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
    

class EthernetPmHistoryData3:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, False, False)
        self.drop_events = MeAttribute("Drop events", 4, False, False)
        self.octets = MeAttribute("Octets", 4, False, False)
        self.packets = MeAttribute("Packets", 4, False, False)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, False)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, False)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, False)
        self.fragments = MeAttribute("Fragments", 4, False, False)
        self.jabbers = MeAttribute("Jabbers", 4, False, False)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, False)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, False)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, False)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, False)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, False)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, False)

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
    

class PortMappingPackage:
    def __init__(self):
        self.max_ports = MeAttribute("Max ports", 1, False, False)
        self.port_list_1 = MeAttribute("Port list 1", 16, False, False)
        self.port_list_2 = MeAttribute("Port list 2", 16, False, False)
        self.port_list_3 = MeAttribute("Port list 3", 16, False, False)
        self.port_list_4 = MeAttribute("Port list 4", 16, False, False)
        self.port_list_5 = MeAttribute("Port list 5", 16, False, False)
        self.port_list_6 = MeAttribute("Port list 6", 16, False, False)
        self.port_list_7 = MeAttribute("Port list 7", 16, False, False)
        self.port_list_8 = MeAttribute("Port list 8", 16, False, False)

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
    

class MulticastOperationsProfile:
    def __init__(self):
        self.igmp_version = MeAttribute("IGMP version", 1, False, False)
        self.igmp_function = MeAttribute("IGMP function", 1, False, False)
        self.immediate_leave = MeAttribute("Immediate leave", 1, False, False)
        self.upstream_igmp_tci = MeAttribute("Upstream IGMP TCI", 2, False, False)
        self.upstream_igmp_tag_control = MeAttribute("Upstream IGMP tag control", 1, False, False)
        self.upstream_igmp_rate = MeAttribute("Upstream IGMP rate", 4, False, False)
        self.dynamic_access_control_list_table = MeAttribute("Dynamic access control list table", 24, False, False)
        self.static_access_control_list_table = MeAttribute("Static access control list table", 24, False, False)
        self.lost_groups_list_table = MeAttribute("Lost groups list table", 10, False, False)
        self.robustness = MeAttribute("Robustness", 1, False, False)
        self.querier_ip_address = MeAttribute("Querier IP address", 4, False, False)
        self.query_interval = MeAttribute("Query interval", 4, False, False)
        self.query_max_response_time = MeAttribute("Query max response time", 4, False, False)
        self.last_member_query_interval = MeAttribute("Last member query interval", 4, False, False)

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
    

class MulticastSubscriberConfigInfo:
    def __init__(self):
        self.me_type = MeAttribute("ME type", 1, False, False)
        self.multicast_operations_profile_pointer = MeAttribute("Multicast operations profile pointer", 2, False, False)
        self.max_simultaneous_groups = MeAttribute("Max simultaneous groups", 2, False, False)
        self.max_multicast_bandwidth = MeAttribute("Max multicast bandwidth", 4, False, False)
        self.bandwidth_enforcement = MeAttribute("Bandwidth enforcement", 1, False, False)

        self.attributes = (
            self.me_type,
            self.multicast_operations_profile_pointer,
            self.max_simultaneous_groups,
            self.max_multicast_bandwidth,
            self.bandwidth_enforcement,
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
    

class MulticastSubscriberMonitor:
    def __init__(self):
        self.me_type = MeAttribute("ME type", 1, False, False)
        self.current_multicast_bandwidth = MeAttribute("Current multicast bandwidth", 4, False, False)
        self.max_join_messages_counter = MeAttribute("Max Join messages counter", 4, False, False)
        self.bandwidth_exceeded_counter = MeAttribute("Bandwidth exceeded counter", 4, False, False)
        self.active_group_list_table = MeAttribute("Active group list table", 24, False, False)

        self.attributes = (
            self.me_type,
            self.current_multicast_bandwidth,
            self.max_join_messages_counter,
            self.bandwidth_exceeded_counter,
            self.active_group_list_table,
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
    

class FecPmHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data id", 2, False, False)
        self.corrected_bytes = MeAttribute("Corrected bytes", 4, False, False)
        self.corrected_code_words = MeAttribute("Corrected code words", 4, False, False)
        self.uncorrectable_code_words = MeAttribute("Uncorrectable code words", 4, False, False)
        self.total_code_words = MeAttribute("Total code words", 4, False, False)
        self.fec_seconds = MeAttribute("FEC seconds", 2, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.corrected_bytes,
            self.corrected_code_words,
            self.uncorrectable_code_words,
            self.total_code_words,
            self.fec_seconds,
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
    

class FileTransferController:
    def __init__(self):
        self.supported_transfer_protocols = MeAttribute("Supported transfer protocols", 2, False, False)
        self.file_type = MeAttribute("File type", 2, False, False)
        self.file_instance = MeAttribute("File instance", 2, False, False)
        self.local_file_name_pointer = MeAttribute("Local file name pointer", 2, False, False)
        self.network_address_pointer = MeAttribute("Network address pointer", 2, False, False)
        self.file_transfer_trigger = MeAttribute("File transfer trigger", 1, False, False)
        self.file_transfer_status = MeAttribute("File transfer status", 1, False, False)
        self.gem_iwtp_pointer = MeAttribute("GEM IWTP pointer", 2, False, False)
        self.undersize_packets = MeAttribute("Undersize Packets", 2, False, False)
        self.vlan = MeAttribute("VLAN", 2, False, False)
        self.file_size = MeAttribute("File size", 4, False, False)
        self.directory_listing_table = MeAttribute("Directory listing table", 25, False, False)

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
    

class EthernetFramePmHistoryDataDs:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, False, False)
        self.drop_events = MeAttribute("Drop events", 4, False, False)
        self.octets = MeAttribute("Octets", 4, False, False)
        self.packets = MeAttribute("Packets", 4, False, False)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, False)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, False)
        self.crc_errored_packets = MeAttribute("CRC Errored Packets", 4, False, False)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, False)
        self.oversize_packets = MeAttribute("Oversize Packets", 4, False, False)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, False)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, False)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, False)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, False)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, False)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, False)

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
    

class EthernetFramePmHistoryDataUs:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval End Time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold Data Id", 2, False, False)
        self.drop_events = MeAttribute("Drop events", 4, False, False)
        self.octets = MeAttribute("Octets", 4, False, False)
        self.packets = MeAttribute("Packets", 4, False, False)
        self.broadcast_packets = MeAttribute("Broadcast Packets", 4, False, False)
        self.multicast_packets = MeAttribute("Multicast Packets", 4, False, False)
        self.crc_errored_packets = MeAttribute("CRC Errored Packets", 4, False, False)
        self.undersize_packets = MeAttribute("Undersize Packets", 4, False, False)
        self.oversize_packets = MeAttribute("Oversize Packets", 4, False, False)
        self.packets_64_octets = MeAttribute("Packets 64 Octets", 4, False, False)
        self.packets_65_to_127_octets = MeAttribute("Packets 65 to 127 Octets", 4, False, False)
        self.packets_128_to_255_octets = MeAttribute("Packets 128 to 255 Octets", 4, False, False)
        self.packets_256_to_511_octets = MeAttribute("Packets 256 to 511 Octets", 4, False, False)
        self.packets_512_to_1023_octets = MeAttribute("Packets 512 to 1023 Octets", 4, False, False)
        self.packets_1024_to_1518_octets = MeAttribute("Packets 1024 to 1518 Octets", 4, False, False)

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
    

class VirtualEthernetInterfacePoint:
    def __init__(self):
        self.administrative_state = MeAttribute("Administrative state", 14, False, False)
        self.operational_state = MeAttribute("Operational state", 1, False, False)
        self.interdomain_name = MeAttribute("Interdomain name", 25, False, False)
        self.tcp_udp_pointer = MeAttribute("TCP UDP pointer", 2, False, False)
        self.iana_assigned_port = MeAttribute("IANA assigned port", 2, False, False)

        self.attributes = (
            self.administrative_state,
            self.operational_state,
            self.interdomain_name,
            self.tcp_udp_pointer,
            self.iana_assigned_port,
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
    

class BbfTr:
    def __init__(self):
        self.administrative_state = MeAttribute("Administrative state", 1, False, False)
        self.acs_network_address = MeAttribute("ACS network address", 2, False, False)
        self.associated_tag = MeAttribute("Associated tag", 2, False, False)

        self.attributes = (
            self.administrative_state,
            self.acs_network_address,
            self.associated_tag,
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
    

class GemPortNetworkCtpPerformanceMonitoringHistoryData:
    def __init__(self):
        self.interval_end_time = MeAttribute("Interval end time", 1, False, False)
        self.threshold_data_id = MeAttribute("Threshold data ID", 2, False, False)
        self.transmitted_gem_frames = MeAttribute("Transmitted GEM frames", 4, False, False)
        self.received_gem_frames = MeAttribute("Received GEM frames", 4, False, False)
        self.received_payload_bytes = MeAttribute("Received payload bytes", 8, False, False)
        self.transmitted_payload_bytes = MeAttribute("Transmitted payload bytes", 8, False, False)
        self.encryption_key_errors = MeAttribute("Encryption key errors", 4, False, False)

        self.attributes = (
            self.interval_end_time,
            self.threshold_data_id,
            self.transmitted_gem_frames,
            self.received_gem_frames,
            self.received_payload_bytes,
            self.transmitted_payload_bytes,
            self.encryption_key_errors,
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
    

class PppoeIntelbrasOlt8820I110Gi:
    def __init__(self):
        self.wan_type = MeAttribute("Wan-Type", 1, False, False)
        self.user = MeAttribute("User", 25, False, False)
        self.password = MeAttribute("Password", 25, False, False)
        self.mppe = MeAttribute("MPPE", 1, False, False)
        self.service_name = MeAttribute("Service Name", 25, False, False)

        self.attributes = (
            self.wan_type,
            self.user,
            self.password,
            self.mppe,
            self.service_name,
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
    

class WanExtendedConfigFh:
    def __init__(self):
        self.wan_number = MeAttribute("WAN Number", 2, False, False)
        self.wan_index = MeAttribute("WAN Index", 1, False, False)
        self.wan_name_1 = MeAttribute("WAN name 1", 16, False, False)
        self.wan_name_2_dns = MeAttribute("WAN name 2 DNS", 16, False, False)
        self.wan_name_3_dns = MeAttribute("WAN name 3 DNS", 16, False, False)
        self.wan_name_4 = MeAttribute("WAN name 4", 16, False, False)
        self.wan_uppir = MeAttribute("WAN UPPIR", 4, False, False)
        self.wan_downpir = MeAttribute("WAN DOWNPIR", 4, False, False)

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
    

class WanProfileFileFh:
    def __init__(self):
        self.create_or_delete_wan_ipv4 = MeAttribute("Create-or-Delete WAN IPV4", 2, False, False)
        self.create_or_delete_wan_ipv6 = MeAttribute("Create-or-Delete WAN IPV6", 2, False, False)

        self.attributes = (
            self.create_or_delete_wan_ipv4,
            self.create_or_delete_wan_ipv6,
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
    

class WanModeFh:
    def __init__(self):
        self.wan_index = MeAttribute("WAN INDEX", 1, False, False)
        self.wan_name_1 = MeAttribute("WAN name 1", 16, False, False)
        self.wan_name_2 = MeAttribute("WAN name 2", 16, False, False)
        self.wan_name_3 = MeAttribute("WAN name 3", 16, False, False)
        self.wan_name_4 = MeAttribute("WAN name 4", 16, False, False)
        self.wan_conected_mode = MeAttribute("WAN Conected Mode", 1, False, False)
        self.wan_conected_type = MeAttribute("WAN Conected Type", 1, False, False)
        self.vlan = MeAttribute("VLAN", 2, False, False)
        self.cos = MeAttribute("COS", 2, False, False)
        self.nat = MeAttribute("NAT", 1, False, False)
        self.ip_mode = MeAttribute("IP MODE", 1, False, False)
        self.qos_enable = MeAttribute("QoS Enable", 1, False, False)
        self.conect_status = MeAttribute("Conect Status", 1, False, False)
        self.gem_port_point = MeAttribute("GEM PORT POINT", 2, False, False)
        self.dhcp_remote_id = MeAttribute("DHCP REMOTE ID", 10, False, False)
        self.active_flag = MeAttribute("ACTIVE FLAG", 1, False, False)

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
    

class WanConfigFh:
    def __init__(self):
        self.proxy_enable = MeAttribute("Proxy Enable", 1, False, False)
        self.userppoe1 = MeAttribute("Userppoe1", 16, False, False)
        self.userppoe2 = MeAttribute("Userppoe2", 16, False, False)
        self.passwordppoe1 = MeAttribute("Passwordppoe1", 16, False, False)
        self.passwordppoe2 = MeAttribute("Passwordppoe2", 16, False, False)
        self.service_name_1 = MeAttribute("Service Name 1", 16, False, False)
        self.service_name_2 = MeAttribute("Service Name 2", 16, False, False)
        self.dail_parther = MeAttribute("Dail Parther", 1, False, False)
        self.authentic_mode = MeAttribute("Authentic Mode", 1, False, False)
        self.auto_drop_time = MeAttribute("Auto Drop Time", 2, False, False)

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
    

class WanPortBindFh:
    def __init__(self):
        self.lan_bind = MeAttribute("LAN Bind", 1, False, False)
        self.ssid_bind = MeAttribute("SSID Bind", 1, False, False)

        self.attributes = (
            self.lan_bind,
            self.ssid_bind,
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
    

class WanWanProfileFh:
    def __init__(self):
        self.wan_ip_host_ip_addr = MeAttribute("WAN IP HOST IP ADDR", 4, False, False)
        self.wan_ip_host_mask = MeAttribute("WAN IP HOST MASK", 4, False, False)
        self.wan_ip_host_gateway = MeAttribute("WAN IP HOST Gateway", 4, False, False)
        self.wan_ip_host_primary_dns = MeAttribute("WAN IP HOST Primary DNS", 4, False, False)
        self.wan_ip_host_secondary_dns = MeAttribute("WAN IP HOST Secondary DNS", 4, False, False)
        self.wan_ip_host_static_ipv6 = MeAttribute("WAN IP HOST Static IPv6", 19, False, False)
        self.wan_ip_host_ipv6_gateway = MeAttribute("WAN IP HOST IPv6 Gateway", 19, False, False)
        self.wan_ip_host_ipv6_primary_dns_static_ipv6 = MeAttribute("WAN IP HOST IPV6 Primary DNS Static IPv6", 19, False, False)
        self.wan_ip_host_ipv6_secondary_dns_static_ipv6 = MeAttribute("WAN IP HOST IPV6 Secondary DNS Static IPv6", 19, False, False)
        self.wan_ip_host_wan_protocol = MeAttribute("WAN IP HOST WAN Protocol", 1, False, False)
        self.wan_ip_host_static_prefix = MeAttribute("WAN IP HOST Static Prefix", 19, False, False)
        self.wan_ip_host_prefix_pool = MeAttribute("WAN IP HOST Prefix Pool", 19, False, False)
        self.wan_ip_host_address_source = MeAttribute("WAN IP HOST Address Source", 1, False, False)
        self.wan_ip_host_mac_address_source = MeAttribute("WAN IP HOST MAC Address Source", 6, False, False)

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
    

class WifiGeneralConfig:
    def __init__(self):
        self.wifi_std = MeAttribute("wifi_std", 2, False, False)
        self.wifi_auth = MeAttribute("wifi_auth", 2, False, False)
        self.wifi_cryp = MeAttribute("wifi_cryp", 2, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.wifi_pass = MeAttribute("wifi_pass", 25, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.wifi_ssid = MeAttribute("wifi_ssid", 25, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.wifi_enabled = MeAttribute("wifi_enabled", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 2, False, False)

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
    

class WifiAdvanceConfig:
    def __init__(self):
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.wifi_channel = MeAttribute("wifi_channel", 1, False, False)
        self.wifi_tx_pwr = MeAttribute("wifi_tx_pwr", 1, False, False)
        self.wifi_country = MeAttribute("wifi_country", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.wifi_freq_bandwidth = MeAttribute("wifi_freq_bandwidth", 1, False, False)

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
    

class WanExtendedVlanFh:
    def __init__(self):
        self.vlan_mode = MeAttribute("VLAN Mode", 1, False, False)
        self.tranlation_enable = MeAttribute("Tranlation Enable", 1, False, False)
        self.tranlation__vid = MeAttribute("Tranlation  VID", 2, False, False)
        self.vlan_cos = MeAttribute("VLAN CoS", 2, False, False)
        self.qinq_enable = MeAttribute("QinQ Enable", 1, False, False)
        self.vlan_tpid = MeAttribute("VLAN TPID", 2, False, False)
        self.slan_id = MeAttribute("SLAN ID", 2, False, False)
        self.slan_cos = MeAttribute("SLAN CoS", 2, False, False)

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
    

class OnuCapability:
    def __init__(self):
        self.operator_id = MeAttribute("operator_id", 4, False, False)
        self.ctc_spec_version = MeAttribute("ctc_spec_version", 1, False, False)
        self.onu_type = MeAttribute("onu_type", 1, False, False)
        self.onu_tx_power_supply_control = MeAttribute("onu_tx_power_supply_control", 1, False, False)

        self.attributes = (
            self.operator_id,
            self.ctc_spec_version,
            self.onu_type,
            self.onu_tx_power_supply_control,
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
    

class LoidAuthentication:
    def __init__(self):
        self.operator_id = MeAttribute("operator_id", 4, False, False)
        self.loid = MeAttribute("loid", 24, False, False)
        self.password = MeAttribute("password", 12, False, False)
        self.authentication_status = MeAttribute("authentication_status", 1, False, False)

        self.attributes = (
            self.operator_id,
            self.loid,
            self.password,
            self.authentication_status,
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
    

class Default:
    def __init__(self):
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)
        self.not_identified = MeAttribute("Not_identified", 1, False, False)

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
    