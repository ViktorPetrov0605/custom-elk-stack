# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Reflective Relay for Layer 2 Switching [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01100.html`
**Tags:** layer2, vlan, trunk, stp, spanning-tree

---

Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Reflective Relay for Layer 2 Switching [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01100.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.pdf] PDF - Complete Book (3.97 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_01100.pdf] PDF - This Chapter (1.0 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: September 12, 2023 
## Chapter: Configuring Reflective Relay for Layer 2 Switching 
 Chapter Contents 
 
- [#id_75929] Configuring Reflective Relay for Layer 2 Switching 
- [#id_54067] About Reflective Relay 802.1Qbg 
 
- [#id_54078] Reflective Relay Support 
- [#con_1706247] Guidelines and Limitations for Reflective Relay 
- [#task_FF3EE5517D2641C981D78CA8D9980340] Configuring Reflective Relay Using the NX-OS CLI Close 
# Configuring Reflective Relay for Layer 2 Switching
 

- [#id_54067] 
- [#con_1706247] 
- [#task_FF3EE5517D2641C981D78CA8D9980340] 
## About Reflective Relay 802.1Qbg
 

Reflective relay is a tagless approach of IEEE standard 802.1Qbg. It forwards all traffic to an external switch that applies policy and sends the traffic back to the destination or target VM on the server as needed. There is no local switching. For broadcast or multicast traffic, reflective relay provides packet replication to each VM locally on the server. 
 

Reflective relay leverages the external switch for switching features and management capabilities, freeing server resources to support the VMs. Reflective relay applies the policies you configure on the Cisco Nexus switches to traffic between the VMs on the same server. 
 

You can enable reflective relay to turn back traffic out of the same port it came in on. You can enable reflective relay on a Layer 2 physical port or port-channel interface policy using the NX-OS CLI. This feature is disabled by default. 
 

The term Virtual Ethernet Port Aggregator (VEPA) is also used to describe 802.1Qbg functionality.
 

- [#id_54078] 
### Reflective Relay Support
 

Nexus Switches introduces support for Reflective relay in these releases:
 
 Table 1. Feature Support Information 

Nexus Switches
 

Introductory Release
 

N9K-C93180YC-EX
 

N9K-C93180TC-EX
 

Release 7.0(3)I7(1)
 

N9K-C93180YC-FX
 

N9K-C93180TC-FX
 

N9K-C93180YC-EX
 

Release 9.2(1)
 

N9K-C93180YC-FX3
 

N9K-C93108TC-FX3P
 

Release 9.3(5)
 
 
## Guidelines and Limitations for Reflective Relay
 

Reflective relay has these configuration guidelines or limitations: 
 
 
- 

IEEE standard 802.1Qbg tagless approach, known as reflective relay. 
 
- 

Physical domains—virtual domains are not supported.
 
- 

Physical ports and port channels—Does not support Cisco Fabric Extender (FEX) and blade servers. If reflective relay is enabled on an unsupported interface, a fault is raised, and the last valid configuration is retained. Disabling reflective relay on the port clears the fault. 
 
- 

ARP suppression must be disabled before using the reflective relay feature.
 
## Configuring Reflective Relay Using the NX-OS CLI
 

Reflective relay is disabled by default; however, you can enable it on a port or port channel as a Layer 2 interface policy on the switch. In the NX-OS CLI, you can use a template to enable reflective relay on multiple ports or you can enable it on individual ports. 
 
### Procedure
 
 

**Step 1**
 

 configure terminal 
 
### Example:
 
```
`switch# configure terminal switch(config)#`
```
 

Enters global configuration mode. 
 

**Step 2**
 

interface ethernet 1/2 
 
### Example:
 
```
`switch(config)# interface ethernet 1/2 switch(config-if)#`
```
 Enables the port. 

**Step 3**
 

switchport virtual-ethernet-bridge 
 
### Example:
 
```
`switch(config-if)# switchport virtual-ethernet-bridge switch(config-if)#`
```
 

Configures the Layer 2 port as a host port for the reflective relay feature. 
 

**Step 4**
 

[no] switchport virtual-ethernet-bridge 
 
### Example:
 
```
`switch(config-if)# no switchport virtual-ethernet-bridge`
```
 

Enables the reflective relay feature. 
 
 

**Note**
  

The reflective relay feature is only supported on access or trunk ports.
 
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
