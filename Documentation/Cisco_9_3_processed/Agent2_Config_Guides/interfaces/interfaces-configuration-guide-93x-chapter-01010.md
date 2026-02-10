# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring Q-in-Q VLAN Tunnels [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html`
**Tags:** interfaces, ethernet, port-channels, switchport, vlan

---

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring Q-in-Q VLAN Tunnels [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.65 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.pdf] PDF - This Chapter (1.34 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: March 28, 2022 
## Chapter: Configuring Q-in-Q VLAN Tunnels 
 Chapter Contents 
 
- [#id_75922] Configuring Q-in-Q VLAN Tunnels 
- [#concept_5A268F937D074F5FB4CBFAAD1825F15C] Information About 	 Q-in-Q Tunnels 
 
- [#concept_430A5AF3DE4D4B3E825D1C5B9146EF8F] Q-in-Q 	 Tunneling 
- [#concept_2FEB69F79ACA484F92BC11BCF91C8155] Native VLAN 	 Hazard 
- [#concept_3E17598E84C14025A51B13734F67917F] Information About 	 Layer 2 Protocol Tunneling 
- [#id_96466] Selective Q-in-Q with Multiple Provider VLANs 
- [#id_75909] Guidelines and Limitations for Q-in-Q tunneling and Layer 2 Protocol Tunneling 
- [#id_96465] Guidelines and Limitations for Selective Q-in-Q with Multiple Provider VLANs 
- [#d38287e827a1635] Configuring Q-in-Q Tunnels and Layer 2 Protocol Tunneling 
 
- [#task_97236FD4B73843B794588FD7CA5E775E] Creating a 802.1Q 	 Tunnel Port 
- [#id_96467] Configuring Selective Q-in-Q with Multiple provider VLANs 
- [#task_D09D873BA1AD4C239DCEB58A8EF0FF82] Changing the 	 EtherType for Q-in-Q 
- [#task_FCB1BBBDA123457FB80F20E455E2956E] Enabling the Layer 2 	 Protocol Tunnel 
- [#task_35A01FA066EE4477971008741321CCC2] Configuring Global 	 CoS for L2 Protocol Tunnel Ports 
- [#task_01BA32DE128747C39E537FC9DD713E17] Configuring 	 Thresholds for Layer 2 Protocol Tunnel Ports 
- [#Cisco_Task.dita_737d9bda-c91f-4944-8113-588dc6ba4b7e] Configuring Combined Access Port Feature set 
- [#id_64426] Configuring Q-in-Q Double Tagging 
- [#reference_59C5C28FC5614D00BAD33FBFE7A38503] Verifying the Q-in-Q 	 Configuration 
- [#reference_E60FB0BE7E6C440DA3267D79842FA092] Configuration 	 Examples for Q-in-Q and Layer 2 Protocol Tunneling Close 
# Configuring Q-in-Q VLAN Tunnels
 

- [#concept_5A268F937D074F5FB4CBFAAD1825F15C] 
- [#id_75909] 
- [#id_96465] 
- [#Cisco_Task.dita_737d9bda-c91f-4944-8113-588dc6ba4b7e] 
- [#id_64426] 
- [#reference_59C5C28FC5614D00BAD33FBFE7A38503] 
- [#reference_E60FB0BE7E6C440DA3267D79842FA092] 
## Information About 	 Q-in-Q Tunnels 
 

This chapter describes how to configure IEEE 802.1Q-in-Q VLAN tunnels and Layer 2 protocol tunneling on Cisco NX-OS devices.
 

A Q-in-Q VLAN tunnel 		enables a service provider to segregate the traffic of different customers in 		their infrastructure, while still giving the customer a full range of VLANs for 		their internal use by adding a second 802.1Q tag to an already tagged frame. 	 
 

- [#concept_430A5AF3DE4D4B3E825D1C5B9146EF8F] 
- [#concept_2FEB69F79ACA484F92BC11BCF91C8155] 
- [#concept_3E17598E84C14025A51B13734F67917F] 
- [#id_96466] 
### Q-in-Q 	 Tunneling 
 

Business customers of 		service providers often have specific requirements for VLAN IDs and the number 		of VLANs to be supported. The VLAN ranges required by different customers in 		the same service-provider network might overlap, and the traffic of customers 		through the infrastructure might be mixed. Assigning a unique range of VLAN IDs 		to each customer would restrict customer configurations and could easily exceed 		the VLAN limit of 4096 of the 802.1Q specification. 	 
 
 

**Note**
 		 

Q-in-Q is supported 		 on port channels. To configure a port channel as an asymmetrical link, all 		 ports in the port channel must have the same tunneling configuration. 		 
 	 
 

Using the 802.1Q 		tunneling feature, service providers can use a single VLAN to support customers 		who have multiple VLANs. Customer VLAN IDs are preserved and the traffic from 		different customers is segregated within the service-provider infrastructure 		even when they appear to be on the same VLAN. The 802.1Q tunneling expands the 		VLAN space by using a VLAN-in-VLAN hierarchy and tagging the tagged packets. A 		port configured to support 802.1Q tunneling is called a tunnel port. When you 		configure tunneling, you assign a tunnel port to a VLAN that is dedicated to 		tunneling. Each customer requires a separate VLAN, but that VLAN supports all 		of the customer’s VLANs. 	 
 

Customer traffic that 		is tagged in the normal way with appropriate VLAN IDs come from an 802.1Q trunk 		port on the customer device and into a tunnel port on the service-provider edge 		switch. The link between the customer device and the edge switch is an 		asymmetric link because one end is configured as an 802.1Q trunk port and the 		other end is configured as a tunnel port. You assign the tunnel port interface 		to an access VLAN ID that is unique to each customer. See the figure below. 	 
 Figure 1. 802.1Q-in-Q 		 Tunnel Ports 

 

Packets that enter the 		tunnel port on the service-provider edge switch, which are already 		802.1Q-tagged with the appropriate VLAN IDs, are encapsulated with another 		layer of an 802.1Q tag that contains a VLAN ID that is unique to the customer. 		The original 802.1Q tag from the customer is preserved in the encapsulated 		packet. Therefore, packets that enter the service-provider infrastructure are 		double-tagged. 	 
 

The outer tag contains 		the customer’s access VLAN ID (as assigned by the service provider), and the 		inner VLAN ID is the VLAN of the incoming traffic (as assigned by the 		customer). This double tagging is called tag stacking, Double-Q, or Q-in-Q as 		shown in the figure below. 	 
 Figure 2. Untagged, 		 802.1Q-Tagged, and Double-Tagged Ethernet Frames 

 

By using this method, 		the VLAN ID space of the outer tag is independent of the VLAN ID space of the 		inner tag. A single outer VLAN ID can represent the entire VLAN ID space for an 		individual customer. This technique allows the customer’s Layer 2 network to 		extend across the service provider network, potentially creating a virtual LAN 		infrastructure over multiple sites. 	 
 
 

**Note**
 		 

Hierarchical 		 tagging, or multi-level dot1q tagging Q-in-Q, is not supported. 		 
 	 
 
### Native VLAN 	 Hazard 
 

When configuring 		802.1Q tunneling on an edge switch, you must use 802.1Q trunk ports for sending 		out packets into the service-provider network. However, packets that go through 		the core of the service-provider network might be carried through 802.1Q 		trunks, ISL trunks, or nontrunking links. When 802.1Q trunks are used in these 		core switches, the native VLANs of the 802.1Q trunks must not match any native 		VLAN of the dot1q-tunnel port on the same switch because traffic on the native 		VLAN is not tagged on the 802.1Q transmitting trunk port. 	 
 

In the figure below, 		VLAN 40 is configured as the native VLAN for the 802.1Q trunk port from 		Customer X at the ingress edge switch in the service-provider network (Switch 		B). Switch A of Customer X sends a tagged packet on VLAN 30 to the ingress 		tunnel port of Switch B in the service-provider network that belongs to access 		VLAN 40. Because the access VLAN of the tunnel port (VLAN 40) is the same as 		the native VLAN of the edge-switch trunk port (VLAN 40), the 802.1Q tag is not 		added to tagged packets that are received from the tunnel port. The packet 		carries only the VLAN 30 tag through the service-provider network to the trunk 		port of the egress-edge switch (Switch C) and is misdirected through the egress 		switch tunnel port to Customer Y. 	 
 Figure 3. Native VLAN 		 Hazard 

 

These are a couple 		ways to solve the native VLAN problem: 	 
 
 
- 		 

Configure the edge 			 switch so that all packets going out an 802.1Q trunk, including the native 			 VLAN, are tagged by using the vlan dot1q tag native command. If the switch is 			 configured to tag native VLAN packets on all 802.1Q trunks, the switch accepts 			 untagged packets but sends only tagged packets. 		 
 		 
 

**Note**
 			 

The 				vlan 				 dot1q tag native command is a global command 				that affects the tagging behavior on all trunk ports. 			 
 		 
 		 
- 		 

Ensure that the 			 native VLAN ID on the edge switch trunk port is not within the customer VLAN 			 range. For example, if the trunk port carries traffic of VLANs 100 to 200, 			 assign the native VLAN a number outside that range. 		 
 		 
### Information About 	 Layer 2 Protocol Tunneling 
 

Customers at different 		sites connected across a service-provider network need to run various Layer 2 		protocols to scale their topology to include all remote sites, as well as the 		local sites. The Spanning Tree Protocol (STP) must run properly, and every VLAN 		should build a proper spanning tree that includes the local site and all remote 		sites across the service-provider infrastructure. The Cisco Discovery Protocol 		(CDP) must be able to discover neighboring Cisco devices from local and remote 		sites, and the VLAN Trunking Protocol (VTP) must provide consistent VLAN 		configuration throughout all sites in the customer network. 	 
 

You can configure the switch to allow multi-tagged BPDUs on a tunnel port. If you enable the l2protocol tunnel allow-double-tag command, when a multi-tagged customer BPDU enters the tunnel port, the original 802.1Q tags from the customer traffic is preserved and an outer VLAN tag (customer’s access VLAN ID, as assigned by the service-provider) is added in the encapsulated packet. Therefore, BPDU packets that enter the service-provider infrastructure are multi tagged. When the BPDUs leave the service-provider network, the outer tag is removed and the original multi-tagged BPDU is sent to the customer network. 
 

When protocol 		tunneling is enabled, edge switches on the inbound side of the service-provider 		infrastructure encapsulate Layer 2 protocol packets with a special MAC address 		and send them across the service-provider network. Core switches in the network 		do not process these packets, but forward them as normal packets. Bridge 		protocol data units (BPDUs) for CDP, STP, or VTP cross the service-provider 		infrastructure and are delivered to customer switches on the outbound side of 		the service-provider network. Identical packets are received by all customer 		ports on the same VLANs. 	 
 

If protocol tunneling 		is not enabled on 802.1Q tunneling ports, remote switches at the receiving end 		of the service-provider network do not receive the BPDUs and cannot properly 		run STP, CDP, 802.1X, and VTP. When protocol tunneling is enabled, Layer 2 		protocols within each customer’s network are totally separate from those 		running within the service-provider network. Customer switches on different 		sites that send traffic through the service- provider network with 802.1Q 		tunneling achieve complete knowledge of the customer’s VLAN. 	 
 
 

**Note**
 		 

Layer 2 protocol 		 tunneling works by tunneling BPDUs in the software. A large number of BPDUs 		 that come into the supervisor will cause the CPU load to go up. You might need 		 to make use of software rate limiters to reduce the load on the supervisor CPU. 		 See 		 [#task_01BA32DE128747C39E537FC9DD713E17] Configuring Thresholds for Layer 2 Protocol Tunnel Ports. 		 		 
 	 
 

For example, in the 		figure below, Customer X has four switches in the same VLAN that are connected 		through the service-provider network. If the network does not tunnel BPDUs, 		switches on the far ends of the network cannot properly run the STP, CDP, 		802.1X, and VTP protocols. 	 
 Figure 4. Layer 2 Protocol 		 Tunneling 

 

In the preceding 		example, STP for a VLAN on a switch in Customer X, Site 1 will build a spanning 		tree on the switches at that site without considering convergence parameters 		based on Customer X’s switch in Site 2. 	 
 

The figure below shows 		the resulting topology on the customer’s network when BPDU tunneling is not 		enabled. 	 
 Figure 5. Virtual Network 		 Topology Without BPDU Tunneling 

 
### Selective Q-in-Q with Multiple Provider VLANs 
 

Selective Q-in-Q with multiple provider VLANs is a tunneling feature that allows user-specific range of customer VLANs on a port to be associated with one specific provider VLAN and enables you to have multiple customer VLAN to provider VLAN mappings on a port. Packets that come in with a VLAN tag that matches any of the configured customer VLANs on the port are tunneled across the fabric using the properties of the service provider VLAN. The encapsulated packet carries the customer VLAN tag as part of the Layer 2 header of the inner packet. 
 
## Guidelines and Limitations for Q-in-Q tunneling and Layer 2 Protocol Tunneling 
 

Q-in-Q tunnels and Layer 2 tunneling have the following configuration guidelines and limitations: 
 
 
- 

Q-in-Q should be configured on the customer-facing interface of the service provider’s edge device. If an Ethernet frame ingresses a Cisco Nexus 9000 series switch, the switch cannot encapsulate the frame with two 802.1Q headers within a single forwarding decision. Similarly, if a Q-in-Q-encapsulated Ethernet frame needs to egress a Cisco Nexus 9000 series switch without any 802.1Q headers, the switch cannot decapsulate two 802.1Q headers from the Ethernet frame within a single forwarding decision. 
 
- 

Mapping multiple VLANs is supported. 
 
- 

Multiple selective Q-in-Q tags are not supported. That is, Q-in-Q does not support multiple SP tags on a single interface. 
 
- 

Switches in the service-provider network must be configured to handle the increase in MTU size due to Q-in-Q tagging. 
 
- 

MAC address learning for Q-in-Q tagged packets is based on the outer VLAN (Service Provider VLAN) tag. Packet forwarding issues might occur in deployments where a single MAC address is used across multiple inner (customer) VLANs. 
 
- 

Layer 3 and higher parameters cannot be identified in tunnel traffic (for example, Layer 3 destination and source addresses). Tunneled traffic cannot be routed. 
 
- 

The system dot1q-tunnel transit or system dot1q-tunnel transit vlan provider_vlan_list command have the following limitations: 
 
 
- 

These commands are required on Cisco Nexus 9300-EX/FX/FX2/FX3/GX switches and 9500 switches with 9700-EX/FX/GX line cards if the device is configured with Q-in-Q, Selective Q-in-Q or Selective Q-in-Q with multiple provider VLAN features. 
 
- 

It is required that you configure the system dot1q-tunnel transit or system dot1q-tunnel transit vlan provider_vlan_list command on ToR or modular devices. Beginning with Cisco NX-OS Release 9.3(5), the system dot1q-tunnel transit vlan provider_vlan_list command is supported. 
 
- 

It is required that you configure the system dot1q-tunnel transit or the system dot1q-tunnel transit vlan provider_vlan_list command on vPC switches or non-vPC switches. 
 
- 

Layer 2 frames that exit trunk ports will always be tagged, even with the native VLAN of the port if these commands have been configured. 
 
- 

The MPLS, GRE, and IP-in-IP functionalities will not function effectively in conjunction with the Q-in-Q tunneling features if these commands have been configured on the switch. 
 
- 

Cisco Nexus 9000 Series devices can provide only MAC-layer ACL/QoS for tunnel traffic (VLAN IDs and src/dest MAC addresses). 
 
- 

You should use MAC address-based frame distribution. 
 
- 

Asymmetrical links do not support the Dynamic Trunking Protocol (DTP) because only one port on the link is a trunk. You must configure the 802.1Q trunk port on an asymmetrical link to trunk unconditionally. 
 
- 

You cannot configure the 802.1Q tunneling feature on ports that are configured to support private VLANs. Private VLAN are not required in these deployments. 
 
- 

You must disable IGMP snooping on the tunnel VLANs. 
 
- 

You should enter the vlan dot1Q tag native command to maintain the tagging on the native VLAN and drop untagged traffic. This command prevents native VLAN misconfigurations. 
 
- 

You must manually configure the 802.1Q interfaces to be edge ports. 
 
- 

 IGMP snooping is not supported on the inner VLAN. 
 
- 

Q-in-Q is not supported on the uplink ports of Cisco Nexus 9332PQ, 9372PX, 9372TX, and 93120TX switches and Cisco Nexus 9396PX, 9396TX, and 93128TX switches with the N9K-M6PQ or N9K-M12PQ generic expansion module (GEM). 
 
- 

Q-in-Q tunnels might be affected by the limitations of the Application Leaf Engine (ALE) uplink ports on Cisco Nexus 9300 and 9500 Series devices: [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/ale_ports/b_Limitations_for_ALE_Uplink_Ports_on_Cisco_Nexus_9000_Series_Switches.html] Limitations for ALE Uplink Ports 
 
- 

Q-in-Q tagging is not supported. 
 
- 

Layer 2 protocol tunneling is not supported on Cisco Nexus 9500 Series switches with N9K-X9636C-R, N9K-X9636Q-R, N9K-X9636C-RX line cards. 
 
- 

Cisco Nexus 9500 Series switches with N9K-X9636C-R, N9K-X9636Q-R, N9K-X9636C-RX line cards, Q-in-Q is supported only on port or port-channel Layer 2 Access VLAN Edge devices. 
 
- 

FEX configuration is not supported on Q-in-Q ports.
 
- 

If the command **l2potocol tunnel stp** is configured on a tunnel interface, the VLAN that you configure on the service provider must be different from that of the customer network. 
 
## Guidelines and Limitations for Selective Q-in-Q with Multiple Provider VLANs
 
 
- 

For selective Q-in-Q with multiple provider VLANs, all the existing limitations and guidelines for selective Q-in-Q apply.
 
- 

Beginning with Cisco NX-OS Release 9.3(5), selective Q-in-Q with multiple provider VLANs feature is supported on Cisco Nexus N9K-C9316D-GX, N9K-C93600CD-GX, N9K-C9364C-GX switches. 
 
- 

Selective Q-in-Q with multiple provider VLANs feature is supported on Nexus 9300-EX, 9300-FX, 9300-FX2, 9300-FX3 switches.
 
- 

When you enable multiple provider VLANs on a vPC port channel, you must make sure that the configuration is consistent across the vPC peers. 
 
- 

We recommended not to allow provider VLANs on a regular trunk. 
 
- 

Only allow native VLAN and provider VLANs on the allowed vlan list of a Selective QinQ trunk interface.
 
- 

Selective QinQ trunk VLANs cannot be mixed with regular VLANs on the same Selective QinQ trunk interface. 
 
- 

Port to VLAN mappings (for example: switchport vlan mapping 10 20) is not supported on a port that is configured for selective Q-in-Q with multiple provider VLANs. 
 
- 

Private VLAN is not supported on a port that is configured for selective Q-in-Q with multiple provider VLANs.
 
- 

Only Layer 2 switching is supported. 
 
- 

Routing on provider VLANs is not supported.
 
- 

FEX is not supported for selective Q-in-Q with multiple provider VLANs.
 
- 

Selective Q-in-Q with multiple provider VLANs commands not DME-ized.
 
- 

When VLAN1 is configured as native VLAN with selective Q-in-Q and selective Q-in-Q with multiple provider tag, traffic on the native VLAN gets dropped. Do not configure VLAN1 as native VLAN when the port is configured with the selective Q-in-Q. When VLAN1 is configured as customer VLAN, then the traffic on VLAN1 gets dropped. 
 
### Guidelines and Limitations for Combined Access Port Feature set
 
 
- 

Beginning Cisco NX-OS Release 9.3(3), Combined Access Port Feature set is supported on Cisco Nexus C9348GC-FXP switches with IPv4 underlay. 
 
- 

The Combined Access Port Feature set consists of the following features: 
 
 
- 

Private VLAN (with secondary isolated)
 
- 

Selective Q-in-Q
 
- 

Port-Security
 
- 

All the guidelines and limitations for PVLAN and selective Q-in-Q are applicable for Combined Access Port Feature set also.
 
- 

Port mode private-vlan trunk secondaryis supported on Combined Access Port Feature set. 
 
- 

When you enable Combined Access Port Feature set on a vPC port channel, you must ensure that the configuration is consistent across the vPC peers. 
 
- 

We recommend that you enter system dot1q-tunnel transit when running the Combined Access Port Feature set. 
 
- 

Port VLAN mapping (for example: switchport vlan mapping 10 20) is not supported. 
 
- 

Only layer 2 switching is supported on Selective Q-in-Q.
 
- 

We dont allow spanning-tree bpdufilter to be disabled on the interface when dot1q-tunnel is configured on the interface. 
 
- 

Only routing is supported on native VLAN of the Combined Access Port Feature
 

Configuring Q-in-Q Tunnels and Layer 2 Protocol Tunneling
 
## Creating a 802.1Q 	 Tunnel Port 
 			 		 

You create the dot1q-tunnel port using the switchport mode command. 
 		 
 

**Note**
 				 

You must set the 802.1Q tunnel port to an edge port with the spanning-tree port type edge command. The provider VLAN membership of the port is changed using the 						switchport access vlan 						vlan-id 					 command. 
 		 

You should disable 			 IGMP snooping on the access VLAN allocated for the dot1q-tunnel port to allow 			 multicast packets to traverse the Q-in-Q tunnel. 		 
 		 
 			 

 For seamless packet forwarding and preservation of all VLAN tags on pure transit boxes in the SP cloud that have no Q-in-Q encapsulation or decapsulation requirement, configure the system-wide system dot1q-tunnel transit or system dot1q-tunnel transit vlan 						provider_vlan_list command. To remove the configuration, use the no system dot1q-tunnel transit or system dot1q-tunnel transit vlan 						provider_vlan_list command. 
 			 

For the supported platforms and limitations of the system dot1q-tunnel transit or system dot1q-tunnel transit vlan 							provider_vlan_list command, see [#id_75909] Guidelines and Limitations for Q-in-Q tunneling and Layer 2 Protocol Tunneling section.
 	 
### Before you begin
 		 

You must first 		 configure the interface as a switchport. 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure terminal 			 		 
- switch(config)# 			 interface ethernet 				slot/port 			 		 
- switch(config-if)# 			 switchport 		 
- switch(config-if)# 			 switchport mode 				 dot1q-tunnel 		 			 
- switch(config-if)# 						spanning-tree port type edge 			 
- switch(config-if)# 						switchport access vlan 						vlan-id 					 
- (Optional) switch(config-if)# 			 no switchport mode 				 dot1q-tunnel 		 
- switch(config-if)# 			 exit 		 
- (Optional) switch(config)# 			 show 				 dot1q-tunnel [interface 				if-range] 		 
- (Optional) switch(config)# 			 no shutdown 		 
- (Optional) switch(config)# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure terminal 			 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config)# 			 interface ethernet 				slot/port 			 		 
 			 

Specifies an 				interface to configure, and enters interface configuration mode. 			 
 		 

**Step 3**
 

switch(config-if)# 			 switchport 		 
 			 

Sets the 				interface as a Layer 2 switching port. 			 
 		 

**Step 4**
 

switch(config-if)# 			 switchport mode 				 dot1q-tunnel 		 
 			 

Creates a 802.1Q 				tunnel on the port. The port will go down and reinitialize (port flap) when the 				interface mode is changed. BPDU filtering is enabled and CDP is disabled on 				tunnel interfaces. 			 
 		 			 

**Step 5**
 

switch(config-if)# 						spanning-tree port type edge 
 					 

Designates the port as a spanning-tree edge port.
 				 			 

**Step 6**
 

switch(config-if)# 						switchport access vlan 						vlan-id 					 
 Configures the Provider access VLAN value. 

**Step 7**
 

(Optional) switch(config-if)# 			 no switchport mode 				 dot1q-tunnel 		 
 (Optional) 			 

Disables the 				802.1Q tunnel on the port. 			 
 		 

**Step 8**
 

switch(config-if)# 			 exit 		 
 			 

Exits 				configuration mode. 			 
 		 

**Step 9**
 

(Optional) switch(config)# 			 show 				 dot1q-tunnel [interface 				if-range] 		 
 (Optional) 			 

Displays all 				ports that are in dot1q-tunnel mode. Optionally, you can specify an interface 				or range of interfaces to display. 			 
 		 

**Step 10**
 

(Optional) switch(config)# 			 no shutdown 		 
 (Optional) 			 

Clears the 				errors on the interfaces and VLANs where policies correspond with hardware 				policies. This command allows policy programming to continue and the port to 				come up. If policies do not correspond, the errors are placed in an 				error-disabled policy state. 			 
 		 

**Step 11**
 

(Optional) switch(config)# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
### Example
 		 This example shows how to create an 802.1Q tunnel port: 
```
` switch# **configure terminal** switch(config)# **interface ethernet 7/1** switch(config-if)# **switchport** switch(config-if)# **switchport mode dot1q-tunnel** switch(config-if)# **spanning-tree port type edge** switch(config-if)# **switchport access vlan vlan 10** switch(config-if)# **exit** switch(config)# **exit** switch# **show dot1q-tunnel** `
```
 			 	 
## Configuring Selective Q-in-Q with Multiple provider VLANs
 
### Before you begin
 

You must configure provider VLANs 
 

You must disable spanning-tree on the trunk port using the spanning-tree bpdufilter enable command. 
 
### SUMMARY STEPS
 
 
- switch# configure terminal 
- switch(config)# interface interface-id 
- switch(config if)# switchport 
- switch(config-if)# switchport mode trunk 
- switch(config-if)# spanning-tree bpdufilter enable 
- switch(config-if)# switchport trunk native vlan vlan-id 
- switch(config-if)# switchport vlan mapping vlan-id-range dot1q-tunnel outer vlan-id 
- switch(config-if)# switchport trunk allowed vlan vlan_list 
- switch(config-if)# exit 
- switch(config-if)# show interfaces interface-id vlan mapping 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# configure terminal 
 

Enters global configuration mode.
 

**Step 2**
 

switch(config)# interface interface-id 
 

Enters interface configuration mode for the interface connected to the service provider network. You can enter a physical interface or an EtherChannel port channel. 
 

**Step 3**
 

switch(config if)# switchport 
 

Sets the interface as a Layer 2 switching port.
 

**Step 4**
 

switch(config-if)# switchport mode trunk 
 

Sets the interface as a Layer 2 trunk port.
 

**Step 5**
 

switch(config-if)# spanning-tree bpdufilter enable 
 

Disables the sending and processing of spanning-tree BPDUs on this interface.
 

**Step 6**
 

switch(config-if)# switchport trunk native vlan vlan-id 
 

Sets the native VLAN for the 802.1Q trunk. Valid values are from 1 to 4094. The default value is VLAN1.
 

**Step 7**
 

switch(config-if)# switchport vlan mapping vlan-id-range dot1q-tunnel outer vlan-id 
 

Enter the VLAN IDs to be mapped:
 
 
- 

vlan-id-range—The customer VLAN ID range(C-VLAN) entering the switch from the customer network. The range is from 1 to 4094. You can enter a string of VLAN-IDs. 
 
- 

outer vlan-id—Enter the outer VLAN ID (S-VLAN) of the service provider network. The range is from 1 to 4094.
 

**Step 8**
 

switch(config-if)# switchport trunk allowed vlan vlan_list 
 

Sets the allowed VLANs for the trunk interface.
 

**Step 9**
 

switch(config-if)# exit 
 

Exits the configuration mode.
 

**Step 10**
 

switch(config-if)# show interfaces interface-id vlan mapping 
 

Verifies the mapping configuration.
 
 

The following example shows how to configure selective Q-in-Q with multiple provider VLANs: 
 
### Example
 
```
`switch# sh run int e1/1 interface Ethernet1/1 switchport switchport mode trunk switchport trunk native vlan 2 switchport vlan mapping 3-400 dot1q-tunnel 400 switchport vlan mapping 401-800 dot1q-tunnel 401 switchport vlan mapping 801-1200 dot1q-tunnel 10 switchport vlan mapping 1201-1600 dot1q-tunnel 1400 switchport vlan mapping 1601-2000 dot1q-tunnel 9 switchport vlan mapping 2001-2400 dot1q-tunnel 3000 switchport vlan mapping 2401-2800 dot1q-tunnel 2099 switchport vlan mapping 2801-3200 dot1q-tunnel 2800 switchport vlan mapping 3201-3600 dot1q-tunnel 3967 switchport vlan mapping 3601-4000 dot1q-tunnel 600 spanning-tree bpdufilter enable switchport trunk allowed vlan 2,9-10,400-401,600,1400,2099,2800,3000,3967 switch# show interface e1/1 vlan mapping Interface Eth1/1: Original VLAN Translated VLAN --------------- ----------------- 3 400 4 400 5 400 6 400 7 400 8 400 9 400 10 400 11 400 12 400 13 400 14 400 15 400 16 400 17 400 18 400 19 400 20 400 switch# show consistency-checker selective-qinq interface e1/1 Fetching ingressVlanXlate entries from slice:0 HW Fetching ingressVlanXlate entries from slice:1 HW Performing port specific checks for intf Eth1/1 Port specific selective QinQ checks for interface Eth1/1 : PASS Switch# `
```
 
## Changing the 	 EtherType for Q-in-Q 
 			 

The switch default EtherType is 0x8100 for 802.1Q and Q-in-Q encapsulations. EtherType cannot be configured to 0x9100, 0x9200 and 0x88a8 on the switchport interface. 
 		 		 			 			 		 	 
## Enabling the Layer 2 	 Protocol Tunnel 
 		 

You can enable 		 protocol tunneling on the 802.1Q tunnel port. 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure terminal 			 		 
- switch(config)# 			 interface ethernet 				slot/port 			 		 
- switch(config-if)# 			 switchport 		 
- switch(config-if)# 			 switchport mode 				 dot1q-tunnel 		 
- switch(config-if)# l2protocol tunnel [cdp | stp | lacp | lldp |vtp] 				 
- (Optional) switch(config-if)# no l2protocol tunnel [cdp | stp | lacp | lldp |vtp] 				 
- switch(config-if)# 			 exit 		 
- (Optional) switch(config)# 			 no shutdown 		 
- (Optional) switch(config)# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure terminal 			 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config)# 			 interface ethernet 				slot/port 			 		 
 			 

Specifies an 				interface to configure, and enters interface configuration mode. 			 
 		 

**Step 3**
 

switch(config-if)# 			 switchport 		 
 			 

Sets the 				interface as a Layer 2 switching port. 			 
 		 

**Step 4**
 

switch(config-if)# 			 switchport mode 				 dot1q-tunnel 		 
 			 

Creates a 802.1Q 				tunnel on the port. The port will go down and reinitialize (port flap) when the 				interface mode is changed. BPDU filtering is enabled and CDP is disabled on 				tunnel interfaces. 			 
 		 

**Step 5**
 

switch(config-if)# l2protocol tunnel [cdp | stp | lacp | lldp |vtp] 				 
 					 

Enables Layer 2 protocol tunneling. Optionally, you can enable CDP, STP, LACP, LLDP, or VTP tunneling. 
 				 

**Step 6**
 

(Optional) switch(config-if)# no l2protocol tunnel [cdp | stp | lacp | lldp |vtp] 				 
 (Optional) 					 

Disables protocol tunneling. 
 					 				 

**Step 7**
 

switch(config-if)# 			 exit 		 
 			 

Exits 				configuration mode. 			 
 		 

**Step 8**
 

(Optional) switch(config)# 			 no shutdown 		 
 (Optional) 			 

Clears the 				errors on the interfaces and VLANs where policies correspond with hardware 				policies. This command allows policy programming to continue and the port to 				come up. If policies do not correspond, the errors are placed in an 				error-disabled policy state. 			 
 		 

**Step 9**
 

(Optional) switch(config)# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
### Example
 		 This example shows 		 how to enable protocol tunneling on an 802.1Q tunnel port: 		 
```
` switch# **configure terminal** switch(config)# **interface ethernet 7/1** switch(config-if)# **switchport** switch(config-if)# **switchport mode dot1q-tunnel** switch(config-if)# **l2protocol tunnel stp** switch(config-if)# **exit** switch(config)# **exit**`
```
 		 	 
## Configuring Global 	 CoS for L2 Protocol Tunnel Ports 
 		 

You can specify a 		 Class of Service (CoS) value globally so that ingress BPDUs on the tunnel ports 		 are encapsulated with the specified class. 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure terminal 			 		 
- switch(config)# 			 l2protocol tunnel cos 				value 		 
- (Optional) switch(config)# 			 no l2protocol tunnel 				 cos 		 
- switch(config)# 			 exit 		 
- (Optional) switch# 			 no shutdown 		 
- (Optional) switch# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure terminal 			 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config)# 			 l2protocol tunnel cos 				value 		 
 			 

Specifies a 				global CoS value on all Layer 2 protocol tunneling ports. The default cos-value 				is 5. 			 
 		 

**Step 3**
 

(Optional) switch(config)# 			 no l2protocol tunnel 				 cos 		 
 (Optional) 			 

Sets the global 				CoS value to default. 			 
 		 

**Step 4**
 

switch(config)# 			 exit 		 
 			 

Exits 				configuration mode. 			 
 		 

**Step 5**
 

(Optional) switch# 			 no shutdown 		 
 (Optional) 			 

Clears the 				errors on the interfaces and VLANs where policies correspond with hardware 				policies. This command allows policy programming to continue and the port to 				come up. If policies do not correspond, the errors are placed in an 				error-disabled policy state. 			 
 		 

**Step 6**
 

(Optional) switch# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
### Example
 		 This example shows 		 how to specify a global CoS value for the purpose of Layer 2 protocol 		 tunneling: 		 
```
` switch# **configure terminal** switch(config)# **l2protocol tunnel cos 6** switch(config)# **exit**`
```
 		 	 
## Configuring 	 Thresholds for Layer 2 Protocol Tunnel Ports 
 		 

You can specify the 		 port drop and shutdown value for a Layer 2 protocol tunneling port. 		 
 	 
### SUMMARY STEPS
 
 
- switch# 			 configure terminal 			 		 
- switch(config)# 			 interface ethernet 				slot/port 			 		 
- switch(config-if)# 			 switchport 		 
- switch(config-if)# 			 switchport mode 				 dot1q-tunnel 			 		 
- switch(config-if)# 			 l2protocol tunnel drop-threshold [cdp | 				stp | 				vtp] 				packets-per-sec 		 
- (Optional) switch(config-if)# 			 no 				 l2protocol tunnel drop-threshold [cdp | 				stp | 				vtp] 			 		 
- switch(config-if)# 			 l2protocol tunnel shutdown-threshold [cdp | 				stp | 				vtp] 				packets-per-sec 			 		 
- (Optional) switch(config-if)# no l2protocol tunnel shutdown-threshold [cdp | stp | vtp] 				 
- switch(config-if)# 			 exit 		 
- (Optional) switch(config)# 			 no shutdown 		 
- (Optional) switch(config)# 			 copy running-config 				 startup-config 		 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

switch# 			 configure terminal 			 		 
 			 

Enters global 				configuration mode. 			 
 		 

**Step 2**
 

switch(config)# 			 interface ethernet 				slot/port 			 		 
 			 

Specifies an 				interface to configure, and enters interface configuration mode. 			 
 		 

**Step 3**
 

switch(config-if)# 			 switchport 		 
 			 

Sets the 				interface as a Layer 2 switching port. 			 
 		 

**Step 4**
 

switch(config-if)# 			 switchport mode 				 dot1q-tunnel 			 		 
 			 

Creates a 802.1Q 				tunnel on the port. 			 
 		 

**Step 5**
 

switch(config-if)# 			 l2protocol tunnel drop-threshold [cdp | 				stp | 				vtp] 				packets-per-sec 		 
 			 

Specifies the 				maximum number of packets that can be processed on an interface before being 				dropped. Optionally, you can specify CDP, STP, or VTP. Valid values for the 				packets are from 1 to 4096. 			 
 		 

**Step 6**
 

(Optional) switch(config-if)# 			 no 				 l2protocol tunnel drop-threshold [cdp | 				stp | 				vtp] 			 		 
 (Optional) 			 

Resets the 				threshold values to 0 and disables the drop threshold. 			 
 		 

**Step 7**
 

switch(config-if)# 			 l2protocol tunnel shutdown-threshold [cdp | 				stp | 				vtp] 				packets-per-sec 			 		 
 			 

Specifies the 				maximum number of packets that can be processed on an interface. When the 				number of packets is exceeded, the port is put in error-disabled state. 				Optionally, you can specify CDP, STP, or VTP. Valid values for the packets is 				from 1 to 4096. 			 
 		 

**Step 8**
 

(Optional) switch(config-if)# no l2protocol tunnel shutdown-threshold [cdp | stp | vtp] 				 
 (Optional) 					 

Resets the threshold values to 0 and disables the shutdown threshold. 
 				 

**Step 9**
 

switch(config-if)# 			 exit 		 
 			 

Exits 				configuration mode. 			 
 		 

**Step 10**
 

(Optional) switch(config)# 			 no shutdown 		 
 (Optional) 			 

Clears the 				errors on the interfaces and VLANs where policies correspond with hardware 				policies. This command allows policy programming to continue and the port to 				come up. If policies do not correspond, the errors are placed in an 				error-disabled policy state. 			 
 		 

**Step 11**
 

(Optional) switch(config)# 			 copy running-config 				 startup-config 		 
 (Optional) 			 

Copies the 				running configuration to the startup configuration. 			 
 		 
 
## Configuring Combined Access Port Feature set
 

To configure combined access port feature set follow these steps.
 
### SUMMARY STEPS
 
 
- interface interface [port | port-channel | vPC] 
- switchport mode private-vlan trunk secondary 
- switchport private-vlan trunk native vlan vlan_id 
- switchport private-vlan trunk allowed vlan vlan list 
- switchport private-vlan association trunk primary_vlan_ID secondary_vlan_ID 
- switchport vlan mapping [vlan-id-range | all] dot1q-tunnel outer vlan-id 
- storm-control broadcast level [high level] [ lower level ] 
- storm-control multicast level [high level] [ lower level ] 
- storm-control action [shutdown | trap ] 
- load-interval counter {1 | 2 | 3 } 
- switchport port-security maximum [max-addr ] 
- switchport port-security action [restrict | shutdown | protect] 
- switchport port-security 
- service-policy {input | type {qos input | queuing {input | output}}} policy-map-name 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 interface interface [port | port-channel | vPC] 
 
### Example:
 
```
`switch# **interface port-channel 202**`
```
 

Places you into the interface configuration mode for the specified port channel. The range is from 1 to 4096.
 

**Step 2**
 

switchport mode private-vlan trunk secondary 
 
### Example:
 
```
`switch(config)# **switchport mode private-vlan trunk secondary**`
```
 

Configures the port as a secondary trunk port for a private VLAN. 
 

**Step 3**
 

switchport private-vlan trunk native vlan vlan_id 
 
### Example:
 
```
`switch(config)# **switchport private-vlan trunk native vlan 4002**`
```
 

Configures native VLAN assigned on a PVLAN trunk port. 
 

**Step 4**
 

switchport private-vlan trunk allowed vlan vlan list 
 
### Example:
 
```
`switch(config)# **switchport private-vlan trunk allowed vlan 1002,4002**`
```
 

Configures a list of allowed normal VLANs on a PVLAN trunk port. 
 

**Step 5**
 

switchport private-vlan association trunk primary_vlan_ID secondary_vlan_ID 
 
### Example:
 
```
`switch(config)# **switchport private-vlan association trunk 4050 4049**`
```
 

Configures association between primary VLAN and secondary VLAN on the PVLAN trunk port.
 

**Step 6**
 

switchport vlan mapping [vlan-id-range | all] dot1q-tunnel outer vlan-id 
 
### Example:
 
```
`switch(config-if)# **switchport vlan mapping all dot1q-tunnel 1002**`
```
 

Enter the customer range VLANs or keyword all which includes all the 4K VLANs. 
 

**Step 7**
 

storm-control broadcast level [high level] [ lower level ] 
 
### Example:
 
```
`switch(config-if)# **storm-control broadcast level 1.00**`
```
 

Configures broadcast storm control. Specifies the upper threshold levels for broadcast traffic.
 

**Step 8**
 

storm-control multicast level [high level] [ lower level ] 
 
### Example:
 
```
`switch(config-if)# **storm-control multicast level 1.00**`
```
 

Enables multicast traffic storm control on the interface, configures the traffic storm control level, and applies the traffic storm control level to all traffic storm control modes enabled on the interface. 
 

**Step 9**
 

storm-control action [shutdown | trap ] 
 
### Example:
 
```
`switch(config-if)# **storm-control action shutdown**`
```
 

Configures traffic storm-control to either generate trap or error-disable the port when a traffic storm occurs.
 

**Step 10**
 

load-interval counter {1 | 2 | 3 } 
 
### Example:
 
```
`switch(config-if)# **load-interval counter 1 5**`
```
 

Specifies the interval between sampling statistics on the interface.
 

**Step 11**
 

switchport port-security maximum [max-addr ] 
 
### Example:
 
```
`switch(config-if)# **switchport port-security maximum 3**`
```
 

Sets the maximum number of secure MAC addresses on a port.
 

**Step 12**
 

switchport port-security action [restrict | shutdown | protect] 
 
### Example:
 
```
`switch(config-if)# **switchport port-security violation restrict**`
```
 

Restrict security violation mode on the interface.
 

**Step 13**
 

switchport port-security 
 
### Example:
 
```
`switch(config-if)# **switchport port-security**`
```
 

Displays the port security configuration information.
 

**Step 14**
 

service-policy {input | type {qos input | queuing {input | output}}} policy-map-name 
 
### Example:
 
```
`switch(config-if)# **service-policy type qos input ovh_qos**`
```
 

Attaches a policy map to an interface.
 
 
## Configuring Q-in-Q Double Tagging
 

Enable multi-tagging for STP and CDP BPDUs.
 
### SUMMARY STEPS
 
 
- configure terminal 
- interface interface 
- switchport 
- switchport mode dot1q-tunnel 
- l2protocol tunnel [cdp | stp] 
- (Optional) no l2protocol tunnel [cdp | stp] 
- l2protocol tunnel allow-double-tag 
- (Optional) no l2protocol tunnel allow-double-tag 
- exit 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 configure terminal 
 
### Example:
 
```
`switch# **configure terminal**`
```
 

Enters global configuration mode.
 

**Step 2**
 

interface interface 
 
### Example:
 
```
`switch(config)# **interface ethernet 7/1**`
```
 

Specifies the interface that you are configuring. 
 

**Step 3**
 

switchport 
 
### Example:
 
```
`switch(config-if)# **switchport**`
```
 

Sets the interface as a Layer 2 switching port.
 

**Step 4**
 

switchport mode dot1q-tunnel 
 
### Example:
 
```
`switch(config-if)# **switchport mode dot1q-tunnel**`
```
 

Creates an 802.1Q tunnel on the port. The port goes down and reinitializes (port flap) when the interface mode is changed. BPDU filtering is enabled and CDP is disabled on tunnel interfaces. 
 

**Step 5**
 

l2protocol tunnel [cdp | stp] 
 
### Example:
 
```
`switch(config-if)# **l2protocol tunnel cdp**`
```
 

Enables Layer 2 protocol tunneling. Optionally, you can enable CDP or STP. 
 

**Step 6**
 

(Optional) no l2protocol tunnel [cdp | stp] 
 
### Example:
 
```
`switch(config-if)# **no l2protocol tunnel stp**`
```
 (Optional) 

Disables protocol tunneling. 
 

**Step 7**
 

l2protocol tunnel allow-double-tag 
 
### Example:
 
```
`switch(config-if)# **l2protocol tunnel allow-double-tag**`
```
 

Enables multi-tagging for STP and CDP BPDUs on the interface. 
 

**Step 8**
 

(Optional) no l2protocol tunnel allow-double-tag 
 
### Example:
 
```
`switch(config-if)# **no l2protocol tunnel allow-double-tag**`
```
 (Optional) 

Disables multi-tagging for STP and CDP BPDUs on the interface.
 

**Step 9**
 

exit 
 
### Example:
 
```
`switch(config-if)# **exit**`
```
 

Exits configuration mode.
 
 
### Example
 

This example shows how to enable multi-tagging for STP and CDP BPDUs:
 
```
`switch# configure terminal switch(config)# interface ethernet 7/1 switch(config-if)# switchport switch(config-if)# switchport mode dot1q-tunnel switch(config-if)# l2protocol tunnel cdp switch(config-if)# l2protocol tunnel stp switch(config-if)# l2protocol tunnel allow-double-tag switch(config-if)# exit switch(config)# exit switch#`
```
 
## Verifying the Q-in-Q 	 Configuration 
 		 
 					 

Command 					 
 				 					 

Purpose 					 
 				 					 

clear l2protocol tunnel 							 counters [interface 						 if-range] 					 
 				 					 

Clears all 						the statistics counters. If no interfaces are specified, the Layer 2 protocol 						tunnel statistics are cleared for all interfaces. 					 
 				 					 

show dot1q-tunnel [interface 						 if-range] 						 					 
 				 					 

Displays a 						range of interfaces or all interfaces that are in dot1q-tunnel mode. 					 
 				 					 

show l2protocol tunnel 						 [interface 						 if-range | 						 vlan 						 vlan-id] 					 
 				 					 

Displays 						Layer 2 protocol tunnel information for a range of interfaces, for all 						dot1q-tunnel interfaces that are part of a specified VLAN or all interfaces. 					 
 				 					 

show l2protocol tunnel summary 					 
 				 					 

Displays a 						summary of all ports that have Layer 2 protocol tunnel configurations. 					 
 				 					 

show running-config l2pt 					 
 				 					 

Displays 						the current Layer 2 protocol tunnel running configuration. 					 
 				 
 	 
## Configuration 	 Examples for Q-in-Q and Layer 2 Protocol Tunneling 
 		 This example shows a service provider switch that is configured to 		 process Q-in-Q for traffic coming in on Ethernet 7/1. A Layer 2 protocol tunnel 		 is enabled for STP BPDUs. The customer is allocated VLAN 10 (outer VLAN tag). 		 
```
` switch# **configure terminal** Enter configuration commands, one per line. End with CNTL/Z. switch(config)# **vlan 10** switch(config-vlan)# **no shutdown** switch(config-vlan)# **no ip igmp snooping** switch(config-vlan)# **exit** switch(config)# **interface ethernet 7/1** switch(config-if)# **switchport** switch(config-if)# **switchport mode dot1q-tunnel** switch(config-if)# **switchport access vlan 10** switch(config-if)# **spanning-tree port type edge** switch(config-if)# **l2protocol tunnel stp** switch(config-if)# **no shutdown** switch(config-if)# **exit** switch(config)# **exit** switch#`
```
 		 	 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
