# Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Flex Links [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0100.html`
**Tags:** layer2, vlan, trunk, stp, spanning-tree

---

Cisco Nexus 9000 Series NX-OS Layer 2 Switching Configuration Guide, Release 9.3(x) - Configuring Flex Links [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0100.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.pdf] PDF - Complete Book (3.97 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x_chapter_0100.pdf] PDF - This Chapter (1.07 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: September 12, 2023 
## Chapter: Configuring Flex Links 
 Chapter Contents 
 
- [#id_92388] Configuring Flex Links 
- [#id_92289] Information About Flex Links 
 
- [#id_92290] Flex Links 
- [#id_92291] Preemption 
- [#id_98415] Multicast 
- [#id_92362] Guidelines and Limitations 
- [#id_92363] Default Settings 
- [#id_92364] Configuring Flex Links 
 
- [#id_92367] Configuring Flexlinks 
- [#id_92373] Configuring Flex Link Preemption 
- [#id_92383] Verifying Configuration Close 
# Configuring Flex Links
 

This chapter describes how to configure Flex Links on the Cisco NX-OS 9000 Series Switches. Flex Links are a pair of interfaces that provide a mutual backup. 
 

The chapter includes the following sections:
 

- [#id_92289] 
- [#id_92362] 
- [#id_92363] 
- [#id_92364] 
- [#id_92383] 
## Information About Flex Links
 

This section includes the following topics:
 

- [#id_92290] 
- [#id_92291] 
- [#id_98415] 
### Flex Links
 

Flex Links are a pair of a Layer 2 interfaces (switchports or port channels), where one interface is configured to act as a backup to the other. 
 

This feature provides an alternative solution to the Spanning Tree Protocol (STP), allowing users to turn off STP and still provide basic link redundancy. You generally configure Flex Links in networks where customers do not want to run STP on the switch. When you configure STP on the switch, it is not necessary to configure Flex Links because STP already provides link-level redundancy or backup. 
 
 

**Note**
 

STP is enabled by default on network node interfaces (NNIs). It is disabled on enhanced network interfaces (ENIs), but you can enable it. STP is not supported on user network interfaces (UNIs). 
 
 

You configure Flex Links on one Layer 2 interface (the active link) by assigning another Layer 2 interface as the Flex Link or backup link. When one of the links is up and forwarding traffic, the other link is in standby mode, ready to begin forwarding traffic if the other link shuts down. At any given time, only one of the interfaces is in the linkup state and forwarding traffic. If the primary link shuts down, the standby link starts forwarding traffic. When the active link comes back up, it goes into standby mode and does not forward traffic. STP is disabled on Flex Link interfaces. 
 

In Figure **Flex Links Configuration Example**, ports 1 and 2 on switch A are connected to uplink switches B and C. Because they are configured as Flex Links, only one of the interfaces is forwarding traffic; the other is in standby mode. If port 1 is the active link, it begins forwarding traffic between port 1 and switch B; the link between port 2 (the backup link) and switch C is not forwarding traffic. If port 1 goes down, port 2 comes up and starts forwarding traffic to switch C. When port 1 comes back up, it goes into standby mode and does not forward traffic; port 2 continues forwarding traffic. 
 
### Preemption
 

You can also choose to configure a preemption mechanism, specifying the preferred port for forwarding traffic. In the following figure, for example, you can configure the Flex Link pair with preemption mode so that after port 1 comes back up in the scenario, if it has greater bandwidth than port 2, port 1 begins forwarding after pre-empt delay (default pre-empt delay is 35 seconds); and port 2 becomes the standby. You do this by entering the interface configuration switchport backup interface preemption mode bandwidth and switchport backup interface preemption delay commands. 
 Figure 1. Flex Links Configuration Example 

If a primary (forwarding) link or the standby link goes down, a trap notifies the network management stations. Flex Links are supported only on Layer 2 ports and port channels in either trunk or access mode. They are not supported on VLANs or Layer 3 ports. 
 
### Multicast
 

When a Flex Link interface is learned as an mrouter port, the standby (non-forwarding) interface is also co-learned as an mrouter port if the link is up. This co-learning is for internal software state maintenance and has no relevance with respect to IGMP operations or hardware forwarding unless multicast fast-convergence is enabled. With multicast fast-convergence configured, the co-learned mrouter port is immediately added to the hardware. Flex Link supports multicast fast convergence for IPv4 IGMP. 
 
## Guidelines and Limitations
 

Consider the following guidelines and limitations when configuring Flex Links:
 
 
- 

Flex links are supported on the following platforms : Cisco Nexus 9300-EX, 9300-FX , 9300-FX2 , C9364C switches.
 
- 

Flex Links are supported on Cisco Nexus 9300-FX, 9300-FX2, and 9348GC-FXP switches with IPv4 multicast.
 
- 

Because the Spanning Tree Protocol is implicitly disabled on Flex Link interfaces, ensure that you do not configure any other redundant paths in the same topology to prevent loops. In addition, configure the corresponding links to upstream switches by using the spanning-tree port type normal command so they do not get blocked by Bridge Assurance. 
 
- 

Flex Links are designed for uplink interfaces, which are typically configured as trunk ports. As a link backup mechanism, a Flex Link pair must have the same configuration characteristics, including the same switchport mode and list of allowed VLANs. Port-profile makes a convenient tool for syncing up such configurations for the Flex Link pair. Flex Link does not require that the two interfaces have the same configurations. However, long term mismatches in configurations may result in forwarding problems, particularly during failover. 
 
- 

Flex Links cannot be configured on the following interface types:
 
 
- 

Layer 3 interfaces
 
- 

SPAN destinations
 
- 

Port channel members
 
- 

Interfaces configured with Private VLANs
 
- 

Interfaces in end node mode
 
- 

Layer 2 multi-path
 
- 

You can configure only one Flex Link backup link for any active link and it must be a different interface from the active interface. 
 
- 

An interface can belong to only one Flex Link pair; it can be a backup link for only one active link.
 
- 

Neither of the links can be a port that belongs to an EtherChannel. However, you can configure two port channels (EtherChannel logical interfaces) as Flex Links, and you can configure a port channel and a physical interface as Flex Links, with either the port channel or the physical interface as the active link. 
 
- 

A backup link does not have to be the same type (Ethernet or port channel) as the active link. However, we recommend that you configure both Flex Links with similar characteristics so that there are no loops or changes in behavior if the standby link begins to forward traffic. 
 
- 

STP is disabled on Flex Link ports. A Flex Link port does not participate in STP, even if the VLANs present on the port are configured for STP. When STP is not enabled, be sure that there are no loops in the configured topology. 
 
 

**Note**
 

STP is available only on NNIs or ENIs.
 
 
- 

Do not configure any STP features (for example, PortFast, and BPDU Guard) on Flex Links ports.
 
- 

Default interface CLI on the flex link pair (active and standby) is not supported. When either breakout / in is performed in either primary or standby interface, flex link configuration is removed. 
 
- 

vPC is not supported. Flex Link is used in place of vPC where configuration simplicity is desired and there is no need for active-active redundancy. 
 
- 

Beginning with Cisco NX-OS Release 9.3(5), the Flex Link feature is supported on Cisco Nexus 9300-GX, N9K-C93108TC-FX3H, and N9K-C93108TC-FX3P platform switches. 
 
- 

Beginning with Cisco NX-OS Release 9.3(7), the Flex Link feature is supported on Cisco N9K-C93180YC-FX3 platform switch.
 
## Default Settings
 
 

Parameters
 

Default
 

Flex links
 

Disabled
 

Multicast Fast-Convergence
 

Disabled
 

Flex links preemption mode
 

 Off
 

Flex links preemption delay
 

35 seconds
 
 
## Configuring Flex Links
 

- [#id_92367] 
- [#id_92373] 
### Configuring Flexlinks
 

You can configure a pair of layer 2 interfaces (switch ports or port channels) as Flex Link interfaces, where one interface is configured to act as a backup to the other. 
 
#### Before you begin
 

Review the Guidelines and Limitations for this feature. (See [#id_92362] Guidelines and Limitations.) 
 
### SUMMARY STEPS
 
 
- configure terminal 
- feature flexlink 
- interface{ ethernet slot/ port | port-channel channel no 
- switchport backup interface {ethernet slot/ port | port-channel channel-no} [multicast fast-convergence] 
- (Optional) end 
- (Optional) show interface switchport backup 
- (Optional) copy running-config startup config 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 
 

Enter global configuration mode.
 

**Step 2**
 

feature flexlink 
 

Enables Flex Link.
 

**Step 3**
 

interface{ ethernet slot/ port | port-channel channel no 
 

Specifies the Ethernet or port channel interface and enters interface configuration mode.
 

**Step 4**
 

switchport backup interface {ethernet slot/ port | port-channel channel-no} [multicast fast-convergence] 
 

Specifies a physical layer 2 interface (Ethernet or port channel) as the backup interface in a Flex Link pair. When one link is forwarding traffic the other interface is in standby mode. 
 
 
- 

ethernet slot/port—Specifies the backup Ethernet interface. The slot number is 1 and the port number is from 1 to 48.
 
- 

port-channel port-channel-no—Specifies the backup port channel interface. The port-channel-no number is from 1 to 4096.
 
- 

multicast—Specifies the multicast parameters.
 
- 

fast-convergence—Configures fast convergence on the backup interface.
 

**Step 5**
 

(Optional) end 
 (Optional) 

Return to privileged EXEC mode.
 

**Step 6**
 

(Optional) show interface switchport backup 
 (Optional) 

Verifies the configuration. 
 

**Step 7**
 

(Optional) copy running-config startup config 
 (Optional) 

 Save your entries in the switch startup configuration file.
 
 
#### Example
 

This example shows how to configure an Ethernet switchport backup pair: Ethernet 1/1 is active interface, Ethernet 1/2 is the backup interface: 
 
```
`switch(config)# feature flexlink switch(config)# interface ethernet 1/1 switch(config-if)# switchport backup interface ethernet 1/2 switch(config-if)# exit switch(config)# interface port-channel300 switch(config-if)# switchport backup interface port-channel301 switch(config-if)# show ip igmp snooping mrouter Type: S - Static, D - Dynamic, V - vPC Peer Link, I - Internal,C - Co-learned, U - User Configured Vlan Router-port Type Uptime Expires 200 Po300 D 13:13:47 00:03:15 200 Po301 DC 13:13:47 00:03:15`
```
 

This example shows how to configure the port channel switchport backup pair with multicast fast convergence:
 
```
`switch(config)# interface port-channel10 switch(config-if)# switchport backup interface port-channel20 multicast fast-convergence`
```
 

This example shows an example of multicast convergence with a pair of Flex Link interfaces: po305 and po306. A general query received on po305 makes it an mrouter port and po306 as co-learned. 
 
```
`switch(config)# interface po305 Switch(config-if)# switchport backup interface po306 switch# show ip igmp snooping mrouter Type: S - Static, D - Dynamic, V - vPC Peer Link, I - Internal, C - Co-learned Vlan Router-port Type Uptime Expires 4 Po300 D 00:00:12 00:04:50 4 Po301 DC 00:00:12 00:04:50`
```
 
### Configuring Flex Link Preemption
 

Configure a preemption scheme for the Flex Links pair (active and backup links).
 
#### Before you begin
 

Review the Guidelines and Limitations for this feature. (See [#id_92362] Guidelines and Limitations.) 
 

Define and enable the Flex Link. (See [#id_92367] Configuring the Flex Link.) 
 

Determine what preemption mode, if any, you want to assign to the port. (See [#id_92291] Preemption.) 
 
### SUMMARY STEPS
 
 
- configure terminal 
- interface ethernet slot/port 
- switchport backup interface ethernet slot / port 
- switchport backup interface ethernet slot / port preemption mode {forced | bandwidth | off} 
- switchport backup interface ethernet slot / port preemption delay delay-time 
- (Optional) end 
- (Optional) show interface switchport backup 
- (Optional) copy running-config startup config 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

configure terminal 
 

Enter global configuration mode.
 

**Step 2**
 

interface ethernet slot/port 
 

Specify the interface, and enters interface configuration mode. The interface can be a physical Layer 2 interface or a port channel (logical interface). 
 

**Step 3**
 

switchport backup interface ethernet slot / port 
 

Configures a physical Layer 2 interface (or port channel) as part of a Flex Link pair with the interface. When one link is forwarding traffic, the other interface is in standby mode. 
 

**Step 4**
 

switchport backup interface ethernet slot / port preemption mode {forced | bandwidth | off} 
 

Configures a physical Layer 2 interface (Ethernet or port channel) as part of a flex link pair. When one link is forwarding traffic the other interface is in standby mode. 
 
 
- 

preemption—Configures a preemption scheme for a backup interface pair.
 
- 

mode—Specifies the preemption mode.
 

Configure a preemption mechanism and delay for a Flex Link pair. You can configure the preemption as: 
 
 
- 

forced —the active interface always preempts the backup. 
 
- 

bandwidth —the interface with the higher bandwidth always acts as the active interface. 
 
- 

off —no preemption happens from active to backup. 
 
 

**Note**
  

During a bandwidth preemption mode, only bandwidth changes are considered, speed changes are ignored.
 
 

**Step 5**
 

switchport backup interface ethernet slot / port preemption delay delay-time 
 

Configure the delay time until a port preempts another port. The delay-time range is from 1 to 300 seconds. The default preemption delay is 35 seconds. 
 
 

**Note**
  

Setting a delay time only works with forced and bandwidth modes.
 
 

**Step 6**
 

(Optional) end 
 (Optional) 

Return to privileged EXEC mode.
 

**Step 7**
 

(Optional) show interface switchport backup 
 (Optional) 

Verifies the configuration. 
 

**Step 8**
 

(Optional) copy running-config startup config 
 (Optional) 

 Save your entries in the switch startup configuration file.
 
 
#### Example
 

This example shows how to sets the preemption mode to forced, sets the delay time to 50, and verifies the configuration:
 
```
`switch(config)# configure terminal switch(config)# interface ethernet 1/48 switch(config-if)# switchport backup interface ethernet 1/4 preemption mode forced switch(config-if)# switchport backup interface ethernet 1/4 preemption delay 50 switch(config-if)# end switch# show interface switchport backup detail Switch Backup Interface Pairs: Active Interface Backup Interface State ------------------------------------------------------------------------ Ethernet1/48 Ethernet1/4 Active Down/Backup Down Preemption Mode : forced Preemption Delay : 50 seconds Multicast Fast Convergence : Off Bandwidth : 10000000 Kbit (Ethernet1/48), 10000000 Kbit (Ethernet1/4)`
```
 
## Verifying Configuration
 
 

Command
 

Purpose
 

show interface switchport backup 
 

Displays information about all switchport Flex Link interfaces.
 show interface switchport backup detail 

Displays detailed information about all switchport Flex Link interfaces.
 

show running-config backup 
 

show startup-config backup 
 

Displays the running or startup configuration for backup interfaces.
 

show running-config flexlink 
 

show startup-config flexlink 
 

Displays the running or startup configuration for flex link interfaces.
 
 

This example shows summary configuration for the Flex Link pair:
 
```
`9k-203-Pip(config)# show interface switchport backup Switch Backup Interface Pairs: Active Interface Backup Interface State ------------------------------------------------------------------------ Ethernet1/9 port-channel103 Active Standby/Backup Up Ethernet1/12 Ethernet1/13 Active Up/Backup Standby Ethernet1/21 port-channel203 Active Up/Backup Standby Ethernet1/24 Ethernet1/25 Active Up/Backup Standby port-channel301 port-channel302 Active Down/Backup Up k-203-Pip(config)# show interface switchport backup detail Switch Backup Interface Pairs: Active Interface Backup Interface State ------------------------------------------------------------------------ Ethernet1/9 port-channel103 Active Standby/Backup Up Preemption Mode : bandwidth Preemption Delay : 1 seconds Multicast Fast Convergence : On Bandwidth : 1000000 Kbit (Ethernet1/9), 2000000 Kbit (port-channel103) ..`
```
 

This example shows information about all switchport Flex Link interfaces:
 
```
`switch# show interface switchport backup Switch Backup Interface Pairs: Active Interface Backup Interface State ------------------------------------------------------------------------ Ethernet1/1 Ethernet1/2 Active Down/Backup Down Ethernet1/8 Ethernet1/45 Active Down/Backup Down Ethernet1/48 Ethernet1/4 Active Down/Backup Down port-channel10 port-channel20 Active Down/Backup Up port-channel300 port-channel301 Active Down/Backup Down`
```
 

This example shows details about all switchport Flex Link interfaces:
 
```
`switch# show interface switchport backup detail Switch Backup Interface Pairs: Active Interface Backup Interface State ------------------------------------------------------------------------ Ethernet1/1 Ethernet1/2 Active Down/Backup Down Preemption Mode : off Multicast Fast Convergence : Off Bandwidth : 10000000 Kbit (Ethernet1/1), 10000000 Kbit (Ethernet1/2) Ethernet1/8 Ethernet1/45 Active Down/Backup Down Preemption Mode : forced Preemption Delay : 10 seconds Multicast Fast Convergence : Off Bandwidth : 10000000 Kbit (Ethernet1/8), 10000000 Kbit (Ethernet1/45) Ethernet1/48 Ethernet1/4 Active Down/Backup Down Preemption Mode : forced Preemption Delay : 50 seconds Multicast Fast Convergence : Off Bandwidth : 10000000 Kbit (Ethernet1/48), 10000000 Kbit (Ethernet1/4) port-channel10 port-channel20 Active Down/Backup Up Preemption Mode : forced Preemption Delay : 10 seconds Multicast Fast Convergence : Off Bandwidth : 100000 Kbit (port-channel10), 10000000 Kbit (port-channel20) port-channel300 port-channel301 Active Down/Backup Down Preemption Mode : off Multicast Fast Convergence : Off Bandwidth : 100000 Kbit (port-channel300), 100000 Kbit (port-channel301)`
```
 

This example shows the running configuration for backup interfaces: 
 
```
`switch# show running-config backup !Command: show running-config backup !Time: Sun Mar 2 03:05:17 2014 version 6.0(2)A3(1) feature flexlink interface port-channel10 switchport backup interface port-channel20 preemption mode forced switchport backup interface port-channel20 preemption delay 10 interface port-channel300 switchport backup interface port-channel301 interface Ethernet1/1 switchport backup interface Ethernet1/2 interface Ethernet1/8 switchport backup interface Ethernet1/45 preemption mode forced switchport backup interface Ethernet1/45 preemption delay 10 interface Ethernet1/48 switchport backup interface Ethernet1/4 preemption mode forced switchport backup interface Ethernet1/4 preemption delay 50 `
```
 

This example shows the startup configuration for backup interfaces:
 
```
`switch# show startup-config backup !Command: show startup-config backup !Time: Sun Mar 2 03:05:35 2014 !Startup config saved at: Sun Mar 2 02:54:58 2014 version 6.0(2)A3(1) feature flexlink interface port-channel10 switchport backup interface port-channel20 preemption mode forced switchport backup interface port-channel20 preemption delay 10 interface Ethernet1/8 switchport backup interface Ethernet1/45 preemption mode forced switchport backup interface Ethernet1/45 preemption delay 10`
```
 

This example shows the startup configuration for backup interfaces:
 
```
`switch# show startup-config backup !Command: show startup-config backup !Time: Sun Mar 2 03:05:35 2014 !Startup config saved at: Sun Mar 2 02:54:58 2014 version 6.0(2)A3(1) feature flexlink interface port-channel10 switchport backup interface port-channel20 preemption mode forced switchport backup interface port-channel20 preemption delay 10 interface Ethernet1/8 switchport backup interface Ethernet1/45 preemption mode forced switchport backup interface Ethernet1/45 preemption delay 10`
```
 

This example shows the running configuration of Flex Link:
 
```
`switch# show running-config flexlink !Command: show running-config flexlink !Time: Sun Mar 2 03:11:49 2014 version 6.0(2)A3(1) feature flexlink interface port-channel10 switchport backup interface port-channel20 preemption mode forced interface port-channel300 switchport backup interface port-channel301 interface port-channel305 switchport backup interface port-channel306 interface Ethernet1/1 switchport backup interface Ethernet1/2 interface Ethernet1/8 switchport backup interface Ethernet1/45 preemption mode forced switchport backup interface Ethernet1/45 preemption delay 10 interface Ethernet1/48 switchport backup interface Ethernet1/4 preemption mode forced switchport backup interface Ethernet1/4 preemption delay 50 `
```
 

This example shows the startup configuration of Flex Link:
 
```
`switch# show startup-config flexlink !Command: show startup-config flexlink !Time: Sun Mar 2 03:06:00 2014 !Startup config saved at: Sun Mar 2 02:54:58 2014 version 6.0(2)A3(1) feature flexlink interface port-channel10 switchport backup interface port-channel20 preemption mode forced switchport backup interface port-channel20 preemption delay 10 interface Ethernet1/8 switchport backup interface Ethernet1/45 preemption mode forced switchport backup interface Ethernet1/45 preemption delay 10`
```
 
 

**Note**
 

Before using the no feature flexlink , all flexlink pair configuration must be disabled. 
 

In order to ensure, user will be promoted with a confirmation message when user execute no feature flexlink as shown below: 
 
```
`"WARNING!!! Please remove all flexlink configuration before disabling feature flexlink. `
```
 
```
`Failure to do so may put ports in inconsistent state. Do you want to proceed? Y/N :"`
```
 

This message is prompted only if DME is enabled in the system.
 

If the user chooses to proceed with this command, flexlink peer configuration will remain in the running configuration.
 

This, in turn, may cause system inconsistency in the ports, that are a part of flexlink configuration. 
 

Once system is in an inconsistent state, the user needs to recover the system.
 

For recovery, the user needs to re-configure using the command feature flexlink and remove each interface pair configuration using the command no switchport backup interface Ethernet x/y . 
 

Once all the pair configurations are removed, the user can execute no feature flexlink . 
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
