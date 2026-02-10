# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring VTP [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0110.html`
**Tags:** layer2, vlan, trunk, stp, spanning-tree

---

Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring VTP [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0110.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.pdf] PDF - Complete Book (3.97 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0110.pdf] PDF - This Chapter (1.03 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: September 12, 2023 
## Chapter: Configuring VTP 
 Chapter Contents 
 
- [#id_75936] Configuring VTP 
- [#concept_6173D581511F48F8B838DACC03C3556A] Information About VTP 
 
- [#con_1273440] VTP 
- [#concept_B1E8DEB43B7343EAB6FE291549103C11] VTP Overview 
- [#concept_13398A3BC3AB419C93E0E0CCD67886D8] VTP Modes 
- [#concept_92AE43B5177B4B6F8687AE014CD4FAD5] VTP Per Interface 
- [#id_75997] Guidelines and Limitations for Configuring VTP 
- [#con_1274975] Default Settings 
- [#task_1273736] Configuring 	 VTP Close 
# Configuring VTP
 

- [#concept_6173D581511F48F8B838DACC03C3556A] 
- [#id_75997] 
- [#con_1274975] 
- [#task_1273736] 
## Information About VTP
 

VTP is supported for VTP version 1 and 2.
 
 

**Note**
 

You can configure VLANs without actually creating the VLANs. For more details, see [b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0101.html#task_35050AA238434173898A2B49DEEF0724] Configuring a VLAN Before Creating the VLAN. 
 
 

- [#con_1273440] 
- [#concept_B1E8DEB43B7343EAB6FE291549103C11] 
- [#concept_13398A3BC3AB419C93E0E0CCD67886D8] 
- [#concept_92AE43B5177B4B6F8687AE014CD4FAD5] 
### VTP
 		 

VTP is a Layer 2 		 messaging protocol that maintains VLAN consistency by managing the addition, 		 deletion, and renaming of VLANs within a VTP domain. A VTP domain is made up of 		 one or more network devices that share the same VTP domain name and that are 		 connected with trunk interfaces. Each network device can be in only one VTP 		 domain. 		 
 		 

 Layer 2 trunk 		 interfaces, Layer 2 port channels, and virtual port channels (vPCs) support VTP 		 functionality. 		 
 		 

The VTP is disabled 		 by default on the device. You can enable and configure VTP using the 		 command-line interface (CLI). When VTP is disabled, the device does not relay 		 any VTP protocol packets. 		 
 		 
 

**Note**
 		 

VTP worked only in 			 transparent mode in the Cisco Nexus 9000 Series devices, allowing you to extend 			 a VTP domain across the device. 		 
 		 
 		 

When the device is 		 in the VTP transparent mode, the device relays all VTP protocol packets that it 		 receives on a trunk port to all other trunk ports. When you create or modify a 		 VLAN that is in VTP transparent mode, those VLAN changes affect only the local 		 device. A VTP transparent network device does not advertise its VLAN 		 configuration and does not synchronize its VLAN configuration based on received 		 advertisements. 		 
 		 
 

**Note**
 		 

VLAN 1 is required 			 on all trunk ports used for switch interconnects if VTP is supported in the 			 network. Disabling VLAN 1 from any of these ports prevents VTP from functioning 			 properly. 		 
 		 
 		 	 
### VTP Overview
 

VTP allows each router or LAN device to transmit advertisements in frames on its trunk ports. These frames are sent to a multicast address where they can be received by all neighboring devices. They are not forwarded by normal bridging procedures. An advertisement lists the sending device's VTP management domain, its configuration revision number, the VLANs which it knows about, and certain parameters for each known VLAN. By hearing these advertisements, all devices in the same management domain learn about any new VLANs that are configured in the transmitting device. This process allows you to create and configure a new VLAN only on one device in the management domain, and then that information is automatically learned by all the other devices in the same management domain. 
 

Once a device learns about a VLAN, the device receives all frames on that VLAN from any trunk port by default, and if appropriate, forwards them to each of its other trunk ports, if any. This process prevents unnecessary VLAN traffic from being sent to a device. 
 

VTP also publishes information about the domain and the mode in a shared local database that can be read by other processes such as Cisco Discovery Protocol (CDP). 
 
### VTP Modes
 

VTP is supported in these modes:
 
 
- 

Transparent—Allows you to relay all VTP protocol packets that it receives on a trunk port to all other trunk ports. When you create or modify a VLAN that is in VTP transparent mode, those VLAN changes affect only the local device. A VTP transparent network device does not advertise its VLAN configuration and does not synchronize its VLAN configuration based on received advertisements. 
 

If VTP is in transparent mode, you can configure VLAN long names of up to 128 characters.
 
### VTP Per Interface
 

VTP allows you to enable or disable the VTP protocol on a per-port basis to control the VTP traffic. When a trunk is connected to a switch or end device, it drops incoming VTP packets and prevents VTP advertisements on this particular trunk. By default, VTP is enabled on all the switch ports. 
 
## Guidelines and Limitations for Configuring VTP
 

 VTP has the following configuration guidelines and limitations: 
 
 
- 

show commands with the internal keyword are not supported. 
 
- 

In SNMP, the vlanTrunkPortVtpEnabled object indicates whether the VTP feature is enabled or not. The status of the vlanTrunkPortVtpEnabled object aligns with the output of the show vtp trunk interface eth a/b command. 
 
- 

VTP advertisements are not sent out on Cisco Nexus Fabric Extender ports.
 
- 

VTP pruning is not possible with transparent devices. When there are transparent devices in a VTP domain, VTP pruning has to be disabled. If VTP pruning is not disabled on the neighboring devices, the Cisco Nexus devices will not learn any MACs from the neighboring device because the VLANs are pruned/disabled on the links pointing to the Nexus. 
 
## Default Settings
 		 

This table lists the default settings for VTP parameters. 		 
 
 Table 1. Default VTP Parameters 				 

Parameters 				 
 				 				 

Default 				 
 				 				 

 VTP 				 
 				 				 

Disabled 				 
 				 				 

 VTP Mode 				 
 				 				 

Transparent 				 
 				 				 

 VTP Domain 				 
 				 				 

blank 				 
 				 				 

 VTP Version 				 
 				 				 

1 				 
 				 				 				 				 				 				 

VTP 				 per Interface 
 				 				 

Enabled 				 
 				 
 	 
## Configuring 	 VTP 
 		 

You can configure 		 VTP on Cisco Nexus 9000 devices. 		 
 		 
 

**Note**
 		 

VLAN 1 is required 			 on all trunk ports used for switch interconnects if VTP is used in transparent 			 mode in the network. Disabling VLAN 1 from any of these ports prevents VTP from 			 functioning properly in transparent mode. 		 
 		 
 		 
 

**Note**
 		 

VTP worked only in 			 transparent mode. 		 
 		 
 	 
### SUMMARY STEPS
 
 
- 			 				config 				 t 			 			 		 
- 			 				feature 				 vtp 			 		 
- 			 				vtp 				 domain 				domain-name 			 			 		 
- 			 				vtp 				 version {1 				| 				2} 			 		 
- 			 				vtp 				 file 				file-name 			 			 		 
- 			 				vtp 				 password 				password-value 			 		 
- 			 				exit 			 		 
- (Optional) 			 				show vtp 				 status 			 		 
- (Optional) 			 				show vtp 				 counters 			 			 		 
- (Optional) 			 				show vtp 				 interface 			 		 
- (Optional) 			 				show vtp 				 password 			 		 
- (Optional) 			 				copy 				 running-config startup-config 			 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 			 				config 				 t 			 			 		 
 
### Example:
 			 
```
`switch# config t switch(config)#`
```
 		 			 

Enters 				configuration mode. 			 
 		 

**Step 2**
 

 			 				feature 				 vtp 			 		 
 
### Example:
 			 
```
`switch(config)# feature vtp switch(config)#`
```
 		 			 

Enables VTP on 				the device. The default is disabled. 			 
 		 

**Step 3**
 

 			 				vtp 				 domain 				domain-name 			 			 		 
 
### Example:
 			 
```
`switch(config)# vtp domain accounting`
```
 		 			 

Specifies the 				name of the VTP domain that you want this device to join. The default is blank. 				 			 
 		 

**Step 4**
 

 			 				vtp 				 version {1 				| 				2} 			 		 
 
### Example:
 			 
```
`switch(config)# vtp version 2`
```
 		 			 

Sets the VTP 				version that you want to use. The default is version 1. 			 
 		 

**Step 5**
 

 			 				vtp 				 file 				file-name 			 			 		 
 
### Example:
 			 
```
`switch(config)# vtp file vtp.dat`
```
 		 			 

Specifies the 				ASCII filename of the IFS file system file where the VTP configuration is 				stored. 			 
 		 

**Step 6**
 

 			 				vtp 				 password 				password-value 			 		 
 
### Example:
 			 
```
`switch(config)# vtp password cisco`
```
 		 			 

Specifies the 				password for the VTP administrative domain. 			 
 		 

**Step 7**
 

 			 				exit 			 		 
 
### Example:
 			 
```
`switch(config)# exit switch#`
```
 		 			 

Exits the 				configuration submode. 			 
 		 

**Step 8**
 

(Optional) 			 				show vtp 				 status 			 		 
 
### Example:
 			 
```
`switch# show vtp status`
```
 		 (Optional) 			 

Displays 				information about the VTP configuration on the device, such as the version, 				mode, and revision number. 			 
 		 

**Step 9**
 

(Optional) 			 				show vtp 				 counters 			 			 		 
 
### Example:
 			 
```
`switch# show vtp counters`
```
 		 (Optional) 			 

Displays 				information about VTP advertisement statistics on the device. 			 
 		 

**Step 10**
 

(Optional) 			 				show vtp 				 interface 			 		 
 
### Example:
 			 
```
`switch# show vtp interface`
```
 		 (Optional) 			 

Displays the 				list of VTP-enabled interfaces. 			 
 		 

**Step 11**
 

(Optional) 			 				show vtp 				 password 			 		 
 
### Example:
 			 
```
`switch# show vtp password`
```
 		 (Optional) 			 

Displays the 				password for the management VTP domain. 			 
 		 

**Step 12**
 

(Optional) 			 				copy 				 running-config startup-config 			 		 
 
### Example:
 			 
```
`switch(config)# copy running-config startup-config`
```
 		 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
### 

### 

- [https://mycase2-stage.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
