# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring Basic Interface Parameters [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html`
**Tags:** interfaces, ethernet, port-channels, switchport

---

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring Basic Interface Parameters [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
- [#fw-content] Skip to content 
- [#] Skip to search 
- [#fw-footer-v2] Skip to footer 

- [https://www.cisco.com/site/us/en/index.html] 
- [/c/en/us/products/index.html] 
- [https://www.cisco.com/site/us/en/solutions/index.html] 
- [/c/en/us/support/index.html] 
- [/c/en/us/training-events.html] 
- [www.cisco.com/c/en/us/about/sitemap.html] 
- [/c/en/us/buy.html] 
- [https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129] 
- [https://www.cisco.com/site/us/en/partners/cisco-partner-program/index.html?ccid=cc000864&dtid=odiprc001129] 
- [https://www.cisco.com/site/us/en/partners/support-help/index.html] 
- [https://www.cisco.com/site/us/en/partners/tools/index.html?dtid=odiprc001129] 
- [https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/] 
- [https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html?ccid=cc000864&dtid=odiprc001129] 
- [https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129] 	 

- [#] 
- [/c/en/us/index.html] 
- [/c/en/us/support/index.html] 
- [/c/en/us/support/all-products.html] 
- [/c/en/us/support/switches/category.html] 
- [/c/en/us/support/switches/nexus-9000-series-switches/series.html] 
- [/c/en/us/support/switches/nexus-9000-series-switches/products-installation-and-configuration-guides-list.html] 		 
# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x)
 		 	 Bias-Free Language 
### Bias-Free Language
 

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html] Learn more about how Cisco is using Inclusive Language.
 Book Contents Book Contents 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_preface_00.html] Preface 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01.html] New and Changed Information 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html] Overview 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html] Configuring Basic Interface Parameters 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0100.html] Configuring Layer 2 Interfaces 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html] Configuring Layer 3 Interfaces 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01111.html] Configuring Bidirectional Forwarding Detection 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html] Configuring Port Channels 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01000.html] Configuring vPCs 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01001.html] Configuring IP Tunnels 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html] Configuring Q-in-Q VLAN Tunnels 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01011.html] Configuring Static and Dynamic NAT Translation 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01100.html] Configuring IP Event Dampening 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01101.html] Configuring IP TCP MSS 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/m-n9000-configuring-unidirectional-ethernet.html] Configuring Unidirectional Ethernet 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_01110.html] Configuring Layer 2 	 Data Center Interconnect 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_01111.html] IETF RFCs supported 	 by Cisco NX-OS Interfaces 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_010000.html] Configuration Limits 	 for Cisco NX-OS Interfaces 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.65 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.pdf] PDF - This Chapter (1.45 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: March 28, 2022 
## Chapter: Configuring Basic Interface Parameters 
 Chapter Contents 
 
- [#id_114491] Configuring Basic Interface Parameters 
- [#concept_0B930AE86C97419F98C15D89121CBBBE] About the Basic Interface Parameters 
 
- [#concept_0DCFD637E96C4ED6842AF4C98B33D04A] Interface descriptions 
- [#concept_9F4D72E8673E482D8FB0881DB4EB9554] Beacon mode 
- [#concept_B279E7CC6BC04683BE07B09298887229] Error-disabled states 
- [#id_110777] MDIX parameters 
- [#concept_484B6DD874FF458A95AF4658338397FE] Interface status error policies 
- [#concept_5B90A64021804159B716BE57A235B802] Interface MTU sizes 
- [#concept_C9C4EE531F9D45379C22F8436F3D8E43] Bandwidth 
- [#concept_7BA47ADAD4874EF5ACC6D4316B256B79] Throughput-delayp values 
- [#concept_5A5040445413471F8544910B22CC94AD] Administrative status parameters 
- [#concept_428CC8BAC2454A7880339458411C78AC] Unidirectional Link Detection 
 
- [#concept_2039349BEACD4076BC82A9798AC467DA] UDLD 
- [#concept_94AD058EE20B45A7A4306540BE4283FE] Default UDLD configuration states 
- [#concept_4B7F3B4E7E6446CA81C65DDB1AB220EF] UDLD normal and aggressive modes 
- [#concept_597E1725831A4454BE80EBADC487691D] Port channels 
- [#concept_E67D9E2BEF694CADB57A5EC68B7BEF75] Port 	 Profiles 
- [#concept_A0972EE64EEB405A978EB90D2420D970] Cisco QSFP+ to SFP+ adapter modules 
- [#id_32705] Cisco SFP+ adapter modules 
- [#Cisco_Concept.dita_f6613a1e-8769-49b5-b21f-db076d2c5c69] Cisco SFP-10G-T-X modules 
- [#id_75899] Guidelines and Limitations 
- [#retimer-ports] Retimer ports 
- [#concept_EF93D0DD1E9B4C868735F14B12AC4B47] Default settings for interface parameters 
- [#concept_9AAF5FBC90A94E3FA1FF51CACE8F4DFD] Configure the basic interface parameters 
 
- [#task_214DA7157EAE465592F9103B4F66EF01] Specify the interfaces for configuration 
- [#task_2A4C7405B4224B5A95CDCDFE09D70508] Add description parameters to interfaces 
- [#task_2F7BEE7CB9604E5A9CE22F59A868378D] Enable beacon mode for an Ethernet port 
- [#concept_DA92494467F740FEA14182DF17FF435B] Configure the error-disabled state 
 
- [#task_DF90090DDB9F42788DC75B387543DB82] Enable the error-disable detection 
- [#task_5C633E9A6FC34B788D2CA7688E7A93AB] Recover an interface from error-disabled state 
- [#task_B504FA1F21CE464B9A1D956BBC6DE03D] Set the error-disabled recovery interval for interfaces 
- [#id_110778] Configure MDIX parameters 
- [#Cisco_Task.dita_465f2b68-ba30-49a3-9fd6-471fbb9a6ecf] Configure media-type for SFP-10G-T-X transceivers 
- [#Cisco_Concept.dita_6448d50d-1347-4e58-9976-07f9347f50a9] Verify media-type 
- [#concept_1C94AC4B56CC4621AEE1642039AD496A] Set MTU size 
 
- [#task_B7C698CB3AB044E8A1D6A7DDF51CF1F2] Configure MTU size for interfaces 
- [#id_114490] Set the system jumbo MTU size 
- [#task_467BE90B278D4A3EA0A669CD7CDB8D58] Configure the bandwidth for Ethernet interfaces 
- [#task_375CED713076446FAC2E142088171CA0] Set the throughput delay interval 
- [#task_7EDD79C1265F48EF839295084611F53E] Shut down and activate interfaces 
- [#task_C154B51D06434F0EBC6E55D4E00BEC62] Enable UDLD modes on interfaces 
- [#task_6414C84081D3492E9817031E9362DEC1] Configure debounce timers for Ethernet ports 
- [#concept_05CD1F6650A44B71A4F665EA9C25B3EA] Configuring Port 	 Profiles 
 
- [#task_949680A841F24707ABC0E320AA79DC47] Creating a Port 	 Profile 
- [#task_3D3FDFA8E7264EC0BCC9677BD0A9BDFB] Entering 	 Port-Profile Configuration Mode and Modifying a Port Profile 
- [#task_8265D9D4AB9E4DE79B6C963B2F0427C8] Assigning a Port 	 Profile to a Range of Interfaces 
- [#task_532B9110C5E74AE2A8272249F8999922] Enabling a Specific 	 Port Profile 
- [#task_1479561618D44C30A2651F7929898F02] Inheriting a Port Profile 
- [#task_0CF9650AEEE1411AA4751FF18BA67D0D] Removing a Port 	 Profile from a Range of Interfaces 
- [#task_3BF33AE3FAF9468BA83153D2A34A22B5] Removing an 	 Inherited Port Profile 
- [#task_t11_p41_ntb] Configure a link MAC-up timer on DWDM or Dark fiber circuits 
- [#id_77483] Configuring 25G Autonegotiation 
 
- [#id_78496] Guidelines and Limitations for 25G Autonegotiation 
- [#id_79207] FEC selection with 25G Autonegotiation 
- [#id_77446] Enable Autonegotiation on interfaces 
- [#id_77448] Disable Autonegotiation on the interfaces 
- [#concept_1D6528CB559F46E88EC9F78D5D137A39] Commands for viewing basic interface parameters 
- [#concept_2993C4CDCEB34F85B4EA562AC4F4849D] Monitor interface counters 
 
- [#task_78182D31B36A44409758FE96B65AC700] Configure sampling intervals for statistics 
- [#task_9EE9E21BEEF04CB89DE0C4F157ACD6B6] Clear the interface counters 
- [#concept_EB5C70B16BE94F34B51CEB1DB2062CCF] Example: Configuring QSA on Cisco Nexus 9396PX switch Close 
# Configuring Basic Interface Parameters
 

- [#concept_0B930AE86C97419F98C15D89121CBBBE] 
- [#id_75899] 
- [#retimer-ports] 
- [#concept_EF93D0DD1E9B4C868735F14B12AC4B47] 
- [#concept_9AAF5FBC90A94E3FA1FF51CACE8F4DFD] 
- [#concept_1D6528CB559F46E88EC9F78D5D137A39] 
- [#concept_2993C4CDCEB34F85B4EA562AC4F4849D] 
- [#concept_EB5C70B16BE94F34B51CEB1DB2062CCF] 
## About the Basic Interface Parameters
 

- [#concept_0DCFD637E96C4ED6842AF4C98B33D04A] 
- [#concept_9F4D72E8673E482D8FB0881DB4EB9554] 
- [#concept_B279E7CC6BC04683BE07B09298887229] 
- [#id_110777] 
- [#concept_484B6DD874FF458A95AF4658338397FE] 
- [#concept_5B90A64021804159B716BE57A235B802] 
- [#concept_C9C4EE531F9D45379C22F8436F3D8E43] 
- [#concept_7BA47ADAD4874EF5ACC6D4316B256B79] 
- [#concept_5A5040445413471F8544910B22CC94AD] 
- [#concept_428CC8BAC2454A7880339458411C78AC] 
- [#concept_597E1725831A4454BE80EBADC487691D] 
- [#concept_E67D9E2BEF694CADB57A5EC68B7BEF75] 
- [#concept_A0972EE64EEB405A978EB90D2420D970] 
- [#id_32705] 
- [#Cisco_Concept.dita_f6613a1e-8769-49b5-b21f-db076d2c5c69] 
### Interface descriptions
 

An interface description is a configuration attribute that
 
 
- 

assigns a recognizable name to an Ethernet or management interface,
 
- 

enables quick identification of the interface in listings with multiple interfaces, and
 
- 

allows unique labeling to distinguish individual interface roles or purposes.
 

To set the description parameter for a port-channel interface, see the “Configuring a Port-Channel Description” section. 
 

To set the description parameter for other interfaces, see the “Configuring the Description” section.
 
### Beacon mode
 

Beacon mode is a port identification feature that
 
 
- 

activates the port’s link-state LED to flash green for identification,
 
- 

is disabled by default, and
 
- 

is enabled by setting the beacon parameter on an interface.
 

You can use beacon mode to easily locate a physical port on a device during installation or troubleshooting. When activated, the corresponding port's LED flashes green, indicating the exact interface. This simplifies tasks such as cable tracing or port verification in complex environments. 
 

To identify the physical port for an interface, activate the beacon parameter for the interface.
 

For information on configuring the beacon parameter, see “Configuring the Beacon Mode” section.
 
### Error-disabled states
 		 			 				 

An error-disabled state is an operational port state that
 				 
 					 
- 						 

occurs when a port is administratively enabled, but disabled at runtime due to a detected problem,
 					 					 
- 						 

results from automated protection mechanisms (such as UDLD detecting unidirectional links or excessive port flapping), and
 					 					 
- 						 

requires manual intervention or specific recovery configuration to restore normal operation.
 					 				 			 			 
#### Additional information 
 				 				 

A port enters the error-disabled (err-disabled) state when it is enabled administratively using the 						no shutdown 					 command, but is disabled at runtime by any process. 
 				 

When an interface is in the err-disabled state, use the 						show interface status err-disabled 					 					 command to find information about the error. 
 				 

For example, if UDLD detects a unidirectional link, the port is shut down at runtime. However, because the port is administratively enabled, the port status displays as err-disable. 
 				 

Once a port goes into the err-disable state, you must manually reenable it or you can configure a timeout value that provides an automatic recovery. 
 				 
 

**Note**
 					 

By default, the automatic recovery is not configured, and the err-disable detection is enabled for all causes. 
 				 
 			 			 
#### Automatic error-disabled recovery
 				 				 

You can configure the automatic error-disabled recovery timeout for a particular error-disabled cause and configure the recovery period. 
 				 

The 						errdisable recovery cause 					 					 command provides an automatic recovery after 300 seconds. 
 				 

You can use the 						errdisable recovery interval 					 					 command to change the recovery period within a range of 30 to 65535 seconds. You can also configure the recovery timeout for a particular err-disable cause. 
 				 

If error-disabled recovery is not enabled for the cause, the interface remains in error-disabled state until you enter the 						shutdown 					 					 and 						no shutdown 					 commands. 
 				 

If the recovery is enabled for a cause, the interface is brought out of the error-disabled state and allowed to retry operation once all the causes have timed out. 
 			 		 		 			 
#### Guidelines
 				 				 
 					 				 			 		 	 
### MDIX parameters
 

A medium-dependent interface crossover (MDIX) parameter is an interface configuration setting that
 
 
- 

enables or disables automatic detection of crossover connections between network devices,
 
- 

applies only to copper network interfaces, and
 
- 

defaults to enabled status, ensuring compatibility without manual wiring considerations.
 

The no mdix auto command is supported only on N9K-C93108TC-EX, N9K-C93108TC-FX, N9K-X9788TC-FX, and N9K-C9348GC-FXP devices. 
 

For information about configuring the MDIX parameter, see the [#id_110778] Configuring the MDIX Parameter section. 
 
### Interface status error policies
 

An interface status error policy is a network policy enforcement mechanism that
 
 
- 

prevents interfaces from being activated if a policy push fails,
 
- 

stores error state information to avoid repeated disruptions, and
 
- 

ensures policy and hardware configuration consistency.
 

Cisco NX-OS policy servers, such as Access Control List (ACL) Manager and Quality of Service (QoS) Manager, maintain a policy database where each policy is defined through the command-line interface. 
 

When you configure an interface with a policy, the system ensures that the policy matches the hardware policies. If a policy is pushed that does not match hardware policy, the interface is set to an error-disabled policy state. The error state persists and information is stored to prevent the port from being brought up in the future, avoiding repeated policy violations and system disruption. 
 

To clear the error and retry the programming, use the no shutdown command. 
 
### Interface MTU sizes
 

A maximum transmission unit (MTU) size is a network interface parameter that
 
 
- 

determines the largest frame size an Ethernet port can process,
 
- 

enforces the drop of frames exceeding the configured size.
 

**Additional information**
 

By default, each interface uses an MTU of 1500 bytes, matching the IEEE 802.3 standard for Ethernet frames.
 

Larger MTU sizes, called jumbo frames, improve processing efficiency. Jumbo frames are typically up to 9216 bytes.
 

Cisco NX-OS platforms allow MTU adjustment per interface or at different levels in the protocol stack.
 

CloudScale switches allow an extra 166 bytes above the configured MTU (by default) to accommodate additional encapsulations in hardware. 
 
 

**Note**
 

For transmissions to occur between two ports, you must configure the same MTU size for both ports. A port drops any frames that exceed its MTU size. 
 
 

**MTU configuration by interface type **
 

MTU is configured per interface. An interface can be a Layer 2 or a Layer 3 interface.
 
 
- 

**Layer 2 interfaces**
 

You can configure the MTU size with one of two values: the system default MTU value or the system jumbo MTU value.
 

The system default MTU value is 1500 bytes. Each Layer 2 interface uses this value by default. You can configure an interface with the default system jumbo MTU value, that is 9216 bytes. 
 

To allow an MTU value from 1500 through 9216, first set the system jumbo MTU. Then, align interface MTUs accordingly.
 
 

**Note**
 

You can change the system jumbo MTU size. When the value is changed, the Layer 2 interfaces that use the system jumbo MTU value, automatically changes to the new system jumbo MTU value. 
 
 
- 

**Layer 3 interfaces**
 

Layer 3 interfaces include the Layer 3 physical interface (configured with no switchport), switch virtual interface (SVI), and sub-interface. You can configure their MTU size between 576 and 9216 bytes. 
 

For information about setting the MTU size, see the *Configuring the MTU Size* section. 
 
#### Guidelines
 
 
- 

Use these MTU guidelines for the Cisco Nexus 9372 switch.
 
 
- 

The 10G interfaces are mapped to specific hardware ports where the default MTU is 1500.
 
- 

The 40G interfaces are mapped as a HiGiG port where the default MTU is 3FFF and the MTU limit check is disabled.
 
- 

In the case of 40G interfaces, since the MTU limit check is disabled, it ignores the packet size and traffic flows regardless of its MTU. 
 
- 

f you configure different MTU sizes for interfaces on the switch, behavior varies based on which port is mismatched and the traffic flow. 
 
- 

If you configure an ingress interface with an MTU less than 9216 on Cisco Nexus 9300-FX2 and 9300-GX devices, FTE does not capture input errors or display events. If you set the ingress MTU to 9216, FTE displays all events. 
 
#### Examples
 

These examples describe the behavior of the switch in various scenarios.
 
 
- 

**Layer 3 port examples**
 

When a Layer 3 port receives a frame whose length exceeds the port's MTU size, the port drops the frame.
 

When a Layer 3 port receives a frame whose length is less than the ingress port's MTU size, but greater than the egress Layer 3 port's MTU size, then the frame is punted to the supervisor of the switch. 
 

If the frame is an IP packet that has the **Don't Fragment (DF)** bit set, then the frame is dropped in software. Otherwise, the frame is fragmented in software. 
 

This may cause performance issues (such as increased latency or packet loss for affected traffic flows) due to Control Plane Policing (CoPP) enabled by default on Cisco Nexus switches. For more information about Control Plane Policing, see, Cisco Nexus 9000 Series NX-OS Security Configuration Guide. 
 
- 

**Layer 2 port examples**
 

When a Layer 2 port receives a frame whose length exceeds the port's MTU size, the port drops the frame.
 

When a Layer 2 port receives a frame whose length is less than the ingress port's MTU size, but greater than the egress Layer 2 port's MTU size, and the frame is routed between VLANs by the switch, then the frame is punted to the supervisor of the switch. 
 

If the frame is an IP packet that has the **Don't Fragment (DF)** bit set, then the frame is dropped in software. Otherwise, the frame is fragmented in software. 
 

This may cause performance issues (such as increased latency or packet loss for affected traffic flows) due to Control Plane Policing (CoPP) enabled by default on Cisco Nexus switches. For more information, see Cisco Nexus 9000 Series NX-OS Security Configuration Guide. 
 
- 

When a Layer 2 port receives a frame whose length is less than the ingress port's MTU size, but greater than the egress Layer 2 port's MTU size, and the frame is switched within the same VLAN by the switch, then the switch forwards the truncated frame. 
 
### Bandwidth
 

Bandwidth is a network performance metric that
 
 
- 

measures the maximum data transfer rate of a network connection,
 
- 

defines the capacity of a link between devices, and
 
- 

remains fixed at the physical layer for Ethernet ports (for example, 1,000,000 Kb).
 

On Ethernet ports, the physical bandwidth is always fixed (such as 1,000,000 Kb). Layer 3 protocols use a configurable bandwidth value solely for internal metric calculations. Modifying this parameter affects only the routing protocol’s behavior and does not physically alter the connection’s capacity. 
 

For example, the Enhanced Interior Gateway Routing Protocol (EIGRP) uses the minimum path bandwidth to determine a routing metric, but the bandwidth at the physical layer remains at 1,000,000 Kb. 
 

For information about configuring the bandwidth parameter, see the [#task_467BE90B278D4A3EA0A669CD7CDB8D58] Configuring the Bandwidth. 
 
### Throughput-delayp values
 

Throughput-delay is an interface configuration parameter that
 
 
- 

provides a value used by Layer 3 protocols to make operating decisions,
 
- 

does not affect the actual throughput delay of an interface, and
 
- 

is specified in tens of microseconds.
 

For example, the Enhanced Interior Gateway Routing Protocol (EIGRP) can use the delay setting to set a preference for one Ethernet link over another, if other parameters such as link speed are equal. The delay value is specified in the tens of microseconds. 
 

For information on configuring the throughput-delay parameter for other interfaces, see [#task_375CED713076446FAC2E142088171CA0] Configuring the Throughput Delay. 
 
### Administrative status parameters
 

An administrative status parameter is a network interface setting that:
 
 
- 

indicates whether an interface is administratively up or down,
 
- 

enables or disables the ability of the interface to transmit data.
 

When the administrative status is set to down, the interface is disabled and cannot transmit data. When set to up, the interface is enabled. 
 

For information about configuring the administrative status parameter for port-channel interfaces, see the “Shutting Down and Restarting the Port-Channel Interface” section. 
 

For information about configuring the administrative status parameter for other interfaces, see the “Shutting Down and Activating the Interface” section. 
 
### Unidirectional Link Detection
 

- [#concept_2039349BEACD4076BC82A9798AC467DA] 
- [#concept_94AD058EE20B45A7A4306540BE4283FE] 
- [#concept_4B7F3B4E7E6446CA81C65DDB1AB220EF] 
#### UDLD
 

Unidirectional Link Detection (UDLD) is a network protocol that
 
 
- 

monitors the physical configuration of fiber and copper Ethernet cables between connected devices,
 
- 

detects the presence of unidirectional links on these connections, and
 
- 

automatically shuts down affected LAN ports to prevent network problems.
 

UDLD is a Cisco-proprietary protocol designed to identify and mitigate issues that occur when traffic passes in only one direction on a connection—known as a unidirectional link. Such conditions can create network loops and cause data loss or protocol malfunctions. 
 

The Cisco Nexus 9000 Series device periodically transmits UDLD frames to neighbor devices on LAN ports with UDLD enabled. If the frames are echoed back within a specific time frame but lack an acknowledgment (echo), the link is flagged as unidirectional. The LAN port is then shut down. 
 

Both ends of the link must support UDLD for the protocol to identify and disable unidirectional links. You can configure the transmission interval for the UDLD frames globally or for the specified interfaces. 
 

**Additional information**
 

UDLD performs tasks that autonegotiation cannot perform, such as detecting the identities of neighbors and shutting down misconnected LAN ports. 
 

When you enable both autonegotiation and UDLD, Layer 1 detections work to prevent physical and logical unidirectional connections and the malfunctioning of other protocols. 
 

A unidirectional link occurs when traffic sent by the local device is received by the neighbor, but traffic from the neighbor is not received by the local device. 
 

If one of the fiber strands in a pair is disconnected and autonegotiation is active, the link does not remain up. In this case, the logical link is undetermined, and UDLD does not take any action. If both fibers work normally at Layer 1, UDLD checks whether they are connected correctly and whether traffic flows bidirectionally between the correct neighbors. This check cannot be performed by autonegotiation, because autonegotiation operates at Layer 1. 
 
 

**Note**
 

By default, UDLD is locally disabled on copper LAN ports to avoid sending unnecessary control traffic on this type of media. 
 
 
##### Example
 

Device A and Device B are connected with fiber-optic cables. Due to a cable break, Device B can receive traffic from Device A, but Device A cannot receive traffic from Device B. UDLD detects this unidirectional condition and disables the affected port, preventing network issues. 
 Figure 1. Unidirectional Link 
##### Analogy
 

UDLD is like a two-way conversation in which both participants regularly confirm they can hear each other. If one participant stops responding, the conversation is paused to prevent misunderstandings—just as UDLD disables a port if bidirectional communication fails. 
 
#### Default UDLD configuration states
 

UDLD configuration state is a system-defined setting that
 
 
- 

specifies whether UDLD operates globally or on specific ports,
 
- 

determines if UDLD runs in standard or aggressive mode, and
 
- 

controls the message interval for UDLD protocol operation.
 

UDLD applies different defaults depending on port media type.
 
 
- 

On Ethernet fiber-optic ports, UDLD is enabled by default.
 
- 

On Ethernet twisted-pair (copper) ports, UDLD is disabled by default. You must enable UDLD if you want to use it. 
 
##### UDLD default configuration states
 

The table shows the default UDLD configuration.
 
 Table 1. UDLD default configuration states 

Feature
 

Default Value
 

UDLD global enable state
 

Globally disabled 
 

UDLD per-port enable state for fiber-optic media
 

Enabled on all Ethernet fiber-optic LAN ports
 

UDLD per-port enable state for twisted-pair (copper) media 
 

Disabled on all Ethernet 10/100 and 1000BASE-TX LAN ports 
 

UDLD aggressive mode
 

Disabled
 

UDLD message interval
 

15 seconds
 
 

For information about configuring the UDLD for the device and its port, see the “Configuring the UDLD Mode” section.
 
#### UDLD normal and aggressive modes
 

The UDLD mode monitors links and determines how to detect and respond to unidirectional link failures.
 

You can use UDLD in normal mode or aggressive mode. 
 
 
- 

Normal mode: UDLD normal mode exchanges packets between peers ports to detect link health. 
 
- 

Aggressive mode: UDLD aggressive mode attempts to re-establish contact with an unresponsive neighbor. If, after eight retries, the link remains unresponsive, UDLD aggressively disables the affected port to prevent undetected one-way faults from causing network issues. 
 
##### Additional information
 

When the switch detects link errors such as an empty echo packet, unidirectional failure, TX or RX loop, or neighbor mismatch, it flags the condition but might not disable the port. 
 

UDLD operates in normal mode by default, and aggressive mode is disabled unless you enable it.
 

When you enable UDLD aggressive mode globally, it activates on all fiber ports. You can also activate on a specific individual fiber port. 
 
 

**Note**
 

You must configure it on individual copper interfaces.
 
 

Use UDLD aggressive mode only between network devices that both support it. Use this mode only on point-to-point links.
 

In these scenarios, UDLD aggressive mode disables a port to prevent traffic loss.
 
 
- 

One side of a link has a stuck port (both transmission and receive) 
 
- 

One side of a link remains up while the other side of the link is down 
 
##### Guidelines
 
 
- 

If you upgrade a line card during an ISSU, and some ports are part of a Layer 2 port channel with UDLD aggressive mode enabled, shutting down a remote port causes UDLD to place the local port in error-disabled state. This is the expected behavior. 
 

To restore service after the ISSU has completed, enter the shutdown command followed by the no shutdown command on the local port. 
 
### Port channels
 		 			 				 				 

A port channel is a logical interface that
 				 
 					 
- 						 

combines multiple physical interfaces to increase aggregate bandwidth,
 					 					 
- 						 

provides redundancy by remaining operational as long as at least one member interface is active, and
 					 					 
- 						 

balances traffic across the participating physical interfaces to optimize network performance.
 					 				 				 

Port channeling also load balances traffic across these physical interfaces. The port channel remains operational as long as at least one physical interface within the channel is active 
 				 

**Additional information**
 				 

You can create Layer 3 port channels by bundling compatible Layer 3 interfaces.
 				 

Any configuration changes made to a port channel are automatically applied to each member interface within that channel.
 				 

For information about port channels, see Chapter 6, "Configuring Port Channels".
 			 		 	 
### Port 	 Profiles 
 

 On Cisco Nexus 9300 Series switches, you can create a port profile that contains many interface commands and apply that port profile to a range of interfaces. Each port profile can be applied only to a specific type of interface; the choices are as follows: 
 
 
- 		 

Ethernet 		 
 		 
- 		 

VLAN network 			 interface 		 
 		 
- 		 

Port channel 		 
 		 

When you choose 		Ethernet or port channel as the interface type, the port profile is in the 		default mode which is Layer 3. Enter the 		switchport command to change the port profile to Layer 		2 mode. 	 
 

You inherit the port 		profile when you attach the port profile to an interface or range of 		interfaces. When you attach, or inherit, a port profile to an interface or 		range of interfaces, the system applies all the commands in that port profile 		to the interfaces. Additionally, you can have one port profile inherit the 		settings from another port profile. Inheriting another port profile allows the 		initial port profile to assume all of the commands of the second, inherited, 		port profile that do not conflict with the initial port profile. Four levels of 		inheritance are supported. The same port profile can be inherited by any number 		of port profiles. 	 
 

The system applies the 		commands inherited by the interface or range of interfaces according to the 		following guidelines: 	 
 
 
- 		 

Commands that you 			 enter under the interface mode take precedence over the port profile’s commands 			 if there is a conflict. However, the port profile retains that command in the 			 port profile. 		 
 		 
- 		 

The port profile’s 			 commands take precedence over the default commands on the interface, unless the 			 port-profile command is explicitly overridden by the default command. 		 
 		 
- 		 

When a range of 			 interfaces inherits a second port profile, the commands of the initial port 			 profile override the commands of the second port profile if there is a 			 conflict. 		 
 		 
- 		 

After you inherit 			 a port profile onto an interface or range of interfaces, you can override 			 individual configuration values by entering the new value at the interface 			 configuration level. If you remove the individual configuration values at the 			 interface configuration level, the interface uses the values in the port 			 profile again. 		 
 		 
- 		 

There are no 			 default configurations associated with a port profile. 		 
 		 			 

A subset of commands 		are available under the port-profile configuration mode, depending on which 		interface type you specify. 	 
 
 

**Note**
 		 

You cannot use port 		 profiles with Session Manager. See the 		 Cisco Nexus 			 9000 Series NX-OS System Management Configuration Guide for information 		 about Session Manager. 		 		 
 	 
 

To apply the 		port-profile configurations to the interfaces, you must enable the specific 		port profile. You can configure and inherit a port profile onto a range of 		interfaces prior to enabling the port profile. You would then enable that port 		profile for the configurations to take effect on the specified interfaces. 	 
 

 If you inherit one or 		more port profiles onto an original port profile, only the last inherited port 		profile must be enabled; the system assumes that the underlying port profiles 		are enabled. 	 
 

When you remove a port 		profile from a range of interfaces, the system undoes the configuration from 		the interfaces first and then removes the port-profile link itself. Also, when 		you remove a port profile, the system checks the interface configuration and 		either skips the port-profile commands that have been overridden by directly 		entered interface commands or returns the command to the default value. 	 
 

If you want to delete 		a port profile that has been inherited by other port profiles, you must remove 		the inheritance before you can delete the port profile. 	 
 

You can also choose a 		subset of interfaces from which to remove a port profile from among that group 		of interfaces that you originally applied the profile. For example, if you 		configured a port profile and configured ten interfaces to inherit that port 		profile, you can remove the port profile from just some of the specified ten 		interfaces. The port profile continues to operate on the remaining interfaces 		to which it is applied. 	 
 

If you delete a 		specific configuration for a specified range of interfaces using the interface 		configuration mode, that configuration is also deleted from the port profile 		for that range of interfaces only. For example, if you have a channel group 		inside a port profile and you are in the interface configuration mode and you 		delete that port channel, the specified port channel is also deleted from the 		port profile as well. 	 
 

Just as in the device, 		you can enter a configuration for an object in port profiles without that 		object being applied to interfaces yet. For example, you can configure a 		virtual routing and forward (VRF) instance without it being applied to the 		system. If you then delete that VRF and related configurations from the port 		profile, the system is unaffected. 	 
 

After you inherit a 		port profile on an interface or range of interfaces and you delete a specific 		configuration value, that port-profile configuration is not operative on the 		specified interfaces. 	 
 

If you attempt to 		apply a port profile to the wrong type of interface, the system returns an 		error. 	 
 

When you attempt to 		enable, inherit, or modify a port profile, the system creates a checkpoint. If 		the port-profile configuration fails, the system rolls back to the prior 		configuration and returns an error. A port profile is never only partially 		applied. 	 
 
### Cisco QSFP+ to SFP+ adapter modules
 		 			 				 				 

A Cisco QSFP+ to SFP+ adapter module (QSA) is a network interface accessory that
 				 
 					 
- 						 

enables the use of 10G SFP+ transceivers in 40G QSFP+ uplink ports,
 					 					 
- 						 

requires all ports in a designated speed group to operate at the same speed (either 10G or 40G).
 					 				 				 

The Cisco QSFP+ to SFP+ adapter (QSA) module enables 10G operation on 40G uplink ports within Cisco Nexus M6PQ and M12PQ uplink modules, which belong to specific Cisco Nexus 9300 devices 
 				 

To use QSA/QSFP modules, six consecutive ports in the M6PQ or M12PQ uplink module must operate at the same speed—either 10G or 40G. 
 				 			 			 
#### Supported platforms and port groups
 				 				 

These Cisco Nexus devices and port groups support the Cisco QSFP+ to SFP+ adapter module:
 				 
 					 
- 						 

Cisco Nexus 9396PX: 2/1–6 (first group), 2/7–12 (second group)
 					 					 
- 						 

Cisco Nexus 93128PX/TX: 2/1–6 (first group), 2/7–8 (second group)
 					 					 
- 						 

Cisco Nexus 937xPX/TX: 1/49–54 (only group)
 					 					 
- 						 

Cisco Nexus 93120TX: 1/97–102 (only group)
 					 					 
- 						 

Cisco Nexus 9332PQ: 1/27–32 (only group)
 					 				 			 		 		 			 
#### Configuring port speed for QSA modules
 				 				 

Use the 						speed-group 10000 					 					 command to configure the first port of a port speed group to set all ports in the group to 10G. The default port speed is 40G. 
 				 

The 						no speed-group 10000 					 command specifies a speed of 40G. 
 				 
 					 					 
- 						 

 Do not remove uplink modules from a Cisco Nexus 9300 platform switch that runs Cisco NX-OS Release 7.0(3)I7(5). Use the ports on uplink modules for uplinks only 
 					 					 
- 						 						 

Beginning with Cisco NX-OS Release 9.2(2), CWDM4 is supported on these line cards:
 						 
 							 
- 								 

36-port 100-Gigabit Ethernet QSFP28 line cards (N9K-X9636C-R)
 							 							 
- 								 

36-port 40-Gigabit Ethernet QSFP+ line cards (N9K-X9636Q-R),
 							 							 
- 								 

36-port 100-Gigabit QSFP28 line cards (N9K-X9636C-RX)
 							 							 
- 								 

52-port 100-Gigabit QSFP28 line cards (N9K-X96136YC-R)
 							 						 					 				 				 

After you configure the speed, the switch enables compatible transceiver modules. The switch disables incompatible modules and displays the message 'check speed-group' config. 
 				 
 

**Note**
 					 					 

The Cisco QSFP+ to SFP+ Adapter (QSA) module does not provide 10G support for the 40G line cards for Cisco Nexus 9500 devices. 
 					 					 

You can use a QSFP-to-SFP adapter on Cisco Nexus 9200 and 9300-EX Series switches and Cisco Nexus 3232C and 3264Q Series switches.
 				 
 			 		 	 
### Cisco SFP+ adapter modules
 

A Cisco SFP+ adapter module is a network interface device that
 
 
- 

enables high-speed connectivity by adapting SFP+ optics for use in higher-capacity switch ports,
 
- 

supports multiple Ethernet speeds (such as 10G and 25G) with manual or automatic speed configuration.
 

The interface breakout module command enables you to split a 100G interface into four 25G interfaces. After you enter this command, you must copy the running configuration to the startup configuration. 
 

Beginning with Cisco NX-OS Release 9.2(3), 10/25 LR is supported on N9K-C93180YC-EX, N9K-X97160YC-EX, N9K-C93180YC-FX, N9K-C93240YC-FX2 and N3K-C34180YC switches. 
 

This dual speed optical transceiver operates at 25G by default and interoperates with other 25G LR transceivers. Because auto speed sensing is not supported, to use this device with a 10G transceiver, configure it manually for 10G speed. 
 

The CVR-2QSFP28-8SFP adapter supports 25-Gigabit optics on 100-Gigabit ports of the Cisco Nexus 9236C switch. 
 
### Cisco SFP-10G-T-X modules
 

A Cisco SFP-10G-T-X module is a hot-swappable, 10 Gigabit Ethernet transceiver that
 
 
- 

provides 10GBASE-T connectivity over standard Category 6a or 7 copper cabling,
 
- 

supports RJ-45 connectors for interface flexibility, and
 
- 

enables up to 30-meter reach for data center and enterprise applications.
 

Starting with Cisco NX-OS Release 9.3(5), 10G BASE-T SFP+ (RJ-45) is supported on N9K-C93240YC-FX2, N9K-C93180YC-EX, N9K-C93180YC-FX and N9K-C93360YC-FX2 devices. 
 

By default, Cisco SFP-10G-T-X modules operate at 10G speeds.
 

When using a SFP-10G-T-X module, all neighboring ports must be either empty or must use passive copper links.
 

The show interface and show interface capability commands display supported speed for certain ports. 
 

The switch may display 100 Mbps as a supported speed for certain ports when using the SFP-10G-T-X transceiver. For GLC-TE transceivers, the lowest supported speed is 1 Gbps. 
 

An interface configured with media-type 10G-TX, while in the admin up state, remains error-disabled when using an unsupported media-type. To resolve this condition, enter these commands on the interface: 
 
 
- 

 shutdown 
 
- 

 no shutdown 
 

The table shows the default port mapping for various Cisco Nexus switches.
 
 Table 2. Default Port Mapping 

Device Name
 

Port Map
 

Cisco Nexus N9K-C93180YC-EX, N9K-C93180YC-FX, N9K-C93180YC-FX3 and N9K-C93180YC-FX3S 
 

PI/PE: 1, 4-5, 8-9, 12-13, 16, 37, 40-41, 44-45, 48
 

Cisco Nexus N9K-C93240YC-FX2 
 

W/ PI Fan/PS: 2, 6, 8, 12, 14, 18, 20, 24, 26, 30, 
 

32, 36, 38, 42, 44, 48
 

W/ PE Fan/PS: 6, 12, 18, 24, 30, 36, 42, 48
 

Cisco Nexus N9K-C93360YC-FX2 
 

PI/PE 1, 4-5, 8, 41, 44-45, 48-49, 52-53, 56-57,
 

60-61, 64-65, 68-69, 72-73, 76-77, 80-81, 84-85, 
 

88-89, 92-93, 96
 
 
## Guidelines and Limitations
 

Basic interface parameters have the following configuration guidelines and limitations: 
 
 
- 

When connecting the Cisco N9K-C9348GC-FXP switch to a third-party (SRX4600 Firewall) firewall, if any switch port of Cisco N9K-C9348GC-FXP switch is connected to the console port of a network device, all ports connected to the firewall may experience link instability or may only establish at 10 Mbps. 
 
- 

MDIX is enabled by default on copper ports. It is not possible to disable it.
 
- 

 show commands with the internal keyword are not supported. 
 
- 

Fiber-optic Ethernet ports must use Cisco-supported transceivers. To verify that the ports are using Cisco-supported transceivers, use the show interface transceivers command. Interfaces with Cisco-supported transceivers are listed as functional interfaces. 
 
- 

A port can be either a Layer 2 or a Layer 3 interface; it cannot be both simultaneously. 
 

By default, each port is a Layer 3 interface. 
 

You can change a Layer 3 interface into a Layer 2 interface by using the switchport command. You can change a Layer 2 interface into a Layer 3 interface by using the no switchport command. 
 
- 

Flow control using pause frames is not supported. 
 
- 

Beginning with Cisco NX-OS Release 9.3(1), only MTU 9216 can be configured on FEX fabric ports. Trying to configure any other value generates an error. 
 

If the MTU value on a FEX fabric port-channel was set to 9216 before the switch was upgraded to Cisco NX-OS Release 9.3(1), the show running config command does not display the MTU value, but the show running-config diff command does. 
 
- 

Beginning with Cisco NX-OS Release 9.3(1), FEX fabric port-channels support only MTU 9216 by default. 
 
- 

The following line cards do not support Link Training:
 

Nexus 9300 Modules:
 
 
- 

N9K-M12PQ (C9396PX, C9396TX, C93128PX, C93128TX)
 

Nexus 9500 Modules:
 
 
- 

X9536PQ
 
- 

X9564PX 
 
- 

X9564TX 
 
- 

When you use a backslash (\) at end of a valid interface description, the parser identifies the backslash as a continuation character and appends an extra line break in command output by adding a new line character '\n' to the command string. This is a Day-1 behavior. 
 
- 

Cisco Nexus 9000 series EX TOR switches and line cards do not support RS-FEC, and CONS16-RS-FEC.
 
- 

On Cisco NX-OS Release 10.3(x) and 10.4(x), manually setting an interface speed to 100 Mbps on Nexus 9000 Series switches may prevent link establishment with certain non-Nexus devices that are also manually set to 100 Mbps. To avoid this issue, enable auto-negotiation on the remote device, or use an intermediate Layer 2 switch as a workaround if the remote configuration cannot be changed. 
 
### Support for QSA
 
 
- 

1 GB with QSA is not supported on Retimer Ports. For information on, see [#retimer-ports] Retimer ports.
 
- 

Beginning with Cisco NX-OS Release 9.2(2), 10 GB with QSA is supported on the following ports:
 
 
- 

Cisco Nexus 9336C-FX2 switch: Ports 1-36
 
- 

Cisco Nexus 9364C switch: Ports 49-64
 
- 

Cisco Nexus 9788TC line card: Ports 49-52
 
- 

Beginning with Cisco NX-OS Release 9.2(2), 1 GB with QSA is supported on the following ports:
 
 
- 

Cisco Nexus 9336C-FX2 switch: Ports 7-32
 
- 

Cisco Nexus 9364C switch: Ports 65 and 66 only
 
### Guidelines for ethernet port speed and duplex mode
 
 
- 

You usually configure Ethernet port speed and duplex mode parameters to auto to allow the system to negotiate the speed and duplex mode between ports. If you decide to configure the port speed and duplex modes manually for these ports, consider the following: 
 
 
- 

Before you configure the speed and duplex mode for an Ethernet or management interface, see the Default Settings section for the combinations of speeds and duplex modes that can be configured at the same time. 
 
- 

If you set the Ethernet port speed to auto, the device automatically sets the duplex mode to auto. 
 
- 

If you enter the no speed command, the device automatically sets both the speed and duplex parameters to auto (the no speed command produces the same results as the speed auto command). 
 
- 

If you configure an Ethernet port speed to a value other than auto (for example, 1G, 10G, or 40G), you must configure the connecting port to match. Do not configure the connecting port to negotiate the speed. 
 
- 

Beginning with Cisco NX-OS Release 9.3(6), Cisco Nexus N9K-C92348GC-X switches support 10M full-duplex mode on ports 1 through 48. 
 
 

**Note**
 

The device cannot automatically negotiate the Ethernet port speed and duplex mode if the connecting port is configured to a value other than auto. 
 
 
 

**Caution**
 

Changing the Ethernet port speed and duplex mode configuration might shut down and reenable the interface. 
 
 
- 

On Cisco Nexus 9000 Series Switches, the `show interface` and `show interface capability` commands may display 100 Mbps as a supported speed for certain ports. However, this speed is only supported when using the SFP-10G-T-X transceiver. For ports using GLC-TE transceivers, the lowest supported speed is 1 Gbps. 
 
### Support for autonegotiation
 
 
- 

Autonegotiation is not supported on 400G and 200G Copper links on these Nexus switches. Configure respective speed on the peer side to bring the link up. 
 
 

Nexus switch
 

Copper support (No autonegotiation)
 

Release
 

N9K-C93600CD-GX
 

400G
 

9.3(5)
 

N9K-C9316D-GX
 

400G
 

9.3(5)
 
 
- 

Autonegotiation is not supported when N9K-C93108TC-FX3P switch is connected to either of the following switches: 
 
 
- 

N9K-C9236C, N9K-C92300YC, N9K-C93180YC-EX, N9K-C93180YC-EXU, N9K-C9232C, N9K-C92300YC, and N9K-C93180YC-FX. 
 
- 

N3K-C3172TQ-XL, N3K-C3172TQ-10GT, N3K-C3172PQ-10GE, and N3K-C3132Q-40GE.
 
- 

Beginning with Cisco NX-OS Release 9.2(2), autonegotiation (40 G/100 G) is supported on the following ports: 
 
 
- 

Cisco Nexus 9336C-FX2 switch: Ports 1-6 and 33-36
 
- 

Cisco Nexus 9364C switch: Ports 49-64
 
- 

Cisco Nexus 93240YC-FX2 switch: Ports 51-54
 
- 

Cisco Nexus 9788TC line card: Ports 49-52
 
- 

Beginning with Cisco NX-OS Release 9.2(1), autonegotiation on native 25G ports is supported on Cisco Nexus N9K-X97160YC-EX, N9K-C93180YC-FX, N9K-C93240YC-FX2 and N9K-C93240YC-FX2-Z switches. 
 
- 

Autonegotiation is not supported on Cisco Nexus N9K-C92300YC switch.
 
- 

Autonegotiation is not supported on 25G breakout ports.
 
- 

If cable length is more than 5 meters, autonegotiation is not supported. This cable length limitation is applicable only to copper cables and not applicable to optical cables. 
 
- 

To configure speed, duplex, and automatic flow control for an Ethernet interface, you can use the negotiate auto command. To disable automatic negotiation, use the no negotiate auto command. 
 
 
- 

For BASE-T copper ports, autonegotiation is enabled even when fixed speed is configured. 
 
## Retimer ports
 

Retimer ports are specialized hardware interfaces you can use on certain Nexus switches and line cards. These ports:
 
 
- 

improve signal integrity between the forwarding engine and front-panel ports,
 
- 

may provide additional features such as MACsec or SyncE capabilities, and
 
- 

may experience slightly longer link-up times depending on speed, optics, cable, and link partner characteristics.
 

Retimer ports may experience longer link-up times depending on the negotiated speed, optics, transceiver, and cable used, as well as specific characteristics of the connected link partner. 
 

In most cases, retimer ports link up within a few seconds. Occasionally, link-up time may be higher depending on negotiated parameters and hardware used. 
 

The table lists Nexus switches and line cards that support retimer ports and identifies the specific ports on each device.
 
 Table 3. Supported retimer ports 

Switch or Line cards
 

Retimer Ports
 

N9K-X9788TC-FX
 

49-52
 

N9K-C93240YC-FX2
 

N9K-C93240YC-FX2-Z
 

51-54
 

N9K-C9336C-FX2
 

1-6, 33-36
 

N9K-C9364C
 

49-64
 

N9K-X96136YC-R
 

49-52
 

N9K-X9736C-FX
 

29-36
 

N9K-C9332C
 

25-32
 

N9K-C93180YC-FX3
 

1-54
 

N9K-C93216TC-FX2
 

N9K-C93360YC-FX2
 

97-108
 
 
## Default settings for interface parameters
 

The table shows the default settings for the basic interface parameters. 
 
 

Parameter 				 
 

Default 				 
 

Description 				 
 

Blank 				 
 

Beacon 				 
 

Disabled 				 
 

Bandwidth 				 
 

Data rate of 					 interface 				 
 

Throughput 					 delay 				 
 

100 					 microseconds 				 
 

Administrative status 				 
 

Shutdown 				 
 

MTU 				 
 

1500 bytes 				 
 

UDLD global 				 
 

Globally 					 disabled 				 
 

UDLD 					 per-port enable state for fiber-optic media 				 
 

Enabled on 					 all Ethernet fiber-optic LAN ports 				 
 

UDLD 					 per-port enable state for copper media 				 
 

Disabled on 					 all Ethernet 1G, 10G, or 40G LAN ports 				 
 

UDLD message 					 interval 				 
 

Disabled 				 
 

UDLD 					 aggressive mode 				 
 

Disabled 				 
 

Error 					 disable 				 
 

Disabled 				 
 

Error 					 disable recovery 				 
 

Disabled 				 
 

Error 					 disable recovery interval 				 
 

300 seconds 				 
 

Buffer-boost 					 				 
 

Enabled 				 
 
 

**Note**
  

This feature is available on N9K-X9564TX and N9K-X9564PX line cards and Cisco Nexus 9300 series devices. 
 
 
 
## Configure the basic interface parameters
 

Basic interface parameters are configuration elements that
 
 
- 

determine how your network interface operates in your device,
 
- 

specify essential settings such as IP address, duplex mode, and speed,
 
- 

and help you ensure proper connectivity and protocol compatibility on your network.
 

You must specify the interface before you can configure the parameters of the interface
 

- [#task_214DA7157EAE465592F9103B4F66EF01] 
- [#task_2A4C7405B4224B5A95CDCDFE09D70508] 
- [#task_2F7BEE7CB9604E5A9CE22F59A868378D] 
- [#concept_DA92494467F740FEA14182DF17FF435B] 
- [#id_110778] 
- [#Cisco_Task.dita_465f2b68-ba30-49a3-9fd6-471fbb9a6ecf] 
- [#Cisco_Concept.dita_6448d50d-1347-4e58-9976-07f9347f50a9] 
- [#concept_1C94AC4B56CC4621AEE1642039AD496A] 
- [#task_467BE90B278D4A3EA0A669CD7CDB8D58] 
- [#task_375CED713076446FAC2E142088171CA0] 
- [#task_7EDD79C1265F48EF839295084611F53E] 
- [#task_C154B51D06434F0EBC6E55D4E00BEC62] 
- [#task_6414C84081D3492E9817031E9362DEC1] 
- [#concept_05CD1F6650A44B71A4F665EA9C25B3EA] 
- [#task_t11_p41_ntb] 
- [#id_77483] 
### Specify the interfaces for configuration
 			 

The interface range configuration mode allows you to configure multiple interfaces of the same or different types using shared configuration parameters. After specifying the interfaces, all subsequent commands affect the selected interfaces until exiting interface configuration mode. 
 			 

Use these steps to specify interfaces for configuration.
 
#### Before you begin
 			 

Review interface types and their method of identification.
 			 
 Table 4. Interface Types and Their Identification Method 						 							 								 

Interface Type 
 							 							 								 

Identity 
 							 						 					 						 							 								 

Ethernet 
 							 							 								 

I/O module slot numbers and port numbers on the module 
 							 						 						 							 								 

Management 
 							 							 								 

0 (for port 0) 
 							 						 					 
 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify one or more interface to configure using the 						interface 						interface 					 					 command. 
 					 

**Ethernet interfaces**: To specify a single Ethernet interface. 
 					 
 

**Note**
  						 

No space is required between the interface type and identity (port or slot/port number).
 						 

 For example, for the Ethernet slot 4, port 5 interface, you can specify either “ethernet 4/5” or “ethernet4/5.” 
 					 
 				 
#### Example:
 					
```
`switch(config)# **interface ethernet 2/1** switch(config-if)#`
```
 				 					 

To specify a range of contiguous Ethernet interfaces (using a dash “-”):
 				 
#### Example:
 					
```
`switch(config)# **interface ethernet 2/29-30** switch(config-if-range)# `
```
 				 					 

To specify noncontiguous Ethernet interfaces (using commas and full specification for each):
 					 
 

**Note**
  						 

When specifying noncontiguous interfaces, enter the interface type for each entry for syntax flexibility: You may omit the space between the type and identity - “ethernet 4/5” or “ethernet4/5”. 
 					 
 				 
#### Example:
 					
```
`switch(config)# **interface ethernet 2/29, ethernet 2/33, ethernet 2/35** switch(config-if-range)# `
```
 				 					 

Use this syntax for breakout cables or multi-level slots:
 					
```
`switch(config)# **interface ethernet 1/2/1** switch(config-if-range)# `
```
 				 					 

 						**Management interface**
 				 					 

The management interface is either “mgmt0" or “mgmt 0”. 
 				 
#### Example:
 					
```
`switch(config)# **interface mgmt0** switch(config-if)#`
```
 				 					 

** VLAN interface**
 				 
#### Example:
 					
```
` switch(config)# interface vlan 10 switch(config-if)#`
```
 				 					 

 						**Loopback interface**
 				 
#### Example:
 					
```
`switch(config)# interface loopback 1 switch(config-if)#`
```
 				 					 

**Subinterfaces**
 					 

You can specify a range of subinterfaces only on the same port (using dash “-”). You can specify multiple subinterfaces discretely using commas: 
 					 
 

**Note**
  						 

You cannot specify a range crossing different ports (for example, “2/29.2-2/30.2” is invalid).
 					 
 				 
#### Example:
 					
```
`switch(config)# interface ethernet 2/29.1-2 switch(config-if-range)#`
```
 				 		 
 			 

You are now in interface configuration mode for the specified interfaces and ready to apply configuration parameters.
 		 
### Add description parameters to interfaces
 			 

You can add text descriptions to Ethernet and management interfaces.
 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the interface using the 						interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 2/1** switch(config-if)#`
```
 				 
#### Example:
 					
```
`switch(config)# **interface mgmt0** switch(config-if)#`
```
 				 					 
 						 
- 							 

 For an Ethernet port, use 									ethernet 									slot/port 								 								. For example, slot 2, port 1 identifies Ethernet interface 2/1. 
 						 						 
- 							 

For the management interface, use 									mgmt0 								 								. For example, mgmt0 identifies the management interface. 
 						 					 				 			 

**Step 3**
 

Add a description using the 						description 						text 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **description Ethernet port 3 on module 1** switch(config-if)#`
```
 				 			 

**Step 4**
 

(Optional) View the description using the 						show interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **show interface ethernet 2/1** `
```
 				 			 

**Step 5**
 

Exit the configuration.
 
#### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 			 

**Step 6**
 

(Optional) Save the current running configuration to the startup configuration.
 
#### Example:
 					
```
`switch(config)# copy running-config startup-config `
```
 				 		 
 
#### Example
 

This example shows 		 how to set the interface description to Ethernet port 24 on module 3: 		 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/24** switch(config-if)# **description server1** switch(config-if)#`
```
 

The output of the 		 show interface 				eth command is enhanced 		 as shown in the following example: 		 
 
```
` Switch# **show version** Software BIOS: version 06.26 NXOS: version 6.1(2)I2(1) [build 6.1(2)I2.1] BIOS compile time: 01/15/2014 NXOS image file is: bootflash:///n9000-dk9.6.1.2.I2.1.bin NXOS compile time: 2/25/2014 2:00:00 [02/25/2014 10:39:03] switch# **show interface ethernet 6/36** Ethernet6/36 is up admin state is up, Dedicated Interface Hardware: 40000 Ethernet, address: 0022.bdf6.bf91 (bia 0022.bdf8.2bf3) Internet Address is 192.168.100.1/24 MTU 9216 bytes, BW 40000000 Kbit, DLY 10 usec `
```
 
### Enable beacon mode for an Ethernet port
 			 

Flash the device's status LED to locate a specific Ethernet port.
 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 						configure terminal 					 				 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the interface using the 						interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 3/1** switch(config-if)#`
```
 				 			 

**Step 3**
 

Enable the beacon mode using the [no] beacon 					 command. 
 
#### Example:
 					
```
`switch(config)# **beacon** switch(config-if)#`
```
 				 					 

The default mode is disabled. Use the [no] beacon 						 command to disable the beacon mode. T 
 				 			 

**Step 4**
 

(Optional) View the interface status using the 						show interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **show interface ethernet 2/1** switch(config-if)#`
```
 				 			 

**Step 5**
 

Exit the configuration mode. 
 
#### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 			 

**Step 6**
 

(Optional) Save the running configuration to the startup configuration. 
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

The Ethernet port's LED flashes, so you can confirm the port's physical location visually.
 		 
#### Example
 

This example shows 		 how to enable the beacon mode for the Ethernet port 3/1: 		 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **beacon** switch(config-if)# `
```
 

This example shows 		 how to disable the beacon mode for the Ethernet port 3/1: 		 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **no beacon** switch(config-if)# `
```
 This example shows 		 how to configure the dedicated mode for Ethernet port 4/17 in the group that 		 includes ports 4/17, 4/19, 4/21, and 4/23: 		 
```
`switch# **configure terminal** switch(config)# **interface ethernet 4/17, ethernet 4/19, ethernet 4/21, ethernet 4/23** switch(config-if)# **shutdown** switch(config-if)# **interface ethernet 4/17** switch(config-if)# **no shutdown** switch(config-if)# `
```
 
### Configure the error-disabled state
 

An error-disabled state is a network interface condition that
 
 
- 

disables a port or interface automatically when a predefined fault or violation is detected,
 
- 

sends signals to the administrator with the specific error that caused the shutdown.
 

Common causes for interfaces entering error-disabled states include:
 
 
- 

BPDU Guard violations
 
- 

Unidirectional Link Detection (UDLD) malfunctions
 
- 

Port security breaches (such as excessive MAC address violations)
 
- 

Link flapping or physical layer errors
 

Network devices often provide logs or status messages to indicate the specific reason an interface was disabled.
 

You can view the reason that an interface moves to the error-disabled state and configure automatic recovery. 
 

- [#task_DF90090DDB9F42788DC75B387543DB82] 
- [#task_5C633E9A6FC34B788D2CA7688E7A93AB] 
- [#task_B504FA1F21CE464B9A1D956BBC6DE03D] 
#### Enable the error-disable detection
 			 

Use this task to configure error-disable detection so that interfaces interfaces enter an error-disabled state when certain faults, such as link flaps or ACL exceptions, are detected. 
 			 

You can enable error-disable detection in an application. As a result, when a cause is detected on an interface, the interface is placed in an error-disabled state, which is an operational state that is similar to the link-down state. 
 		 
##### Before you begin
 

You must have access to a device with appropriate administrative privileges (enable and configuration mode access).
 

Save your running configuration to prevent losing changes
. 
##### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
##### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

 					Specifiy one or more error condition to trigger error-disable on inteface using the errdisable detect cause {acl-exception | all | link-flap | loopback} 					 					 					 					 					 				 
 
##### Example:
 					
```
`switch(config)# **errdisable detect cause all** switch(config-if)#`
```
 				 					 

Error-disable detection is enabled by default for supported causes.
 				 			 			 

**Step 3**
 

If an interface is placed in error-disabled state and requires manual recovery:
 
 					 
- 						 

Administratively shut down the interface.
 						 
##### Example:
 							
```
`switch(config-if)# **shutdown** switch(config)# `
```
 						 					 					 
- 						 

Administratively bring the interface back up. 
 						 
##### Example:
 							
```
`switch(config-if)# **no shutdown** switch(config)# `
```
 						 					 				 					 
 

**Note**
  						 

These commands clear the error-disabled state and restore interface operation.
 					 
 				 			 

**Step 4**
 

(Optional) View information about error-disabled interfaces using the 						show interface status err-disabled command. 					 				 
 
##### Example:
 					
```
`switch(config)# **show interface status err-disabled** `
```
 				 			 

**Step 5**
 

(Optional) Save the running configuration using the 						copy running-config startup-config 					 command. 
 
##### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

Error-disable detection is enabled so that when configured causes are detected on an interface, the interface enters the error-disabled state. 
 		 
##### Example
 			 

This example shows how to enable the error-disabled detection in all cases: 
 			
```
`switch(config)# **errdisable detect cause all** switch(config)# `
```
 		 
#### Recover an interface from error-disabled state
 			 

An interface may become error-disabled for several reasons. Configure recovery to allow the interface to attempt to come up again after a specified interval. 
 			 

You can specify the application to bring the interface out of the error-disabled state. By default, the interface retries after 300 seconds unless you configure the recovery timer using the 					errdisable recovery interval 				 command. 
 		 
##### Before you begin
 			 

Ensure you have administrative access to the switch CLI.
 			 

Confirm the error-disabled cause for the interface. 
 		 
##### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode.
 
##### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the condition for automatic recovery using the 						errdisable recovery cause {all | bpduguard | failed-port-state | link-flap | loopback | miscabling | psecure-violation | security-violation | storm-control | udld | vpc-peerlink} 					 					 					 					 					 					 					 					 					 					 					 					 command. 
 
##### Example:
 					
```
`switch(config)# **errdisable recovery cause all** switch(config-if)#`
```
 				 					 

The device attempts to bring up the interface and waits 300 seconds before another attempt. Automatic recovery is disabled by default. 
 				 			 

**Step 3**
 

(Optional) View error-disabled interface information using the 						show interface status err-disabled 					 					 command. 
 
##### Example:
 					
```
`switch(config)# **show interface status err-disabled** switch(config-if)#`
```
 				 			 

**Step 4**
 

 					Save the running configuration to the startup configuration. 				 
 
##### Example:
 					
```
`switch(config)# **copy running-config startup-config** 					`
```
 				 		 
 			 

The switch attempts to bring the interface up after the recovery interval (default 300 seconds), based on the conditions you specify. 
 		 
##### Example
 			 

This example shows 				how to enable error-disabled recovery under all conditions: 			 
 			
```
`switch(config)# **errdisable recovery cause all** switch(config)# `
```
 		 
#### Set the error-disabled recovery interval for interfaces 
 			 

When a switch port enters an error-disabled state, you can control how long the port remains disabled before the switch attempts recovery. 
 			 

Configuring the error-disabled recovery interval automates port recovery and minimizes unnecessary downtime
 			 

Use these steps to configure the error-disabled recovery timer value. 
 		 
##### Before you begin
 			 

Determine the desired interval (in seconds) for port recovery (valid range: 30–65535 seconds).
 		 
##### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
##### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Set the interval for the interface to recover from the error-disabled state using the 						errdisable recovery interval 						interval 					 					 command. 
 
##### Example:
 					
```
`switch(config)# **errdisable recovery interval 32** switch(config-if)# `
```
 				 					 

The interval range value is from 30 to 65,535 seconds. The default value is 300 seconds.
 				 			 

**Step 3**
 

(Optional) View information on error-disabled interfaces using the 						show interface status err-disabled 					 					 command. 
 
##### Example:
 					
```
`switch(config)# **show interface status err-disabled** switch(config-if)#`
```
 				 			 

**Step 4**
 

(Optional) Save the running configuration to the startup configuration. 
 
##### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

The switch automatically attempts to recover any error-disabled interfaces after the specified interval. Ports previously disabled by error conditions begin the recovery process based on your configured timer. 
 		 
##### Example
 			 

This example shows 				how to configure the error-disabled recovery timer to set the interval for 				recovery to 32 seconds: 			 
 			
```
`switch(config)# errdisable recovery interval 32 switch(config)#`
```
 		 
### Configure MDIX parameters
 

Configure MDIX on a port when you connect devices that use different or unknown cable types. Most devices have MDIX enabled by default to maximize flexibility. 
 

To detect the type of connection with another copper Ethernet port, enable MDIX on the local port. By default, this parameter is enabled. 
 
#### Before you begin
 

Confirm the interface and the platform support manual MDIX configuration. Enable MDIX on the remote port.
 
#### Procedure
 
 

**Step 1**
 

 Enter global configuration mode.
 
#### Example:
 
```
`switch# **configure terminal** switch(config)#`
```
 \ 

**Step 2**
 

Specify an interface using the interface ethernet slot / port command. 
 
#### Example:
 
```
`switch(config)# **interface ethernet 3/1** switch(config-if)# `
```
 

**Step 3**
 

Enable MDIX detection using the {mdix auto} command. 
 
#### Example:
 
```
`switch(config)# **mdix auto** switch(config-if)#`
```
 
```
`switch(config)# **no mdix**switch(config-if)#`
```
 

The no mdix command disables MDIX detection. 
 
 

**Note**
  

The no mdix auto command is supported only on N9K-C93108TC-EX, N9K-C93108TC-FX, N9K-X9788TC-FX, and N9K-C9348GC-FXP devices. 
 
 

**Step 4**
 

Verify the MDIX parameters using the show interface ethernet slot / port command. 
 
#### Example:
 
```
`switch(config)# **show interface ethernet 3/1** switch(config-if)# `
```
 

**Step 5**
 

Exit the configuration. 
 
#### Example:
 
```
`switch(config)# **exit** `
```
 

**Step 6**
 

Save the running configuration to the startup configuration.
 
#### Example:
 
```
`switch(config)# **copy running-config startup-config** `
```
 
 

After you complete these steps, the MDIX mode remains set on the interface.
 
#### Example
 

This example shows how to enable MDIX for Ethernet port 3/1:
 
```
`switch# configure terminal switch(config)# interface ethernet 3/1 switch(config-if)# mdix auto switch(config-if)# `
```
 

This example shows how to enable MDIX for Ethernet port 3/1:
 
```
`switch# configure terminal switch(config)# interface ethernet 3/1 switch(config-if)# no mdix switch(config-if)# `
```
 
### Configure media-type for SFP-10G-T-X transceivers
 

Use this task to specify the SFP-10G-T-X media type for a device interface. To configure this, enter the media-type 10g-tx command in interface configuration mode. To restore the default, enter the no media-type 10g-tx command. 
 

Use these steps to configure the media type for an SFP-10G-T-X transceiver.
 
#### Procedure
 
   Command or Action Purpose 

**Step 1**
 

Enter global configuration mode.
 
#### Example:
 
```
`Switch# **configure terminal** `
```
 

**Step 2**
 

Enter interface configuration mode for the interface that has the SFP-10G-T-X installed. 
 
#### Example:
 
```
`Switch (config)# **interface ethernet 1/5** `
```
 

**Step 3**
 

Configure the media type as 10G-TX on the interface by using the media-type 10g-tx command. 
 
#### Example:
 
```
`Switch (Config)# **[no] media-type 10g-tx** `
```
 
 

**Note**
  

If the interface is configured with media-type 10G-TX while in the administrative "up" state and does not support this configuration,the interface enters into the error-disabled state. To recover, enter these commands on the interface: 
 
 
- 

 shutdown 
 
- 

 no shutdown 
 
 
 

The interface is set to use the SFP-10G-T-X media type. If the interface does not support this configuration, you may need to take additional steps to recover from an error-disabled state 
 
### Verify media-type
 

Verify the media-type configuration on Cisco switches using these commands. The media-type defines the physical interface’s capabilities (such as copper or fiber and supported speeds). 
 
 
- 

show running-config interface interface : Displays the current configuration, including the media-type set for the specified interface. 
 
- 

show interface status : Lists all active interfaces, their operational status, speed, and detected media type,. For example, SFP-10G-T-X modules may be present on various ports. 
 
- 

show module : Shows detailed information about installed hardware modules, including supported port types and slot details. 
 

Use this example to verify the media-type configuration:
 
 

**Note**
 

Ports supporting SFP-10G-T-X modules may differ between devices. This example displays the port numbers for SFP-10G-T-X on a Cisco Nexus N9K-C93240YC-FX2 switch. 
 
 
```
`switch# **show running-config interface ethernet 1/2 ** !Command: show running-config interface Ethernet1/2 !Running configuration last done at: Mon Jun 1 10:16:46 2020 !Time: Mon Jun 1 10:16:54 2020 version 9.3(5) Bios:version 05.41 interface Ethernet1/2 switchport switchport access vlan 10 mtu 9216 media-type 10g-tx no shutdown Supported ports in Switch 01: `
```
 
```
`switch# **show interface status | i i SFP-10** Eth1/2 -- connected 10 full 10G SFP-10G-T-X Eth1/6 -- connected 11 full 10G SFP-10G-T-X Eth1/8 -- connected 11 full 10G SFP-10G-T-X Eth1/12 -- connected 12 full 10G SFP-10G-T-X Eth1/14 -- connected 12 full 10G SFP-10G-T-X Eth1/18 -- connected 13 full 10G SFP-10G-T-X Eth1/20 -- connected 13 full 10G SFP-10G-T-X Eth1/24 -- connected 14 full 10G SFP-10G-T-X Eth1/26 -- connected 14 full 10G SFP-10G-T-X Eth1/30 -- connected 15 full 10G SFP-10G-T-X Eth1/32 -- connected 15 full 10G SFP-10G-T-X Eth1/36 -- connected 16 full 10G SFP-10G-T-X Eth1/38 -- connected 16 full 10G SFP-10G-T-X Eth1/42 -- connected 20 full 10G SFP-10G-T-X Eth1/44 Connect_to_Sw_01 connected 202 full 10G SFP-10G-T-X Eth1/48 Connect_to_Sw_02 connected 202 full 10G SFP-10G-T-X `
```
 
```
` switch# **show module** Mod Ports Module-Type Model Status --- ----- ------------------------------------- --------------------- --------- 1 60 48x10/25G + 12x40/100G Ethernet Modul N9K-C93240YC-FX2 active * Mod Sw Hw Slot --- ----------------------- ------ ---- 1 9.3(4.104) 0.3020 NA Mod MAC-Address(es) Serial-Num --- -------------------------------------- ---------- 1 b4-de-31-94-4e-c8 to b4-de-31-94-4f-0f FDO2143306S Mod Online Diag Status --- ------------------ 1 Pass`
```
 
### Set MTU size
 		 			 				 				 

A maximum transmission unit (MTU) size is a network interface parameter that
 				 
 					 
- 						 

defines the largest packet size an interface can transmit without fragmentation,
 					 					 
- 						 

differs depending on whether the interface is Layer 2 or Layer 3, and
 					 					 
- 						 

can be set to the default, jumbo, or a custom value to suit network requirements.
 					 				 			 		 		 
#### Default values
 			 			 
 				 
- 					 

Every interface has a default MTU of 1500 bytes, known as the system default MTU.
 				 				 
- 					 

Layer 2 interfaces can be configured with a value of 9216 bytes, which is the default value for the system jumbo MTU.
 				 			 		 		 
#### Guidelines to configure MTU size
 			 			 

MTU is configured per interface. Interfaces may be Layer 2 or Layer 3. 
 			 
 				 
- 					 

For Layer 2 interfaces, you can select either the system default MTU (1500 bytes) or the system jumbo MTU (9216 bytes by default).
 					 

To configure a Layer 2 MTU between 1500 and 9216 bytes, first adjust the system jumbo MTU to the desired value. Then, set the interface MTU. 
 					 
 

**Note**
 						 

When the system jumbo MTU size is changed, all Layer 2 interfaces using the system jumbo MTU are automatically updated to the new value. 
 					 
 				 				 
- 					 

For Layer 3 interfaces (physical, switch virtual interface [SVI], or subinterface), you can set an MTU size between 576 and 9216 bytes. 
 				 			 		 		 
#### Examples
 			 			 

If you set the system jumbo MTU to 9000 bytes, all Layer 2 interfaces configured to use the jumbo value change to 9000 bytes.
 			 			 

To configure a Layer 3 SVI with an MTU of 2000 bytes, set the MTU directly on the SVI within the range of 576 to 9216 bytes.
 		 	 

- [#task_B7C698CB3AB044E8A1D6A7DDF51CF1F2] 
- [#id_114490] 
#### Configure MTU size for interfaces
 			 			 

Configuring the MTU size allows you to optimize network performance for specific applications and ensure compatibility with upstream or downstream devices. The MTU settings may differ between Layer 2 and Layer 3 interfaces. 
 			 		 
##### Before you begin
 			 

Determine whether you are configuring a Layer 2, Layer 3, or a management interface
 			 

Ensure you know the appropriate MTU value.
 			 
 				 
- 					 

For Layer 3 interfaces (including physical, SVI, or subinterfaces), enter a value between 576 and 9216 bytes.
 				 				 
- 					 

For Layer 2 interfaces, enter 1500 (system default) or the system jumbo MTU value (default is 9216 bytes; this value can be adjusted). 
 					 

For management interfaces on Cisco Nexus 9000 switches running Cisco NX-OS Release 9.3(1) or later, up to 9216 bytes are supported.
 				 			 			 
 

**Note**
 				 

When you change the MTU size, the end device may briefly lose its network connection.
 			 
 		 
##### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode.
 
##### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the ethernet interface to configure using the 						interface ethernet 						slot/port, vlan vlan-id mgmt 0 					 					 command. 
 
##### Example:
 					
```
`switch(config)# **interface ethernet 3/1** switch(config-if)# switch(config)# interface vlan 100 switch(config-if)# switch(config)# interface mgmt 0 switch(config-if)#`
```
 				 			 

**Step 3**
 

Configure the MTU value on an interface using the 						mtu 						size 					 					 command. 
 
##### Example:
 					
```
`switch(config-if)# **mtu 9216** switch(config-if)# `
```
 				 					 

 							size 						 is the desired MTU value within the supported range for the interface type 
 					 
 						 
- 							 

For Layer 3 interfaces, enter a value between 576 and 9216 bytes.
 						 						 
- 							 

For Layer 2 interfaces, enter 1500 or the system jumbo MTU value
 						 					 					 

If you need to use a different system jumbo MTU size for Layer 2 interfaces, see Set the system jumbo MTU size. 
 				 			 

**Step 4**
 

Exit the configuration.
 
##### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 		 
 			 

The interface you selected uses the MTU value that you configured for packet transmission.
 		 
##### Example
 			 

This example shows 				how to configure the Layer 2 Ethernet port 3/1 with the default MTU size 				(1500): 			 
 			
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **switchport** switch(config-if)# **mtu 1500** switch(config-if)# 			`
```
 			

This example displays the output of show running-config interface command: 
 			
```
`switch# **show run int mgmt0** !Command: show running-config interface mgmt0 !Running configuration last done at: Fri May 31 11:32:28 2019 !Time: Fri May 31 11:32:33 2019 version 9.3(1) Bios:version 07.65 interface mgmt0 mtu 9216 vrf member management ip address 168.51.170.73/82 			`
```
 		 
#### Set the system jumbo MTU size
 

Set the system jumbo MTU when your network environment requires support for frames larger than standard Ethernet frames to increase throughput for high-performance applications. The system jumbo MTU must be an even number between 1500 and 9216. The default is 9,216 bytes. 
 
##### Procedure
 
 

**Step 1**
 

Enter global configuration mode. configure terminal 
 
##### Example:
 
```
`switch# **configure terminal** switch(config)#`
```
 

**Step 2**
 

Set the system jumbo MTU size using the system jumbomtu size command. 
 
##### Example:
 
```
`switch(config)# **system jumbomtu 8000** switch(config)# `
```
 

Use an even number between 1,500 to 9,216. 
 

**Step 3**
 

Specify the Layer 2 interface using the interface type slot/port command. 
 
##### Example:
 
```
`switch(config)# **interface ethernet 2/1** switch(config-if)# `
```
 

**Step 4**
 

Apply the MTU to the interface using the mtu size command. 
 
##### Example:
 
```
`switch(config-if)# **mtu 8000** switch(config-if)# `
```
 

**Step 5**
 

Exit the configuration.
 
##### Example:
 
```
`switch(config-if)# **exit** switch(config)# `
```
 

Exits the interface mode.
 

**Step 6**
 

(Optional) Save the running configuration to the startup configuration. 
 
##### Example:
 
```
`switch(config)# **copy running-config startup-config** `
```
 
 

Layer 2 interfaces use the new jumbo MTU value, supporting larger frames as specified.
 
##### Example
 

This example shows how to configure the system jumbo MTU as 8000 bytes and how to change the MTU specification for a Layer 2 interface that was configured with the previous jumbo MTU size: 
 
```
`switch# **configure terminal** switch(config)# **system jumbomtu 8000** switch(config)# **interface ethernet 2/2** switch(config-if)# **mtu 8000** `
```
 
### Configure the bandwidth for Ethernet interfaces
 			 

In Nexus switches, the bandwidth command sets an informational value for Layer 3 protocols. The physical bandwidth of Ethernet interfaces, such as 1G, 10G, or 40G, cannot be changed. 
 		 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode.
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify an Ethernet interface using the 						interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 3/1** switch(config-if)# `
```
 				 			 

**Step 3**
 

Set the bandwidth using the 						bandwidth 						kbps 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **bandwidth 1000000** switch(config-if)#`
```
 				 					 

The bandwidth is an informational-only value. It ranges from 1 and 100,000,000 kilobits per second.
 				 			 

**Step 4**
 

(Optional) View the interface status using the 						show interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **show interface ethernet 2/1** `
```
 				 			 

**Step 5**
 

Exit the configuration mode. 
 
#### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 			 

**Step 6**
 

(Optional) Save the running configuration to the startup configuration. 
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

The interface displays the updated informational bandwidth value for Layer 3 protocols. The physical interface bandwidth remains unchanged. 
 		 
#### Example
 			 

This example shows how to configure an informational value of 1,000,000 kbps for the Ethernet slot 3, port 1 interface bandwidth parameter. 
 			
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **bandwidth 1000000** switch(config-if)# 			`
```
 		 
### Set the throughput delay interval
 			 

The throughput delay value provides information and affects protocol path preference for Ethernet interfaces.
 			 

You can set an informational value in the range of 1 and 16,777,215 tens of microseconds.
 
#### Before you begin
 			 

Ensure the EIGRP feature is enabled by running the 					feature eigrp 				 				 command. 
 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode.
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the interface using the 						interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 3/1** switch(config-if)# `
```
 				 			 

**Step 3**
 

Set the delay interval using the 						delay 						value 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **delay 10000** switch(config-if)# `
```
 				 Configure a value between 1 and 16,777,215 tens of microseconds. 			 

**Step 4**
 

View the interface status to verify the delay setting.
 
#### Example:
 					
```
`switch(config)# **show interface ethernet 3/1** switch(config-if)# `
```
 				 			 

**Step 5**
 

(Optional) Exit the configuration. 
 
#### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 			 

**Step 6**
 

(Optional) Save the running configuration to startup configuration. 
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 
#### Example
 

This example configures a high delay value for Ethernet 7/47 and a lower (default) value for 7/48, making 7/48 the preferred interface. A lower delay value is preferred over a higher value. 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 7/47** switch(config-if)# **delay 16777215** switch(config-if)# **ip address 192.168.10.1/24** switch(config-if)# **ip router eigrp 10** switch(config-if)# **no shutdown** switch(config-if)# **exit** switch(config)# **interface ethernet 7/48** switch(config-if)# **ip address 192.168.11.1/24** switch(config-if)# **ip router eigrp 10** switch(config-if)# **no shutdown** switch(config-if)# `
```
 
### Shut down and activate interfaces
 			 

You may need to temporarily disable (shut down) or enable (activate) an interface for maintenance, troubleshooting, or configuration.
 			 

When an interface is shut down, it becomes disabled. The monitoring displays it as down, and routing protocols exclude it from updates. You can reactivate the interface at any time. You can restart the device to reactivate the interface. 
 			 

Use these steps to shut down and activate an interface.
 
#### Procedure
 
 			 

**Step 1**
 

 Enter global configuration mode.
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the target interface using the 						interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 2/1** switch(config-if)# switch(config)# **interface mgmt0** switch(config-if)#`
```
 				 					 

You can specify the interface type and identity. 
 					 
 

**Note**
  						 

Use ethernet slot/port for Ethernet interfaces and mgmt0 for management interfaces. 
 					 
 					 

Examples
 					 
 						 
- 							 

Ethernet interfaces: The first example shows how to specify the slot 2, port 1 Ethernet interface. 
 						 						 
- 							 

Management interface: The second example shows how to specify the management interface. 
 						 					 				 			 

**Step 3**
 

Disable the interface using the 						shutdown 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **shutdown** switch(config-if)# `
```
 				 			 

**Step 4**
 

(Optional) View the interface status using the 						show interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **show interface ethernet 2/1** switch(config-if)#`
```
 				 			 

**Step 5**
 

Enable (activate) the interface using the 						no shutdown 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **no shutdown** switch(config-if)# `
```
 				 			 

**Step 6**
 

(Optional) View the status of the interface again.
 
#### Example:
 					
```
`switch(config-if)# **show interface ethernet 2/1** switch(config-if)#`
```
 				 			 

**Step 7**
 

Exit the interface mode.
 
#### Example:
 					
```
`switch(config-if)# **exit** switch(config)# `
```
 				 			 

**Step 8**
 

(Optional) Save the running configuration to the startup configuration with the 						copy running-config startup-config 					 				 
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

When you enable the port, its administrative status changes from disabled (down) to enabled (up). The interface becomes active and is included in routing updates. 
 		 
#### Example
 			 

This example shows how to disable and re-enable Ethernet port 3/1:
 			
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **shutdown** switch(config-if)# **no shutdown** switch(config-if)# `
```
 		 
### Enable UDLD modes on interfaces
 

UDLD detects unidirectional links on fiber and copper Ethernet ports and prevents network issues caused by one-way communication. Enable UDLD globally or per interface. Select normal or aggressive mode according to reliability needs. You can enable aggressive mode globally for all fiber ports or on individual interfaces. 
: 

This table lists the commands to enable and disable UDLD on different interfaces.
 
 Table 5. Default UDLD Settings for Fiber and Copper Ports 						 							 								 

Description 
 							 							 								 

Fiber port 
 							 							 								 

Copper or Non-fiber port 
 							 						 					 						 							 								 

Default setting 
 							 							 								 

Enabled 
 							 							 								 

Disabled 
 							 						 						 							 								 

Enable UDLD command 
 							 							 								 

 									 										no udld disable 									 								 
 							 							 								 

 									 										udld enable 									 								 
 							 						 						 							 								 

Disable UDLD command 
 							 							 								 

 									 										udld disable 									 								 
 							 							 								 

 									 										no udld enable 									 								 
 							 						 					 
 

Use these steps to enable UDLD mode.
 
#### Before you begin
 

Before enabling UDLD, ensure it is enabled globally using the feature udld command. On copper ports, explicitly enable UDLD for each interface. On fiber ports, UDLD is enabled by default; confirm this with the no udld disable command. 
Enable aggressive UDLD mode only after you have configured UDLD globally and on each specified interface. 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Enable UDLD globally using the feature udld 					 command. 
 
#### Example:
 					
```
`switch(config)# **feature udld** switch(config)#`
```
 					
```
`switch(config)# **no feature udld** switch(config)#`
```
 				 					 

Use the no feature udld command to disable UDLD fiber ports by default. 
 				 			 

**Step 3**
 

(Optional) Specify the interval to send UDLD messages using the 						udld message-time 						seconds 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **udld message-time 30** switch(config)#`
```
 				 					 

The range is 7 to 90 seconds; the default value is 15 seconds
 				 			 

**Step 4**
 

Enable UDLD in aggressive mode using the 						udld aggressive 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **udld aggressive** switch(config)#`
```
 				 Use the 						no 					 form to disable aggressive mode UDLD on all fibers ports by default. 
 

**Note**
  						 

Use the udld aggressive command to configure the ports. 
 						 
 							 
- 								 

For all fiber ports, use the `udld aggressive` command in global configuration mode. 
 							 							 
- 								 

For specific copper interfaces, enter interface configuration mode interface ethernet 										slot/port and enable the `udld aggressive ` command. 
 							 						 					 
 			 			 

**Step 5**
 

Enable UDLD in normal mode on all fiber interfaces using the 						udld [enable | disable] 					 				 
 
#### Example:
 					
```
`switch(config-if)# **udld enable** switch(config-if)#`
```
 				 					 					 

Disable normal mode UDLD on all fiber ports by default using the 							no 						 command. 
 				 			 

**Step 6**
 

View the UDLD status with the 						show udld [ethernet 						slot/port | global | neighbors] 					 command. 
 
#### Example:
 					
```
`switch(config)# **show udld** switch(config)#`
```
 				 			 

**Step 7**
 

Exit interface mode.
 
#### Example:
 					
```
`switch(config-if-range)# **exit** switch(config)# `
```
 				 			 

**Step 8**
 

(Optional) Save the running configuration to startup configuration. 
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 

UDLD operates in the selected mode to provide bidirectional link detection according to your configuration.
 
#### Example
 

This example shows how to enable the UDLD for the device: 
 
```
`switch# **configure terminal** switch(config)# **feature udld** switch(config)#`
```
 

This example shows how to set the UDLD message interval to 30 seconds: 
 
```
`switch# **configure terminal** switch(config)# **feature udld** switch(config)# **udld message-time 30** switch(config)# `
```
 

This example shows how to disable UDLD for Ethernet port 3/1: 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if-range)# **no udld enable** switch(config-if-range)# **exit** `
```
 

This example shows how to disable UDLD for the device: 
 
```
`switch# **configure terminal** switch(config)# **no feature udld** switch(config)# **exit** `
```
 This example shows how to enable fiber interfaces for the aggressive UDLD mode:
```
`switch# configure terminal switch(config)# udld aggressive `
```
 This example shows how to enable the aggressive UDLD mode for the copper Ethernet interface3/1:
```
`switch# configure terminal switch(config)# interface ethernet 3 switch(config-if)# udld aggressive`
```
 This example shows how to check if aggressive mode is enabled.
```
`switch# sh udld global UDLD global configuration mode: enabled-aggressive UDLD global message interval: 15 switch#`
```
 This example shows how to check if udld aggressive mode is operational for a given interface.
```
`switch# sh udld ethernet 8/2 Interface Ethernet8/2 -------------------------------- Port enable administrative configuration setting: device-default Port enable operational state: enabled-aggressive Current bidirectional state: bidirectional Current operational state: advertisement - Single neighbor detected Message interval: 15 Timeout interval: 5 ..!`
```
 
### Configure debounce timers for Ethernet ports
 			 

Enable the debounce timer for Ethernet ports by specifying a debounce time (in milliseconds). 
 			 

Disable the timer by specifying a debounce timer value of 0.
 			 **Guidelines** 			 			 
 				 
- 					 

The link state of 10G and 100G ports may change repeatedly when connected to the service provider network. As a part of *link reset* or *break-link* functionality, the Tx power light on the SFP is expected to change to N/A state when a link state change occurs. To prevent this behavior during a link state change, increase the link debounce timer starting at 500 ms, and then raise it in 500 ms intervals until the link stabilizes. 
 				 				 
- 					 

On DWDM, UVN, and WAN networks, disable automatic link suspension (ALS) whenever possible ALS suspends the link on the WAN when the device turns off the link. 
 				 				 
- 					 

 The 							link debounce time 						 and 							link debounce link-up time 						 commands can only be applied to a physical Ethernet interface. 
 				 				 
- 					 

Use the 							show interface debounce 						 command to display the debounce times for all Ethernet ports. 
 				 			 			 **Support for debounce timer**
 					 
- 						 

The 								link debounce time 							 command is supported on 1G, 10G, 40G, 25G and 100G SFP/QSFP ports on the Cisco Nexus 9000 series switches. 
 					 					 
- 						 

The 								link debounce time 							 is supported on 1G, 10G, 25G, 40G and 100G ports on Cisco Nexus N9K-C9732C-FX, N9K-C9364C, N9K-X97160YC-EX, N9K-C9336C-FX2, and N9K-C93240YC-FX2 platform switches. 
 					 					 
- 						 

The 								link debounce time 							 command is not supported on 10G and 40G ports on the Cisco Nexus 93300YC-FX and Cisco Nexus 9336C-FX switches. 
 						 

The 								link debounce time 							 is supported on 1G, 10G, 25G, 40G and 100G ports on Cisco Nexus N9K-C9732C-FX, N9K-C9364C, N9K-X97160YC-EX, N9K-C9336C-FX2, and N9K-C93240YC-FX2 platform switches. 
 					 					 
- 						 

The 								link debounce time 							 is not supported on RJ-45 ports on Cisco Nexus 9500 platform switches with N9K-X97160TC-FX line cards. 
 					 					 
- 						 					 					 
- 						 						 					 				 		 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 					 				 			 

**Step 2**
 

Specify an Ethernet interface using the 						interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 3/1** switch(config-if)# `
```
 				 			 

**Step 3**
 

Set the debounce timer using the 						 link debounce time 						time 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **link debounce time 1000** switch(config-if)#`
```
 				 					 

 							time 						 : The debounce timer time ranges from 1 to 5000 milliseconds. 
 					 

 When you specify 0 milliseconds, the debounce timer is disabled. 
 				 			 

**Step 4**
 

Set the link-up timer using the 						 link debounce link-up 						time 					 					 command. 
 
#### Example:
 					
```
`switch(config-if)# **link debounce link-up 1000** switch(config-if)#`
```
 				 					 

 							time 						 :The link-up timer time ranges from 1000 to 10000 milliseconds. Use this command only if port speeds are 10G, 25G, 40G, or 100G. 
 The default value of the timer is 0. If the value is set to 0, the interface comes up without delay. 
 

**Note**
  						 

The 								no link debounce link-up 							 command also resets the value to 0. 
 					 
 					 
 

**Note**
  						 

This command is supported only on Cisco Nexus N9K-X9732C-FX , N9K-C93300YC-FX, N9K-C9336C-FX2, N9K-C9364C and N9K-X97160YC-EX switches. 
 					 
 				 		 
 
#### Example
 
 
- 

 The following example enables the debounce timer and sets the 				debounce time to 1000 milliseconds for an Ethernet interface: 			 
 
```
` switch# **configure terminal** switch(config)# **interface ethernet 1/4** switch(config-if)# **link debounce time 1000** `
```
 
- 

 The following example disables the debounce timer for an Ethernet 				interface: 			 
 
```
` switch# **configure terminal** switch(config)# **interface ethernet 1/4** switch(config-if)# **link debounce time 0** `
```
 
- 					 

 The following example sets the debounce link-up timer to 1000 milliseconds for an Ethernet interface: 
 
```
` switch# **configure terminal** switch(config)# **interface ethernet 1/4** switch(config-if)# **link debounce link-up time 1000** `
```
 
### Configuring Port 	 Profiles 
 

You can apply several configuration parameters to a range of interfaces simultaneously. All the interfaces in the range must be the same type. You can also inherit the configurations from one port profile into another port profile. The system supports four levels of inheritance. 
 

- [#task_949680A841F24707ABC0E320AA79DC47] 
- [#task_3D3FDFA8E7264EC0BCC9677BD0A9BDFB] 
- [#task_8265D9D4AB9E4DE79B6C963B2F0427C8] 
- [#task_532B9110C5E74AE2A8272249F8999922] 
- [#task_1479561618D44C30A2651F7929898F02] 
- [#task_0CF9650AEEE1411AA4751FF18BA67D0D] 
- [#task_3BF33AE3FAF9468BA83153D2A34A22B5] 
#### Creating a Port 	 Profile 
 		 

You can create a 		 port profile on the device. Each port profile must have a unique name across 		 types and the network. 		 
 		 
 

**Note**
 		 

Port profile names 			 can include only the following characters: 		 
 		 
 
- 				 

a-z 				 
 			 
- 				 

A-Z 				 
 			 
- 				 

0-9 				 
 			 
- 				 

No special characters are allowed, except for the following: 				 
 				 
 
- 					 

. 					 
 				 
- 					 

- 					 
 				 
- 					 

_ 					 
 				 			 		 
 	 
### SUMMARY STEPS
 
 
- configure terminal 		 
- port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
- exit 		 
- (Optional) show port-profile 		 
- (Optional) copy running-config startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
 			 

Creates and 				names a port profile for the specified type of interface and enters the 				port-profile configuration mode. 			 
 		 

**Step 3**
 

exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 4**
 

(Optional) show port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 5**
 

(Optional) copy running-config startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows 		 how to create a port profile named test for ethernet interfaces: 		 
```
` switch# **configure terminal** switch(config)# **port-profile type ethernet test** switch(config-ppm)#`
```
 		 	 
#### Entering 	 Port-Profile Configuration Mode and Modifying a Port Profile 
 		 

You can enter the 		 port-profile configuration mode and modify a port profile. To modify the port 		 profile, you must be in the port-profile configuration mode. 		 
 	 
### SUMMARY STEPS
 
 
- 			 configure 				 terminal 		 
- 			 port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
- 			 exit 		 
- (Optional) 			 show 				 port-profile 		 
- (Optional) 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 configure 				 terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

 			 port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
 			 

Enters the 				port-profile configuration mode for the specified port profile and allows you 				to add or remove configurations to the profile. 			 
 		 

**Step 3**
 

 			 exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 4**
 

(Optional) 			 show 				 port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 5**
 

(Optional) 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows 		 how to enter the port-profile configuration mode for the specified port profile 		 and bring all the interfaces administratively up: 		 
```
` switch# configure terminal switch(config)# **port-profile type ethernet test** switch(config-ppm)# **no shutdown** switch(config-ppm)#`
```
 		 	 
#### Assigning a Port 	 Profile to a Range of Interfaces 
 		 

You can assign a 		 port profile to an interface or to a range of interfaces. All the interfaces 		 must be the same type. 		 
 	 
### SUMMARY STEPS
 
 
- configure terminal 		 
- interface [ethernet 				slot/port | 				interface-vlan 				vlan-id | 				port-channel 				number] 		 
- inherit port-profile 				name 		 
- exit 		 
- (Optional) show port-profile 		 
- (Optional) copy running-config startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

interface [ethernet 				slot/port | 				interface-vlan 				vlan-id | 				port-channel 				number] 		 
 			 

Selects the 				range of interfaces. 			 
 		 

**Step 3**
 

inherit port-profile 				name 		 
 			 

Assigns the 				specified port profile to the selected interfaces. 			 
 		 

**Step 4**
 

exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 5**
 

(Optional) show port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 6**
 

(Optional) copy running-config startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows 		 how to assign the port profile named adam to Ethernet interfaces 7/3 to 7/5, 		 10/2, and 11/20 to 11/25: 		 
```
` switch# **configure terminal** switch(config)# **interface ethernet7/3-5, ethernet10/2, ethernet11/20-25** switch(config-if)# **inherit port-profile adam** switch(config-if)#`
```
 		 	 
#### Enabling a Specific 	 Port Profile 
 		 

To apply the 		 port-profile configurations to the interfaces, you must enable the specific 		 port profile. You can configure and inherit a port profile onto a range of 		 interfaces before you enable that port profile. You would then enable that port 		 profile for the configurations to take effect on the specified interfaces. 		 
 		 

If you inherit one 		 or more port profiles onto an original port profile, only the last inherited 		 port profile must be enabled; the system assumes that the underlying port 		 profiles are enabled. 		 
 		 

You must be in the 		 port-profile configuration mode to enable or disable port profiles. 		 
 	 
### SUMMARY STEPS
 
 
- 			 configure 				 terminal 		 
- 			 port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
- state enabled 		 
- exit 		 
- (Optional) 			 show 				 port-profile 		 
- (Optional) copy running-config startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 configure 				 terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

 			 port-profile [type {ethernet | 				interface-vlan | 				port-channel}] 				name 		 
 			 

Creates and 				names a port profile for the specified type of interface and enters the 				port-profile configuration mode. 			 
 		 

**Step 3**
 

state enabled 		 
 			 

Enables that 				port profile. 			 
 		 

**Step 4**
 

exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 5**
 

(Optional) 			 show 				 port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 6**
 

(Optional) copy running-config startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows 		 how to enter the port-profile configuration mode and enable the port profile: 		 
```
` switch# **configure terminal** switch(config)# **port-profile type ethernet test** switch(config-ppm)# **state enabled** switch(config-ppm)#`
```
 		 	 
#### Inheriting a Port Profile
 		 

You can inherit a port profile onto an existing port profile. The 		 system supports four levels of inheritance. 		 
 	 
### SUMMARY STEPS
 
 
- configure terminal 		 
- port-profile 				name 		 
- inherit port-profile 				name 		 
- 			 exit 		 
- (Optional) show port-profile 		 
- (Optional) 			 copy running-config startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 		 
 			 

Enters the global configuration mode. 			 
 		 

**Step 2**
 

port-profile 				name 		 
 			 

Enters the port-profile configuration mode for the specified port 				profile. 			 
 		 

**Step 3**
 

inherit port-profile 				name 		 
 			 

Inherits another port profile onto the existing one. The original 				port profile assumes all the configurations of the inherited port profile. 			 
 		 

**Step 4**
 

 			 exit 		 
 			 

Exits the port-profile configuration mode. 			 
 		 

**Step 5**
 

(Optional) show port-profile 		 
 (Optional) 			 

Displays the port-profile configuration. 			 
 		 

**Step 6**
 

(Optional) 			 copy running-config startup-config 		 
 (Optional) 			 

Copies the running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows how to inherit the port profile named adam onto the 		 port profile named test: 		 
```
` switch# **configure terminal** switch(config)# **port-profile test** switch(config-ppm)# **inherit port-profile adam** switch(config-ppm)#`
```
 		 	 
#### Removing a Port 	 Profile from a Range of Interfaces 
 		 

You can remove a 		 port profile from some or all of the interfaces to which you have applied the 		 profile. You do this configuration in the interfaces configuration mode. 		 
 	 
### SUMMARY STEPS
 
 
- 			 configure 				 terminal 		 
- 			 interface [ethernet 				slot/port | 				interface-vlan 				vlan-id | 				port-channel 				number] 		 
- 			 no inherit port-profile 				 				name 		 
- exit 		 
- (Optional) show port-profile 		 
- (Optional) 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 configure 				 terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

 			 interface [ethernet 				slot/port | 				interface-vlan 				vlan-id | 				port-channel 				number] 		 
 			 

Selects the 				range of interfaces. 			 
 		 

**Step 3**
 

 			 no inherit port-profile 				 				name 		 
 			 

Un-assigns the 				specified port profile to the selected interfaces. 			 
 		 

**Step 4**
 

exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 5**
 

(Optional) show port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 6**
 

(Optional) 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows how to unassign the port profile named adam to Ethernet interfaces 7/3 to 7/5, 10/2, and 11/20 to 11/25: 				
```
` switch# **configure terminal** switch(config)# **interface ethernet 7/3-5, 10/2, 11/20-25** switch(config-if)# **no inherit port-profile adam** switch(config-if)#`
```
 			 	 
#### Removing an 	 Inherited Port Profile 
 		 

You can remove an 		 inherited port profile. You do this configuration in the port-profile mode. 		 
 	 
### SUMMARY STEPS
 
 
- configure terminal 		 
- 			 port-profile 				name 		 
- no inherit port-profile 				name 		 
- 			 exit 		 
- (Optional) show port-profile 		 
- (Optional) copy running-config startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 		 
 			 

Enters the 				global configuration mode. 			 
 		 

**Step 2**
 

 			 port-profile 				name 		 
 			 

Enters the 				port-profile configuration mode for the specified port profile. 			 
 		 

**Step 3**
 

no inherit port-profile 				name 		 
 			 

Removes an 				inherited port profile from this port profile. 			 
 		 

**Step 4**
 

 			 exit 		 
 			 

Exits the 				port-profile configuration mode. 			 
 		 

**Step 5**
 

(Optional) show port-profile 		 
 (Optional) 			 

Displays the 				port-profile configuration. 			 
 		 

**Step 6**
 

(Optional) copy running-config startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
##### Example
 		 This example shows 		 how to remove the inherited port profile named adam from the port profile named 		 test: 		 
```
` switch# **configure terminal** switch(config)# **port-profile test** switch(config-ppm)# **no inherit port-profile adam** switch(config-ppm)#`
```
 		 	 
### Configure a link MAC-up timer on DWDM or Dark fiber circuits
 

DWDM and dark fiber links sometimes require adjustment of the MAC-up timer. This adjustment ensures reliable detection of link events. Setting a specific timer can prevent false link flaps. 
 

This procedure describes how to configure MAC-up timers on DWDM or dark fiber circuits.
 
#### Procedure
 
 

**Step 1**
 

Enter global configuration mode. 
 
#### Example:
 
```
`switch# configure terminal switch(config)#`
```
 

**Step 2**
 

Select the interface for the DWDM or dark fiber circuit using the interface type slot/port 
 
#### Example:
 
```
`switch(config)# interface ethernet1/2 switch(config-if)#`
```
 

**Step 3**
 

Set the link MAC-up timer using the link mac-up timer seconds 
 
#### Example:
 
```
`switch(config-if)# link mac-up timer 10`
```
 

The link MAC-up timer range is 0-120.
 
 

**Note**
  

Configure this setting only on DWDM or dark fiber links.
 
 
 

The link MAC-up timer is configured for the selected interface, enabling optimized performance and improved reliability for DWDM or dark fiber circuits. 
 
### Configuring 25G Autonegotiation
 

Autonegotiation allows devices to advertise enhanced modes of operation it possesses via the link segment and to detect corresponding enhanced operational modes that the other devices may be advertising. Autonegotiation provides the means to exchange information between two devices that share a link segment and to automatically configure both devices to take maximum advantage of their abilities. 
 

- [#id_78496] 
- [#id_79207] 
- [#id_77446] 
- [#id_77448] 
#### Guidelines and Limitations for 25G Autonegotiation
 
 
- 

Beginning with Cisco NX-OS Release 9.2(1), autonegotiation on native 25G ports with copper cables is supported on Cisco Nexus N9K-X97160YC-EX, N9K-C93180YC-FX, N9K-C93240YC-FX2 and N9K-C93240YC-FX2-Z switches. 
 
- 

Autonegotiation is not supported on Cisco Nexus N9K-C92300YC switch.
 
- 

Autonegotiation of 25G interfaces is disabled by default
 
- 

Copper-based 25G transceivers require autonegotiation. Enable the command negotiate auto 25000 under a copper 25G interface. The interface may remain down if this parameter is mismatched between each end of the link. 
 
- 

Autonegotiation is not supported on 25G breakout ports.
 
#### FEC selection with 25G Autonegotiation
 
 Table 6. FEC Selection with 25G Autonegotiation 

Hardware
 

FEC based on CR Lengths
 

1m
 

2m
 

3m
 

5m
 

N9K-C93240YC-FX2
 

No FEC
 

No FEC
 

FC-FEC
 

RS-IEEE
 

N9K-C93180YC-FX
 

No FEC
 

No FEC
 

FC-FEC
 

RS-IEEE
 

N9K-C93180YC-EX
 

No FEC
 

No FEC
 

FC-FEC
 

FC-FEC
 

N9K-X97160YC-EX
 

No FEC
 

No FEC
 

FC-FEC
 

FC-FEC
 
 
 

**Note**
 

25G autonegotiation is not supported on Cisco Nexus N9K-C92300YC switch.
 
 
#### Enable Autonegotiation on interfaces
 

Autonegotiation allows interfaces to automatically select the best speed and duplex mode. You must configure autonegotiation at both ends of a 25G native link. 
 

You can enable autonegotiation using the negotiate auto command. 
 

To enable autonegotiation, use these steps.
 
##### Procedure
 
 

**Step 1**
 

Enter global configuration mode. 
 
##### Example:
 
```
`switch# **configure terminal** switch(config)#`
```
 

**Step 2**
 

Select the interface using the interface ethernet port number command. 
 
##### Example:
 
```
`switch# **interface e1/7** switch(config-if)# `
```
 

**Step 3**
 

Enable autonegotiation on the interface using the negotiate auto port speed command. 
 
##### Example:
 
```
`switch(config-if)# **negotiate auto 25000** switch(config-if)# `
```
 
 

**Note**
  

Apply this command to interfaces on both ends of the 25G native link.
 
 
 

Autonegotiation is enabled on the selected interface.
 
##### Example
 

This example shows how to enable autonegotiation on a specified interface.
 
```
` switch# show interface e1/7 st -------------------------------------------------------------------------------- Port Name Status Vlan Duplex Speed Type -------------------------------------------------------------------------------- Eth1/7 -- connected routed full 25G SFP-H25GB-CU1M switch# conf switch(config)# int e1/7 switch(config-if)# negotiate auto 25000 `
```
 
#### Disable Autonegotiation on the interfaces
 

You can disable autonegotiation using the *no negotiate auto* command. To disable autonegotiation, use these steps. 
 
##### Procedure
 
 

**Step 1**
 

Enter global configuration mode.
 
##### Example:
 
```
`switch# **configure terminal** switch(config)#`
```
 

**Step 2**
 

 Select the interface using the interface ethernet port number command. 
 
##### Example:
 
```
`switch# **int e1/7** switch(config-if)# `
```
 

**Step 3**
 

Disable autonegotiation at the interface using the no negotiate auto port speed command. 
 
##### Example:
 
```
` switch(config-if)# **no negotiate auto 25000** switch(config-if)# `
```
 
 

**Note**
  

You must run this command on both ends of the link for proper operation. 
 
 
 

Autonegotiation is disabled on the configured interface. The interface operates at the speed you specified.
 
##### Example
 

This example shows how to disable autonegotiation on an interface.
 
```
` switch# sh int e1/7 st -------------------------------------------------------------------------------- Port Name Status Vlan Duplex Speed Type -------------------------------------------------------------------------------- Eth1/7 -- connected routed full 25G SFP-H25GB-CU1M switch# conf switch(config)# int e1/7 switch(config-if)# no negotiate auto 25000 `
```
 
## Commands for viewing basic interface parameters
 				 

You can verify the basic interface parameters by displaying their values. You can also clear the counters listed when you display the parameter values. 
 				 

These commands display information about basic interface parameters and states.
 				 
 							 								 									 

Command 
 								 								 									 

Purpose 
 								 							 						 							 								 									 

 										 											show cdp all 										 										 									 
 								 								 									 

Displays the CDP status. 
 								 							 							 								 									 

 										 											show interface 											interface 										 										 									 
 								 								 									 

Displays the configured states of one or all interfaces. 
 								 							 							 								 									 

 										* 											 												show interface brief 											 										* 										 									 
 								 								 									 

Displays a table of interface states. 
 								 							 							 								 									 

 										 											show interface status err-disabled 										 										 									 
 								 								 									 

Displays information about error-disabled interfaces. 
 								 							 							 								 									 

 										 											show udld 											interface 										 										 									 
 								 								 									 

Displays the UDLD status for the current interface or all interfaces. 
 								 							 							 								 									 

 										 											show udld global 										 										 									 
 								 								 									 

Displays the UDLD status for the current device. 
 								 							 							 						 
 		 		 
## Monitor interface counters
 

An interface counter is a network monitoring metric that
 
 
- 

records statistics about data packets and errors on a network interface,
 
- 

assists network administrators in identifying and troubleshooting network problems, and
 
- 

enables performance tracking and capacity planning.
 

**Additional information**
 

 Interface counters track input and output packets, errors, discards, and other events per interface. They are essential for diagnosing network issues and for analyzing traffic patterns over time. 
 

You can display and clear interface counters using Cisco NX-OS.
 

- [#task_78182D31B36A44409758FE96B65AC700] 
- [#task_9EE9E21BEEF04CB89DE0C4F157ACD6B6] 
### Configure sampling intervals for statistics 
 			 

Sampling intervals allow you to customize how frequently the switch collects statistics for traffic monitoring.
 			 

You can set up to three sampling intervals for statistics collections on interfaces. Use these steps to configure interface statistic sampling intervals. 
 
#### Procedure
 
 			 

**Step 1**
 

Enter global configuration mode. 						configure terminal 					 				 
 
#### Example:
 					
```
`switch# **configure terminal** switch(config)#`
```
 				 			 

**Step 2**
 

Specify the interface interface using the 						interface ethernet 						slot/port 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **interface ethernet 4/1** switch(config)# `
```
 				 			 

**Step 3**
 

Configure one or more sampling intervals for bitrate and packet rate statistics using the 						load-interval counters [1 | 2 | 3] seconds 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **load-interval counters 1 100** switch(config)#`
```
 				 					 

Each counter uses these default values.
 					 
 						 
- 							 

1: 30 seconds (60 seconds for VLAN) 
 						 						 
- 							 

2: 300 seconds
 						 						 
- 							 

3: Not configured.
 						 					 				 			 

**Step 4**
 

(Optional) View the interface statistics using the 						show interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch(config)# **show interface ethernet 2/2** switch#`
```
 				 			 

**Step 5**
 

Exit interface mode. 				 
 
#### Example:
 					
```
`switch(config-if-range)# **exit** switch(config)# `
```
 				 			 

**Step 6**
 

(Optional) Save the running configuration to startup configuration.
 
#### Example:
 					
```
`switch(config)# **copy running-config startup-config** `
```
 				 		 
 			 

The specified interface now collects traffic statistics using the configured sampling intervals.
 		 
#### Example
 

This example shows 		 how to set the three sample intervals for the Ethernet port 3/1: 		 
 
```
`switch# **configure terminal** switch(config)# **interface ethernet 3/1** switch(config-if)# **load-interval counter 1 60** switch(config-if)# **load-interval counter 2 135** switch(config-if)# **load-interval counter 3 225** switch(config-if)#`
```
 
### Clear the interface counters
 			 

You can clear the Ethernet and management interface counters by using the 					clear counters interface 				 				command. Perform this task from either configuration mode or interface configuration mode. 
 		 
#### Procedure
 
 			 

**Step 1**
 

Clear the interface counters on the interface using the 						clear counters interface [all | ethernet 						slot/port | loopback 						number | mgmt 						number | port channel 						channel-number] 					 command. 
 
#### Example:
 					
```
`switch# **clear counters ethernet 2/1** switch#`
```
 				 					 				 			 

**Step 2**
 

(Optional) Verify the interface status using the 						show interface 						interface 					 					 command. 
 
#### Example:
 					
```
`switch# **show interface ethernet 2/1** switch#`
```
 				 			 

**Step 3**
 

Verify that interface counters are reset using the 						show interface [ethernet 						slot/port | port channel 						channel-number] counters 					 					 command. 
 
#### Example:
 					
```
`switch# **show interface ethernet 2/1 counters**switch#`
```
 				 		 
 			 

The system resets the interface counter statistics for the specified interfaces.
 		 
#### Example
 			 

This example shows 				how to clear the counters on Ethernet port 5/5: 			 
 			
```
`switch# clear counters interface ethernet 5/5 switch#`
```
 		 
## Example: Configuring QSA on Cisco Nexus 9396PX switch
 		 
 			 
- 				 

Using the default 					configuration on port 2/1, all the QSFPs in port group 2/1-6 are brought up 					with a speed of 40G. If there are any QSA modules in port group 2/1-6, they are 					error disabled. 				 
 			 			 
- 				 

Using the 					 						speed-group [ 						10000 						| 						40000] 					 command 					to configure port 2/7, all the QSAs in port group 2/7-12 are brought up with a 					speed of 10G or 40G. If there are any QSFP modules in port group 2/7-12, they 					are error disabled. 				 
 			 		 		 		 

This example shows how 			to configure QSA for the first port in the speed group for a Cisco Nexus 			9396PX: 		 
 		
```
`switch# conf terminal switch(config)# **interface ethernet 2/7** switch(config-if)# **speed-group 10000** 		`
```
 	 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
