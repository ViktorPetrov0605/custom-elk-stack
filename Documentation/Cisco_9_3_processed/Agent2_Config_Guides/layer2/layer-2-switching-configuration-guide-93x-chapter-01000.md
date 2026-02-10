# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Switching Modes [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01000.html`
**Tags:** layer2, vlan, trunk, stp, spanning-tree

---

Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Switching Modes [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01000.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.pdf] PDF - Complete Book (3.97 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01000.pdf] PDF - This Chapter (1.05 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: September 12, 2023 
## Chapter: Configuring Switching Modes 
 Chapter Contents 
 
- [#id_75934] Configuring Switching Modes 
- [#concept_CFF979FF84E84BFB96BCB51615CF605E] Information About 	 Switching Modes 
- [#id_75999] Guidelines and Limitations for Switching Modes 
- [#reference_282250AE22E346EDA1C0FE2FEB3EC40A] Default Settings for 	 Switching Modes 
- [#d1915e219a1635] Configuring Switching Modes 
 
- [#task_5ABBF98519814012B9E67EF7A5A1537C] Enabling 	 Store-and-Forward Switching 
- [#task_3EF8B9A4E0824CCABFF76826F1E3B459] Reenabling Cut-Through Switching Close 
# Configuring Switching Modes
 

- [#concept_CFF979FF84E84BFB96BCB51615CF605E] 
- [#id_75999] 
- [#reference_282250AE22E346EDA1C0FE2FEB3EC40A] 
## Information About 	 Switching Modes 
 

The switching mode 		determines whether the switch begins forwarding the frame as soon as the switch 		has read the destination details in the packet header or waits until the entire 		frame has been received and checked for cyclic redundancy check (CRC) errors 		before forwarding them to the network. 	 
 

The switching mode is 		applicable to all packets being switched or routed through the hardware and can 		be saved persistently through reboots and restarts. 	 
 

The switch operates in 		either of the following switching modes: 	 
 
### Cut-Through 		 Switching Mode 
 		 		 

Cut-through switching mode is enabled by default. Switches operating in cut-through switching mode start forwarding the frame as soon as the switch has read the destination details in the packet header. A switch in cut-through mode forwards the data before it has completed receiving the entire frame. 
 		 

The switching speed 		 in cut-through mode is faster than the switching speed in store-and-forward 		 switching mode. 		 
 	 
### Store-and-Forward Switching Mode
 		 		 

When 		 store-and-forward switching is enabled, the switch checks each frame for cyclic 		 redundancy check (CRC) errors before forwarding them to the network. Each frame 		 is stored until the entire frame has been received and checked. 		 
 		 

Because it waits to 		 forward the frame until the entire frame has been received and checked, the 		 switching speed in store-and-forward switching mode is slower than the 		 switching speed in cut-through switching mode. 		 
 	 
## Guidelines and Limitations for Switching Modes
 

Consider the following guidelines and limitations for each of the switching modes: 
 
### Cut-Through Switching Mode Guidelines and Limitations
 
 
- 

show commands with the internal keyword are not supported. 
 
- 

Packets with FCS errors are not mirrored if SPAN is configured. 
 
- 

Cut-through switching is supported on the Cisco Nexus 9500 Series switch with the 9636PQ line card. 
 
### Store-and-Forward Switching Mode Guidelines and Limitations
 
 
- 

show commands with the internal keyword are not supported. 
 
- 

Packets with FCS errors are dropped. 
 
- 

Packets with FCS errors are not mirrored if SPAN is configured. 
 
- 

The CPU port always operates in store-and-forward mode. Any packets forwarded to the CPU with FCS errors are dropped. 
 
- 

Store-and-forward mode activates automatically for a port when the switch identifies that the port is oversubscribed and the ingress rate is greater than the switching capacity of the egress port. For example, when the port ingress rate is 10 gigabit and the switching capacity of the egress port is 1 gigabit. 
 
 

**Note**
 

The global configuration does not change, even if store-and-forward mode is activated for an oversubscribed port. 
 
 
## Default Settings for 	 Switching Modes 
 		 

Cut-through 		 switching is enabled by default. 		 
 	 

Configuring Switching Modes
 
## Enabling 	 Store-and-Forward Switching 
 		 
 

**Note**
 		 

Enabling 			 store-and-forward switching mode might impact your port-to-port switching 			 latency. 		 
 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure 				 terminal 		 
- switch(config) # 			 switching-mode store-forward 		 
- (Optional) switch(config)# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure 				 terminal 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config) # 			 switching-mode store-forward 		 
 			 

Enables store-and-forward switching mode. 			 
 		 

**Step 3**
 

(Optional) switch(config)# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Saves the change 				persistently through reboots and restarts by copying the running configuration 				to the startup configuration. 			 
 		 
 
### Example
 		 

This example shows how to enable store-and-forward switching: 		 
 		
```
`switch# **configure terminal** switch(config) # **switching-mode store-forward** switch(config) # `
```
 	 
## Reenabling Cut-Through Switching
 

Cut-through switching is enabled by default. To reenable cut-through switching, use the no form of the switching-mode store-forward command. 
 
### SUMMARY STEPS
 
 
- switch# 			 configure 				 terminal 		 
- switch(config) # no switching-mode store-forward 
- (Optional) switch(config)# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure 				 terminal 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config) # no switching-mode store-forward 
 

Disables store-and-forward switching mode. Enables cut-through switching mode. 
 

**Step 3**
 

(Optional) switch(config)# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Saves the change 				persistently through reboots and restarts by copying the running configuration 				to the startup configuration. 			 
 		 
 
### Example
 

This example shows how to reenable cut-through switching: 
 
```
`switch# **configure terminal** switch(config) # **no switching-mode store-forward** switch(config) # `
```
 
 

**Note**
 

The command no switching-mode store-forward is not supported on Cisco Nexus 9800 Series switches as Cut-Through mode is not available on this platform. 
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
