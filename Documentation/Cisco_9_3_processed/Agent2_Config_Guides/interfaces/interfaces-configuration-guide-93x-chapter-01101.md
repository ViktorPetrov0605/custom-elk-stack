# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring IP TCP MSS [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01101.html`
**Tags:** interfaces, ethernet, port-channels, switchport

---

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring IP TCP MSS [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01101.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.65 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01101.pdf] PDF - This Chapter (1.02 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: March 28, 2022 
## Chapter: Configuring IP TCP MSS 
 Chapter Contents 
 
- [#id_76554] Configuring IP TCP MSS 
- [#id_75492] Information About IP TCP MSS 
- [#id_75495] Default Settings for IP TCP MSS 
- [#id_75496] Guidelines and Limitations for IP TCP MSS 
- [#id_75518] Configuring IP TCP MSS 
 
- [#id_75504] Setting the MSS for TCP Connections 
- [#id_75505] Removing a Set IP TCP MSS 
- [#id_75526] Example: Setting the MSS for TCP Connections 
- [#id_75527] Example: Removing a Set IP TCP MSS 
- [#id_75498] Verifying IP TCP MSS Close 
# Configuring IP TCP MSS
 

- [#id_75492] 
- [#id_75495] 
- [#id_75496] 
- [#id_75518] 
- [#id_75498] 
## Information About IP TCP MSS
 

The IP TCP Maximum Segment Size (MSS) feature enables a switch to set a maximum segment size for all TCP connections that originate or terminate at a Cisco Nexus 9000 Series switch. The MSS in a TCP header field is the maximum data size or payload that a host can send or receive in a single segment. By default, a Cisco Nexus 9000 Series switch sets the MSS value to 536 bytes for IPv4 TCP connections and 1240 bytes for IPv6 TCP connections. This default value is set by the switch during the initial TCP connection establishment. 
 

The switch from which the TCP connection originates will always set the MSS to the user-configured MSS or the difference between the route interface MTU and the protocol header, whichever is lower. Thus, Host A sends a SYN packet with the proposed MSS of 1460 bytes to Host B. After receiving the SYN packet with the proposed MSS, Host B sends a SYN-ACK packet to Host A, accepting the proposed MSS value for the TCP connection. Host A sends an ACK packet to Host B, setting the MSS value to 1460 for the TCP connection. 
 
## Default Settings for IP TCP MSS
 
 Table 1. Default Settings for IP TCP MSS Parameter Default Setting IP TCP MSS 

536 bytes for IPv4 TCP connections
 

1240 bytes for IPv6 TCP connections
 
 
## Guidelines and Limitations for IP TCP MSS
 

If the MSS has to be set to a value that is more than 1460 bytes for IPv4 TCP connections, the corresponding MTU value should be set to the required MSS value plus 40 bytes. If the MSS has to be set to a value that is more than 1440 bytes for IPv6 TCP connections, the corresponding MTU value should be set to the required MSS value plus 60 bytes. 
 
## Configuring IP TCP MSS
 

 [#id_75504] Setting the MSS for TCP Connections 
 

 [#id_75505] Removing a Set IP TCP MSS 
 

- [#id_75504] 
- [#id_75505] 
- [#id_75526] 
- [#id_75527] 
### Setting the MSS for TCP Connections
 
#### Before you begin
 
### SUMMARY STEPS
 
 
- switch# configure terminal 
- switch(config)# ip tcp mss <bytes> 
- switch# show ip tcp mss 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# configure terminal 
 

Enter global configuration mode
 

**Step 2**
 

switch(config)# ip tcp mss <bytes> 
 

Set a maximum segment size.
 

**Step 3**
 

switch# show ip tcp mss 
 

Display the configured IP TCP MSS.
 
 

Example: Running Configuration
 
#### Example
 

This example shows a running configuration, followed by a verification command that displays the configured IP TCP MSS:
 
```
`configure terminal ip tcp mss 5000 Setting TCP MSS to 5000 bytes switch# show ip tcp mss TCP MSS value 5000 bytes`
```
 
### Removing a Set IP TCP MSS
 
### SUMMARY STEPS
 
 
- switch# configure terminal 
- switch(config)# no ip tcp mss 
- switch# show ip tcp mss 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# configure terminal 
 

Enter global configuration mode
 

**Step 2**
 

switch(config)# no ip tcp mss 
 

Remove the configured IP TCP MSS and set the IP TCP MSS to default values.
 

**Step 3**
 

switch# show ip tcp mss 
 

Display the configured IP TCP MSS.
 
 

Example: Running Configuration
 
#### Example
 

This example shows a running configuration, followed by a verification command that displays the configured IP TCP MSS:
 
```
`configure terminal no ip tcp mss 5000 Setting default MSS value is 536 bytes switch# show ip tcp mss TCP MSS value 536 bytes`
```
 
### Example: Setting the MSS for TCP Connections
 

This example shows a setting the MSS for TCP connections:

```
` configure terminal ip tcp mss 2000 `
```
 
### Example: Removing a Set IP TCP MSS
 

This example shows how to remove the MSS:

```
` configure terminal no ip tcp mss `
```
 
## Verifying IP TCP MSS
 
 Table 2. Verifying IP TCP MSS 

Command
 

Purpose
 

 **show ip tcp mss ** 
 

Displays the set IP TCP MSS.
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
