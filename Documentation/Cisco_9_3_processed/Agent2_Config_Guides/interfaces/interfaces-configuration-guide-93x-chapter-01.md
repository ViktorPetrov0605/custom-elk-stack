# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - New and Changed Information [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01.html`
**Tags:** interfaces, ethernet, port-channels, switchport

---

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - New and Changed Information [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.65 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01.pdf] PDF - This Chapter (1.0 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: March 28, 2022 
## Chapter: New and Changed Information 
 Chapter Contents 
 
- [#topic_6F1DD8CD03D5484FA303A09BB8849119] New and Changed Information 
- [#concept_ptm_nvz_hdb] New and Changed Information Close 
# New and Changed Information
 

This chapter provides release-specific information for each new and changed feature in the Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide. 
 

- [#concept_ptm_nvz_hdb] 
## New and Changed Information
 
 Table 1. New and Changed Features for Release 9.3(x) 

Feature 
 

Description 
 

Changed in Release 
 

Where Documented 
 

Layer 3 router over vPC 
 

Added creation of syslog when peer-gateway and layer 3 peer-router commands are not configured on both the vPC peers in the vPC domain. 
 

9.3(9)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01000.html#id_75907] Guidelines and limitations
 BFD multi hop/single hop session 

A new command bfd [multihop | singlehop] is introduced. 
 

9.3(6)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01111.html#task_96067332E3E942478326B57E96D56578] Configuring BFD on BGP
 

 Multicast and Broadcast Subinterface Counters
 

Added support for Cisco Nexus N9K-C9336C-FX2 and N9K-C93240YC-FX2 switches.
 

9.3(6)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#Cisco_Task.dita_c13b3291-a17d-4451-b251-3506bd9d5912] Configuring Subinterface Multicast and Broadcast Counters
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#id_75904] Guidelines and Limitations for Layer 3 Interfaces
 IP Unnumbered on SVI Secondary VLAN on the Gateway 

Added support for IP unnumbered on the secondary SVI in the gateway on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches. 
 

9.3(6)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#id_56338] Configuring IP Unnumbered on SVI Secondary VLAN on the Gateway
 100M Half-Duplex support 

Added support for Cisco N9K-C9348GC-FXP and N9K-C92348GC-X switches.
 

9.3(6)
 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html#id_75899] Guidelines and Limitations NAT 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01011.html#id_75844] Configuring FINRST and SYN Timers
 Sub interface support range from 1-4094 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#task_F08479C86D3E4CA8B273795FA337A734] Configuring a Subinterface on a Routed Interface Selective Q-in-Q with Multiple Provider VLANs 

Added support for Selective Q-in-Q with Multiple Provider VLANs on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches. 
 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html#id_96465] Guidelines and Limitations for Selective Q-in-Q with Multiple Provider VLANs
 IPv6 Flow Label Hashing 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#Cisco_Task.dita_4f4808fb-3c2b-4654-9dea-df65d5057f98] Configuring ECMP Load Balancing IP Load Sharing Options 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#Cisco_Task.dita_4f4808fb-3c2b-4654-9dea-df65d5057f98] Configuring ECMP Load Balancing SVI and Subinterface Ingress/Egress Unicast Counters 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#Cisco_Task.dita_694cfb0f-ab0e-4346-8bab-0c2c0066a44d] Configuring SVI and Subinterface Ingress/Egress Unicast Counters
 Multiple VRFs for Tunnel Decapsulation 

Added support for Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX and N9K-C9364C-GX switches.
 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01001.html#id_75908] Guidelines and Limitations
 Breakout Support Added 2x50G breakout support for Cisco Nexus N9K-C93600CD-GX and N9K-C9364C-GX devices. 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#id_10498] Breakout port support on Cisco Nexus switches
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#Cisco_Concept.dita_a32e509a-0d1f-4254-ab0d-1b32f5bb64be] Breakout features on Cisco Nexus 9000 C93600CD-GX switches
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#Cisco_Concept.dita_f57c1331-aa4d-48ee-a867-305fec14a94f] Breakout considerations for Cisco Nexus 9000 C9364C-GX switch
 Optics Support: 10G BASE-T SFP+ Added support for 10G BASE-T SFP+ on Cisco Nexus N9K-C93240YC-FX2, N9K-C93180YC-EX, N9K-C93180YC-FX and N9K-C93360YC-FX2 devices. 

9.3(5)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html#Cisco_Concept.dita_f6613a1e-8769-49b5-b21f-db076d2c5c69] Cisco SFP-10G-T-X modules
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html#Cisco_Task.dita_465f2b68-ba30-49a3-9fd6-471fbb9a6ecf] Configure media-type for SFP-10G-T-X transceivers
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html#Cisco_Concept.dita_6448d50d-1347-4e58-9976-07f9347f50a9] Verify media-type
 Unidirectional Ethernet Added support for Unidirectional Ethernet on Cisco Nexus 9500 switches with X97160YC-EX line cards. 

9.3(5)
 

[m-n9000-configuring-unidirectional-ethernet.html#Cisco_Concept.dita_f4beb40a-1e5f-408a-ba9d-4a2bdc6f5fac] Unidirectional Ethernet
 

[m-n9000-configuring-unidirectional-ethernet.html#Cisco_Concept.dita_53bc3510-956c-43e2-a180-255e67dbeae4] Best practices for Unidirectional Ethernet configuration
 

[m-n9000-configuring-unidirectional-ethernet.html#Cisco_Task.dita_baee0504-0f9b-4ad6-8fba-8df314156496] Configure Unidirectional Ethernet
 

Cisco Nexus 9364C-GX Switch Breakout
 

Added 4x10G and 4x25G breakout support for Cisco Nexus N9K-C9364C-GX Switches.
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#Cisco_Concept.dita_f57c1331-aa4d-48ee-a867-305fec14a94f] Breakout considerations for Cisco Nexus 9000 C9364C-GX switch
 

Cisco Nexus 93600CD-GX Switch Breakout
 

Added breakout support for Cisco Nexus 93600CD-GX Switches
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#id_10498] Breakout port support on Cisco Nexus switches
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html#Cisco_Concept.dita_a32e509a-0d1f-4254-ab0d-1b32f5bb64be] Breakout features on Cisco Nexus 9000 C93600CD-GX switches
 SVI and Subinterface Ingress/Egress Unicast Counters Added support for SVI and subinterface unicast counters on Cisco Nexus 9300-EX, 9300-FX/FX2 switches; and Cisco Nexus 9500 series switches with X9700-EX|X9700-FX line cards. 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#Cisco_Task.dita_694cfb0f-ab0e-4346-8bab-0c2c0066a44d] Configuring SVI and Subinterface Ingress/Egress Unicast Counters
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#id_75904] Guidelines and Limitations for Layer 3 Interfaces
 GTP Tunnel Load Balancing Added support for Cisco Nexus 9500 platform switches with 9700-EX and 9700-FX line cards. 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_63445] GTP Tunnel Load Balancing
 IPv6 Multihop BFD Added support for Cisco Nexus 9300-GX switches. 

9.3(3)
 

 

SVI Statistics on Layer 3
 

Added support to display SVI statistics on layer 3 on Cisco Nexus 3100 series switches. 
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html#Cisco_Task.dita_6847b4a7-31f3-4217-8229-4b309c674a0c] Configuring SVI TCAM Region
 

IP Load sharing enhancements
 

GRE inner header hashing
 

ECMP symmetric hashing
 

Added support for IP load sharing enhancements, GRE inner header hashing and ECMP symmetric hashing on Cisco Nexus 9364C-GX and 93600CD-GX Switches. 
 

9.3(3)
 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#Cisco_Task.dita_4f4808fb-3c2b-4654-9dea-df65d5057f98] Configuring ECMP Load Balancing Combined Access Port Feature set Added support for Selective Q-in-Q including catch-all, vPC, PVLAN, Storm Control 9.3(3) 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html#id_96465] Guidelines and Limitations for Selective Q-in-Q with Multiple Provider VLANs
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html#Cisco_Task.dita_737d9bda-c91f-4944-8113-588dc6ba4b7e] Configuring Combined Access Port Feature set
 Multiple VRF support on tunnel decap 

Added support for multiple IP-in-IP/GRE tunnel interfaces on a same Cisco Nexus device that can be sourced from or destined to the same IP address across different VRFs. 
 

Added support for Cisco Nexus 93180YC-FX and 9300-GX platforms.
 9.3(3) 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01001.html#id_75908] Guidelines and Limitations
 

Bidirectional Forwarding Detection
 

Added support for Cisco Nexus 9364C-GX, 9316D-GX, and 93600CD-GX platforms.
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01111.html#id_75905] Guidelines and Limitations
 

Port-channel symmetric hashing 
 

Added support for Cisco Nexus 9300-GX platform.
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations
 

Port-channel hash based on GRE inner IP header and GTP TEID
 

Added support for Cisco Nexus 9300-GX platform.
 

9.3(3)
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_63445] GTP Tunnel Load Balancing
 

[b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations
 ECMP symmetric hashing Introduced this feature. 9.3(1) [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations Port-channel symmetric hashing Added support for Cisco Nexus 9300-EX and 9300-FX/FX2 switches and -EX and -FX line cards. 9.3(1) [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations Port-channel hash based on GRE inner IP header Added support for this feature. 9.3(1) 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations 
 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#concept_D1EAFA3071194B5B829D17368AFC27A6] Load Balancing Using Port Channels 
 ECMP hash based on the GRE inner IP header Added support for this feature. 9.3(1) 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#id_113874] Guidelines and Limitations 
 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#concept_D1EAFA3071194B5B829D17368AFC27A6] Load Balancing Using Port Channels 
 

LACP fast timer support during system switchover
 Added support for Cisco Nexus 9500 platform switches with -EX and -FX line cards. 9.3(1) 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html#concept_301253F755A44385B6B4E6F8470A30B4] LACP Fast Timers 
 

System jumbo MTU size
 

Added support for configuring an MTU size of up to 9216 bytes on management interfaces.
 9.3(1) 

 [b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html#id_114490] Set the system jumbo MTU size 
 

BFD multihop for BGP IPv6
 

Introduced this feature.
 9.3(1) 

 
 
 

 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
