# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Layer 2 Switching [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_011.html`
**Tags:** layer2, vlan, trunk, stp, spanning-tree

---

Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Layer 2 Switching [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
- [#fw-content] Skip to content 
- [#] Skip to search 
- [#fw-footer-v2] Skip to footer 

- [https://www.cisco.com/site/us/en/index.html] 
- [/c/en/us/products/index.html] 
- [https://www.cisco.com/site/us/en/solutions/index.html] 
- [/c/en/us/support/index.html] 
- [/c/en/us/training-events.html] 
- [//www.cisco.com/c/en/us/about/sitemap.html] 
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
# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x)
 		 	 Bias-Free Language 
### Bias-Free Language
 

The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html] Learn more about how Cisco is using Inclusive Language.
 Book Contents Book Contents 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_preface_00.html] Preface 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01.html] New and Changed Information 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_010.html] Overview 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_011.html] Configuring Layer 2 Switching 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0100.html] Configuring Flex Links 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0101.html] Configuring VLANs 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0110.html] Configuring VTP 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0111.html] Configuring Private VLANs Using NX-OS 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01000.html] Configuring Switching Modes 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01001.html] Configuring Rapid PVST+ Using Cisco NX-OS 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01010.html] Configuring MST Using Cisco NX-OS 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01011.html] Configuring STP Extensions Using Cisco NX-OS 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01100.html] Configuring Reflective Relay for Layer 2 Switching 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01110.html] Configuring Traffic Storm Control 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_011.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.pdf] PDF - Complete Book (3.97 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_011.pdf] PDF - This Chapter (1.14 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: September 12, 2023 
## Chapter: Configuring Layer 2 Switching 
 Chapter Contents 
 
- [#id_75938] Configuring Layer 2 Switching 
- [#id_101039] Information About Layer 2 Switching 
 
- [#con_1125315] Layer 2 Ethernet Switching Overview 
 
- [#con_1125322] Switching Frames 	 Between Segments 
- [#con_1125342] Building the Address 	 Table and Address Table Changes 
- [#con_1489391] Consistent MAC 	 Address Tables on the Supervisor and on the Modules 
- [#concept_t14_ggk_vgb] High Availability for Switching 
- [#id_101044] Prerequisites for Configuring MAC Addresses 
- [#id_101047] Default Settings for Layer 2 Switching 
- [#mac-move-loop-detection] MAC Move Loop Detection 
- [#generating-syslog-error-messages] Generating Syslog Error Messages 
- [#id_101048] Configuring Layer 2 Switching by Steps 
 
- [#task_1153294] Configuring a Static 	 MAC Address 
- [#disabling-mac-address-learning-on-system] Disabling MAC Address Learning on System 
- [#task_B51E9D96F4E84055B999530F3AC4D5E1] Disabling MAC 	 Address Learning on Layer 2 Interfaces 
- [#task_1126206] Configuring the 	 Aging Time for the MAC Table 
- [#task_1707747] Checking Consistency 	 of MAC Address Tables 
- [#task_1126804] Clearing Dynamic 	 Addresses from the MAC Table 
- [#task_ynk_jdv_l4b] Configuring MAC Address Limits 	 
- [#id_100852] Configuring L2 Heavy Mode 
- [#id_101051] Verifying the Layer 2 Switching Configuration 
- [#id_101052] Configuration Example for Layer 2 Switching 
- [#id_101053] Additional References for Layer 2 Switching -- CLI Version Close 
# Configuring Layer 2 Switching
 

- [#id_101039] 
- [#concept_t14_ggk_vgb] 
- [#id_101044] 
- [#id_101047] 
- [#mac-move-loop-detection] 
- [#generating-syslog-error-messages] 
- [#id_101048] 
- [#id_101051] 
- [#id_101052] 
- [#id_101053] 
## Information About Layer 2 Switching
 
 

**Note**
 

See the [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html] Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, for information on creating interfaces. 
 
 

You can configure Layer 2 switching ports as access or trunk ports. Trunks carry the traffic of multiple VLANs over a single link and allow you to extend VLANs across an entire network. All Layer 2 switching ports maintain MAC address tables. 
 
 

**Note**
 

See the [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/high-availability-and-redundancy/configuration/guide/b-cisco-nexus-9000-nx-os-High-availability-and-redundancy-guide-93x.html] Cisco Nexus 9000 Series NX-OS High Availability and Redundancy Guide, for complete information on high-availability features. 
 
 

- [#con_1125315] 
### Layer 2 Ethernet Switching Overview
 		 			 

The device supports simultaneous, parallel connections between Layer 2 Ethernet segments. Switched connections between Ethernet segments last only for the duration of the packet. New connections can be made between different segments for the next packet. 
 			 

The device solves congestion problems caused by high-bandwidth devices and a large number of users by assigning each device (for example, a server) to its own collision domain. Because each LAN port connects to a separate Ethernet collision domain, servers in a switched environment achieve full access to the bandwidth. 
 			 

Because collisions cause significant congestion in Ethernet networks, an effective solution is full-duplex communication. Typically, 10/100-Mbps Ethernet operates in half-duplex mode, which means that stations can either receive or transmit. In full-duplex mode, which is configurable on these interfaces, two stations can transmit and receive at the same time. When packets can flow in both directions simultaneously, the effective Ethernet bandwidth doubles. 			 
 		 	 

- [#con_1125322] 
- [#con_1125342] 
- [#con_1489391] 
#### Switching Frames 	 Between Segments 
 		 

Each LAN port on a 		 device can connect to a single workstation, server, or to another device 		 through which workstations or servers connect to the network. 		 
 		 

To reduce signal 		 degradation, the device considers each LAN port to be an individual segment. 		 When stations connected to different LAN ports need to communicate, the device 		 forwards frames from one LAN port to the other at wire speed to ensure that 		 each session receives full bandwidth. 		 
 		 

 To switch frames 		 between LAN ports efficiently, the device maintains an address table. When a 		 frame enters the device, it associates the media access control (MAC) address 		 of the sending network device with the LAN port on which it was received. 		 
 	 
#### Building the Address 	 Table and Address Table Changes 
 		 

The device 		 dynamically builds the address table by using the MAC source address of the 		 frames received. When the device receives a frame for a MAC destination address 		 not listed in its address table, it floods the frame to all LAN ports of the 		 same VLAN except the port that received the frame. When the destination station 		 replies, the device adds its relevant MAC source address and port ID to the 		 address table. The device then forwards subsequent frames to a single LAN port 		 without flooding all LAN ports. 		 
 		 

You can configure 		 MAC addresses, which are called static MAC addresses, to statically point to 		 specified interfaces on the device. These static MAC addresses override any 		 dynamically learned MAC addresses on those interfaces. You cannot configure 		 broadcast 		 addresses as static MAC addresses. The static MAC entries are retained 		 across a reboot of the device. 		 
 		 

You must manually 		 configure identical static MAC addresses on both devices connected by a virtual 		 port channel (vPC) peer link. The MAC address table display is enhanced to 		 display information on MAC addresses when you are using vPCs. 		 
 		 

See the [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html] Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide for information about vPCs. 
 		 

The address table 		 can store a number of MAC address entries depending on the hardware I/O module. 		 The device uses an aging mechanism, defined by a configurable aging timer, so 		 if an address remains inactive for a specified number of seconds, it is removed 		 from the address table. 		 
 	 
#### Consistent MAC 	 Address Tables on the Supervisor and on the Modules 
 		 

Optimally, all the 		 MAC address tables on each module exactly match the MAC address table on the 		 supervisor. When you enter the 		 show 			 forwarding consistency l2 command or the 		 show 			 consistency-checker l2 command, the device displays discrepant, 		 missing, and extra MAC address entries. 		 
 	 
## High Availability for Switching
 			 

You can upgrade or downgrade the software seamlessly, with respect to classical Ethernet switching. If you have configured static MAC addresses on Layer 3 interfaces, you must unconfigure those ports in order to downgrade the software. 
 			 
 

**Note**
 				 

See the [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/high-availability-and-redundancy/configuration/guide/b-cisco-nexus-9000-nx-os-High-availability-and-redundancy-guide-93x.html] Cisco Nexus 9000 Series NX-OS High Availability and Redundancy Guide, for complete information on high availability features. 
 			 
 		 
## Prerequisites for Configuring MAC Addresses
 

MAC addresses have the following prerequisites: 
 
 
- 

You must be logged onto the device. 
 
- 

If necessary, install the Advanced Services license. 
 
## Default Settings for Layer 2 Switching
 

This table lists the default setting for Layer 2 switching parameters. 
 
 Table 1. Default Layer 2 Switching Parameters 

Parameters 
 

Default 
 

 Aging time 
 

1800 seconds 
 
 
## MAC Move Loop Detection
 

Cisco Nexus 9000 Series switches leverage L2FM for software MAC learning (and, subsequently, loop detection). If a host (MAC address) moves between two interfaces within the same VLAN, it would trigger a MAC move. If there are a large number of such MAC moves in a short duration of time, the control plane of the switch and the CPU performance could get impacted. L2FM protects the switch from such scenarios by disabling MAC learning on the specific VLAN once the number of MAC moves for the corresponding MAC address exceeds a threshold. 
 

For Broadcom ASIC based switches, the MAC move learn disable threshold criteria is when a single MAC address moves 10 or more times in a duration of 1 second within the same VLAN. 
 

For Cisco Nexus 9300-EX/FX/FX2/FX3/GX switches and Cisco Nexus 9500 switches with 9700-EX/FX/GX line cards, the MAC move learn disable threshold criteria is when a single MAC address moves 10 or more times in 10 seconds within the same VLAN. 
 

Once the threshold limit is hit, all new MAC learning on the corresponding VLAN gets disabled for a period of 120 seconds. After 120 seconds, new MAC learning is re-enabled on that VLAN. There is no impact of this on the rest of the VLANs on the switch. 
 
## Generating Syslog Error Messages
 To see MAC move notifications in syslogs, follow the below steps: 
### Procedure
 
   Command or Action Purpose 

**Step 1**
 

 config t 
 
### Example:
 
```
`switch# config t switch(config)#`
```
 

Enters configuration mode. 
 

**Step 2**
 

logging level l2fm 5 
 
### Example:
 
```
`switch(config)# logging level l2fm 5`
```
 

Enables logging of all L2FM events from level 5 up to the highest severity events.
 

**Step 3**
 

(Optional) mac address-table notification mac-move 
 
### Example:
 
```
`switch(config)# mac address-table notification mac-move`
```
 (Optional) 

Enables MAC move notification on the switch.
 
 

**Note**
  
 
- 

MAC move notification is enabled by default. 
 
- 

This command ensures that the syslog for L2FM detect displays when there is a MAC address move.
 
 
 Following are the sample generated syslog messages: 
 
- 

When MAC move is detected:
 

2023 Nov 29 21:42:04 N-3164Q-40G %L2FM-4-L2FM_MAC_MOVE2: Mac 0003.0001.005d in vlan 500 has moved from Eth1/24 to Eth1/63
 
- 

When MAC learning on VLAN is disabled:
 

2023 Nov 29 21:23:29 N-3164Q-40G %L2FM-2-L2FM_MAC_FLAP_DISABLE_LEARN: Disabling learning in vlan 500 for 120s due to too many mac moves
 
- 

When MAC learning on VLAN is re-enabled:
 

2023 Nov 29 21:23:19 N-3164Q-40G %L2FM-2-L2FM_MAC_FLAP_RE_ENABLE_LEARN: Re-enabling learning in vlan 500
 
### Example
 In order to check if the MAC addresses move, enter the command:
```
`switch# show mac address-table notification mac-move MAC Move Notify Triggers: 1206 Number of MAC Addresses added: 944088 Number of MAC Addresses moved: 265 Number of MAC Addresses removed: 943920 `
```
 
 

**Note**
 

The following are the possible causes for MAC moves:
 
 
- 

MAC addresses move because of server NIC teaming and moving between Active-Active, Active-Standby states, etc.
 
- 

MAC addresses move because the source of the data is physically moved across all switches while STP states are converged and in correct states. 
 
- 

Due to loops in the network.
 
 
## Configuring Layer 2 Switching by Steps
 
 

**Note**
 

If you are familiar with the Cisco IOS CLI, be aware that the Cisco NX-OS commands for this feature might differ from the Cisco IOS commands that you would use. 
 
 

- [#task_1153294] 
- [#disabling-mac-address-learning-on-system] 
- [#task_B51E9D96F4E84055B999530F3AC4D5E1] 
- [#task_1126206] 
- [#task_1707747] 
- [#task_1126804] 
- [#task_ynk_jdv_l4b] 
- [#id_100852] 
### Configuring a Static 	 MAC Address 
 		 

You can configure MAC addresses, which are called static MAC addresses, to statically point to specified interfaces on the device. These static MAC addresses override any dynamically learned MAC addresses on those interfaces. You cannot configure broadcast or multicast addresses as static MAC addresses. 
 	 
### SUMMARY STEPS
 
 
- 			 				config 				 t 			 		 
- 			 				mac 				 address-table static 				 				mac-address 				vlan 				 				vlan-id {[drop 				| 				 interface 				{type 				 slot/port} | 				 port-channel 				 				number]} 			 		 
- 			 				exit 			 		 
- (Optional) 			 				show mac 				 address-table static 			 			 		 
- (Optional) 			 				copy 				 running-config startup-config 			 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 				config 				 t 			 		 
 
#### Example:
 			 
```
`switch# config t switch(config)#`
```
 		 			 

Enters configuration mode.
 		 

**Step 2**
 

 			 				mac 				 address-table static 				 				mac-address 				vlan 				 				vlan-id {[drop 				| 				 interface 				{type 				 slot/port} | 				 port-channel 				 				number]} 			 		 
 
#### Example:
 			 
```
`switch(config)# mac address-table static 1.1.1 vlan 2 interface ethernet 1/2`
```
 		 			 

Specifies a static MAC address to add to the Layer 2 MAC address table.
 					 
 

**Note**
  						 						 

Use the drop option to drop all traffic that is going to the configured MAC address in the specified VLAN. 
 						 

MAC static drop condition is ignored for routed traffic egressing the SVI corresponding to the VLAN where the mac static drop is configured. 
 						 

This issue only impacts routed traffic (MAC drop configuration in the vlan associated with outbound SVI). This does not apply to bridged traffic where traffic ingressing 9K egresses in the same VLAN (L2 forwarded). 
 					 
 		 

**Step 3**
 

 			 				exit 			 		 
 
#### Example:
 			 
```
`switch(config)# exit switch#`
```
 		 			 

Exits the configuration mode.
 		 

**Step 4**
 

(Optional) 			 				show mac 				 address-table static 			 			 		 
 
#### Example:
 			 
```
`switch# show mac address-table static`
```
 		 (Optional) 			 

Displays the 				static MAC addresses. 			 
 		 

**Step 5**
 

(Optional) 			 				copy 				 running-config startup-config 			 		 
 
#### Example:
 			 
```
`switch# copy running-config startup-config`
```
 		 (Optional) 			 

Copies the running configuration to the startup configuration.
 		 
 
#### Example
 		 

This example shows how to put a static entry in the Layer 2 MAC address table:
 		
```
`switch# **config t** switch(config)# **mac address-table static 1.1.1 vlan 2 interface ethernet 1/2** switch(config)#`
```
 	 
### Disabling MAC Address Learning on System 
 

You can now disable and re-enable MAC address learning on system. 
 
### SUMMARY STEPS
 
 
- switch# 			 configure 				 terminal 		 
- switch(config-if)# [no] mac-learn disable 
- switch(config-if)# clear mac address-table dynamic 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure 				 terminal 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config-if)# [no] mac-learn disable 
 

Disables MAC address learning on the switch. 
 

The no form of this command re-enables MAC address learning on the switch. 
 

**Step 3**
 

switch(config-if)# clear mac address-table dynamic 
 

Clears the MAC address table for the switch. 
 
 

**Important**
  After disabling MAC address learning on the switch, ensure that you clear the MAC address table. 
 
 
### Disabling MAC 	 Address Learning on Layer 2 Interfaces 
 		 

You can now disable 		 and re-enable MAC address learning on Layer 2 interfaces. 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure 				 terminal 		 
- switch(config)# 			 interface 				type 				 				slot/port 		 
- switch(config-if)# 			 [no] switchport mac-learn 				 disable 		 
- switch(config-if)# 			 clear mac address-table 				 dynamic interface 				type 				slot/port 			 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure 				 terminal 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config)# 			 interface 				type 				 				slot/port 		 
 			 

Enters the 				interface configuration mode for the specified interface. 			 
 		 

**Step 3**
 

switch(config-if)# 			 [no] switchport mac-learn 				 disable 		 
 			 

Disables MAC 				address learning on Layer 2 interfaces. 			 
 			 

The 				no form of this 				command re-enables MAC address learning on Layer 2 interfaces. 			 
 			 
 

**Note**
  						 

In Warp mode, the Cisco Nexus 3500 switch does not flood Layer 3 traffic to the VLAN in which the port configured using switchport mac-learn disable is present, and the traffic is dropped. In Normal mode, the switch should flood the Layer 3 traffic to this VLAN. 
 					 
 		 

**Step 4**
 

switch(config-if)# 			 clear mac address-table 				 dynamic interface 				type 				slot/port 			 		 
 			 

Clears the MAC 				address table for the specified interface. 			 
 			 
 

**Important**
  After disabling MAC address learning on an interface, ensure 				that you clear the MAC address table. 			 
 		 
 
#### Example
 		 

This example shows 		 how to disable MAC address learning on Layer 2 interfaces: 		 
 		
```
`switch# **configure terminal** switch(config)# **interface ethernet 1/4** switch(config-if)# **switchport mac-learn disable** switch(config-if)# **clear mac address-table dynamic interface ethernet 1/4**`
```
 		

This example shows 		 how to re-enable MAC address learning on Layer 2 interfaces: 		 
 		
```
`switch# **configure terminal** switch(config)# **interface ethernet 1/4** switch(config-if)# **no switchport mac-learn disable** `
```
 	 
### Configuring the 	 Aging Time for the MAC Table 
 		 

You can configure 		 the amount of time that a MAC address entry (the packet source MAC address and 		 port on which that packet was learned) remains in the MAC table, which contains 		 the Layer 2 information. 		 
 		 
 

**Note**
 		 

 MAC addresses are 			 aged out up to two times the configured MAC address table aging timeout. 		 
 		 
 		 
 

**Note**
 		 

You can also 			 configure the MAC aging time in interface configuration mode or VLAN 			 configuration mode. 		 
 		 
 	 
### SUMMARY STEPS
 
 
- 			 				config 				 t 			 		 
- 			 				mac 				 address-table aging-time 				 				seconds 				 			 		 
- 			 				exit 			 		 
- (Optional) 			 				show mac 				 address-table aging-time 			 		 
- (Optional) 			 				copy 				 running-config startup-config 			 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 				config 				 t 			 		 
 
#### Example:
 			 
```
`switch# config t switch(config)#`
```
 		 			 

Enters 				configuration mode. 			 
 		 

**Step 2**
 

 			 				mac 				 address-table aging-time 				 				seconds 				 			 		 
 
#### Example:
 			 
```
`switch(config)# mac address-table aging-time 600`
```
 		 			 

Specifies the 				time before an entry ages out and is discarded from the Layer 2 MAC address 				table. The range is from 120 to 918000; the default is 1800 seconds. Entering 				the value 0 disables the MAC aging. 			 
 		 

**Step 3**
 

 			 				exit 			 		 
 
#### Example:
 			 
```
`switch(config)# exit switch#`
```
 		 			 

Exits the 				configuration mode. 			 
 		 

**Step 4**
 

(Optional) 			 				show mac 				 address-table aging-time 			 		 
 
#### Example:
 			 
```
`switch# show mac address-table aging-time`
```
 		 (Optional) 			 

Displays the 				aging time configuration for MAC address retention. 			 
 		 

**Step 5**
 

(Optional) 			 				copy 				 running-config startup-config 			 		 
 
#### Example:
 			 
```
`switch# copy running-config startup-config`
```
 		 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
#### Example
 		 

This example shows 		 how to set the ageout time for entries in the Layer 2 MAC address table to 600 		 seconds (10 minutes): 		 
 		
```
`switch# **config t** switch(config)# **mac address-table aging-time 600** switch(config)#`
```
 	 
### Checking Consistency 	 of MAC Address Tables 
 		 

You can check the 		 match between the MAC address table on the supervisor and all the modules. 		 
 		 		 	 
### SUMMARY STEPS
 
 
- 					show consistency-checker l2 module <slot_number> 					 
### DETAILED STEPS
 
 Command or Action Purpose 

 					show consistency-checker l2 module <slot_number> 					 
 
#### Example:
 					
```
`switch# show consistency-checker l2 module 7 switch#`
```
 				 					 				 					 

Displays the discrepant, missing, and extra MAC addresses between the supervisor and the specified module. 
 				 
 
#### Example
 		 

This example shows 		 how to display discrepant, missing, and extra entries in the MAC address tables 		 between the supervisor and the specified module: 		 
 		
```
`switch# **show consistency-checker l2 module 7** switch#`
```
 	 
### Clearing Dynamic 	 Addresses from the MAC Table 
 		 

 You can clear all 		 dynamic Layer 2 entries in the MAC address table. (You can also clear entries 		 by designated interface or VLAN.) 		 
 	 
### SUMMARY STEPS
 
 
- 			 				clear mac 				 address-table dynamic 				 {address 				 				mac_addr} {interface [ethernet 				slot/port | port-channel 				channel-number]} {vlan 				vlan_id} 			 		 
- (Optional) 			 				show mac 				 address-table 			 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 				clear mac 				 address-table dynamic 				 {address 				 				mac_addr} {interface [ethernet 				slot/port | port-channel 				channel-number]} {vlan 				vlan_id} 			 		 
 
#### Example:
 			 
```
` switch# clear mac address-table dynamic `
```
 		 			 

Clears the 				dynamic address entries from the MAC address table in Layer 2. 			 
 		 

**Step 2**
 

(Optional) 			 				show mac 				 address-table 			 		 
 
#### Example:
 			 
```
`switch# show mac address-table`
```
 		 (Optional) 			 

Displays the MAC 				address table. 			 
 		 
 
#### Example
 		 

This example shows 		 how to clear the dynamic entries in the Layer 2 MAC address table: 		 
 		
```
`switch# **clear mac address-table dynamic** switch# `
```
 	 
### Configuring MAC Address Limits 	 
 
### SUMMARY STEPS
 
 			 
- 					 						config t 					 				 			 			 
- 					 						mac address-table limit 						vlan 						vlan-id 						limit -value 					 				 			 			 
- 					 						exit 					 				 			 
- (Optional) 					 						copy running-config startup-config 					 				 		 
### DETAILED STEPS
 
   Command or Action Purpose 			 

**Step 1**
 

 					 						config t 					 				 
 
#### Example:
 					
```
`switch# config t switch(config)#`
```
 				 					 

Enters configuration mode. 
 				 			 			 

**Step 2**
 

 					 						mac address-table limit 						vlan 						vlan-id 						limit -value 					 				 
 
#### Example:
 					
```
`switch(config-vlan)# mac address-table limit vlan 40 108`
```
 				 					 

Specifies the VLAN to which the MAC address limits should be applied. 
 					 					 				 			 			 

**Step 3**
 

 					 						exit 					 				 
 
#### Example:
 					
```
`switch(config)# exit switch#`
```
 				 					 

Exits the configuration mode. 
 				 			 

**Step 4**
 

(Optional) 					 						copy running-config startup-config 					 				 
 
#### Example:
 					
```
`switch# copy running-config startup-config`
```
 				 (Optional) 					 

Copies the running configuration to the startup configuration. 
 				 		 
 
### Configuring L2 Heavy Mode
 

The purpose of this feature is to increase the current 92k MAC address scale to 200k by carving out a new L2-heavy template, changing FP tile hardware resource allocations, making necessary control plane changes and ISSU restore support to accommodate new scale. 
 
 

Command
 

Purpose
 

sh system routing mode 
 

Shows the configured and applied mode
 

system routing template-l2-heavy 
 

Enables 200K MAC. 200K MAC is enabled only when this mode is configured and the system is reloaded.
 

Use **no** form of this command to to disable this feature. 
 
 

**Note**
  

Beginning with Cisco NX-OS Release 10.2(2)F, 200K MAC is supported on Cisco N9K-9332D-GX2B platform switches.
 
 

sh run | i system 
 

Runs the applied mode
 
 

**Guidelines & Limitations:**
 
 
- 

This feature is supported for Layer 2 unidimensional scale only. 
 
- 

SVI, Layer 3 interface, and VXLAN VLANs are not supported.
 
- 

Beginning with Cisco NX-OS Release 9.2(3), this feature is supported on the following platforms: N9K-C9264PQ, N9K-C9272Q, N9K-C9236C, N9K-C92300YC, N9K-C92304QC, N9K-C9232C, N9K-C92300YC and 9300-EX 
 

Following is an example for configuring L2 heavy mode:
 
```
`switch (config)# sh system routing mode switch# Configured System Routing Mode: L2 Heavy switch# Applied System Routing Mode: L2 Heavy switch# switch# show run | i system switch# system routing template-l2-heavy switch#`
```
 
## Verifying the Layer 2 Switching Configuration
 

To display Layer 2 switching configuration information, perform one of the following tasks: 
 
 

 Command 
 

Purpose 
 

 show mac address-table 
 

Displays information about the MAC address table. 
 

 show mac address-table limit 
 

Displays information about the limits set for the MAC address table. 
 

 show mac address-table aging-time 
 

Displays information about the aging time set for the MAC address entries.
 

 show mac address-table static 
 

Displays information about the static entries on the MAC address table. 
 

 show interface [interface] mac-address 
 

Displays the MAC addresses and the burn-in MAC address for the interfaces. 
 

show forwarding consistency l2 {module} 
 

Displays discrepant, missing, and extra MAC addresses between the tables on the module and the supervisor. 
 
 
## Configuration Example for Layer 2 Switching
 

 The following example shows how to add a static MAC address and how to modify the default global aging time for MAC addresses: 

```
`switch# **configure terminal** switch(config)# **mac address-table static 0000.0000.1234 vlan 10 interface ethernet 2/15** switch(config)# **mac address-table aging-time 120**`
```
 
## Additional References for Layer 2 Switching -- CLI Version
 
### Related Documents
 
 

 Related Topic 
 

Document Title 
 

 Static MAC addresses 
 

 Cisco Nexus 9000 Series NX-OS Security Configuration Guide 
 

 Interfaces 
 

 Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide 
 

 High availability 
 

 Cisco Nexus 9000 Series NX-OS High Availability and Redundancy Guide 
 

 System management 
 

 Cisco Nexus 9000 Series NX-OS System Management Configuration Guide 
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
