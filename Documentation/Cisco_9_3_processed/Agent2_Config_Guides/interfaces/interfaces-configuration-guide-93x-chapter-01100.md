# Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring IP Event Dampening [Cisco Nexus 9000 Series Switches]

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01100.html`
**Tags:** interfaces, ethernet, port-channels, switchport

---

Cisco Nexus 9000 Series NX-OS Interfaces Configuration Guide, Release 9.3(x) - Configuring IP Event Dampening [Cisco Nexus 9000 Series Switches] - Cisco 	 	 
 
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
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index Search Find Matches in This Book Save [/c/login/index.html?referer=/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01100.html] Log in to Save Content [#] Translations Available Languages 
 Download Download Options 
### 

### 
 
 
- [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.65 MB) [/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01100.pdf] PDF - This Chapter (1.01 MB) 

View with Adobe Reader on a variety of devices
 Print 
## Results
 Updated: March 28, 2022 
## Chapter: Configuring IP Event Dampening 
 Chapter Contents 
 
- [#id_76540] Configuring IP Event Dampening 
- [#concept_hcp_q3s_g2b] IP Event Dampening Overview 
- [#concept_gvc_kxs_g2b] Guidelines and Limitations 
- [#concept_ksq_l3s_g2b] Interface State Change Events 
 
- [#concept_xmw_bjs_g2b] Suppress Threshold 
- [#concept_lzd_b3s_g2b] Half-Life Period 
- [#concept_j4z_53s_g2b] Reuse Threshold 
- [#concept_idy_s3s_g2b] Maximum Suppress Time 
- [#concept_d3s_h3s_g2b] Affected Components 
 
- [#concept_fyp_x3s_g2b] Route Types 
- [#concept_rx5_z3s_g2b] Supported Protocols 
- [#concept_hqn_23s_g2b] How to Configure IP Event Dampening 
 
- [#task_ayv_4ps_g2b] Enabling IP Event Dampening 
- [#task_gxh_rps_g2b] Verifying IP Event Dampening 
- [#id_76282] Default Settings for IP Dampening Parameters Close 
# Configuring IP Event Dampening
 

- [#concept_hcp_q3s_g2b] 
- [#concept_gvc_kxs_g2b] 
- [#concept_ksq_l3s_g2b] 
- [#concept_d3s_h3s_g2b] 
- [#concept_hqn_23s_g2b] 
## IP Event Dampening Overview
 

 Interface state changes occur when interfaces are administratively brought up or down or if an interface changes state. When an interface changes state or flaps, routing protocols are notified of the status of the routes that are affected by the change in state. Every interface state change requires all affected devices in the network to recalculate best paths, install or remove routes from the routing tables, and then advertise valid routes to peer routers. An unstable interface that flaps excessively can cause other devices in the network to consume substantial amounts of system processing resources and cause routing protocols to lose synchronization with the state of the flapping interface. 
 

 The IP Event Dampening feature introduces a configurable exponential decay mechanism to suppress the effects of excessive interface flapping events on routing protocols and routing tables in the network. This feature allows the network operator to configure a router to automatically identify and selectively dampen a local interface that is flapping. Dampening an interface removes the interface from the network until the interface stops flapping and becomes stable. Configuring the IP Event Dampening feature improves convergence times and stability throughout the network by isolating failures so that disturbances are not propagated. This, in turn, reduces the utilization of system processing resources by other devices in the network and improves overall network stability. 
 
## Guidelines and Limitations
 

 The IP Event Dampening feature introduces a configurable exponential decay mechanism to suppress the effects of excessive interface flapping events on routing protocols and routing tables in the network. This feature allows the network operator to configure a router to automatically identify and selectively dampen a local interface that is flapping. See the following guidelines and limitations before configuring IP Event Dampening feature: 
 
 
- 				 

Beginning from Cisco NX-OS Release 9.2(1), IP event dampening is supported on Cisco Nexus 9300-EX, 9300-FX, 9300-FX2, 9300-FXP, 9700-EX, and 9700-FX platform switches. 
 			 
- 				 

Due to changes in the netstack-IP component, all the IP clients observe the impact of dampening or interface. 
 			 
- 				 

 For each flap of the interface, a certain penalty is added. The penalty decays exponentially whose parameters are configured. 
 			 
- 				 

When penalty exceeds the Suppress threshold the interface is dampened. It is unsuppressed when the penalty decays below the Reuse threshold. 
 			 
- 				 

When an interface is dampened, the IP address and the static routes are removed from the interface. All the clients of IP get an IP delete notification. 
 			 
- 				 

When an interface is unsuppressed, the IP address and the relevant routes are added back. All the clients of IP get an IP address add notification for all the IP addresses of the interface. 
 			 
- 				 

 All Layer 3 interfaces that are configured on the Ethernet interface, port channels, and SVI support this feature. 
 			 
## Interface State Change Events
 

 IP Event Dampening feature employs a configurable exponential decay mechanism that is used to suppress the effects of excessive interface flapping or state changes. When the IP Event Dampening feature is enabled, flapping interfaces are dampened from the perspective of the routing protocol by filtering excessive route updates. Flapping interfaces are identified, assigned penalties, suppressed if necessary, and made available to the network when the interface stabilizes. 
 

- [#concept_xmw_bjs_g2b] 
- [#concept_lzd_b3s_g2b] 
- [#concept_j4z_53s_g2b] 
- [#concept_idy_s3s_g2b] 
### Suppress Threshold
 

 The suppress threshold is the value of the accumulated penalty that triggers the router to dampen a flapping interface. The flapping interface is identified by the router and assigned a penalty for each up and down state change, but the interface is not automatically dampened. The router tracks the penalties that a flapping interface accumulates. When the accumulated penalty reaches the default or preconfigured suppress threshold, the interface is placed in a dampened state. 
 
### Half-Life Period
 

 The half-life period determines how fast the accumulated penalty can decay exponentially. When an interface is placed in a dampened state, the router monitors the interface for additional up and down state changes. If the interface continues to accumulate penalties and the interface remains in the suppress threshold range, the interface will remain dampened. If the interface stabilizes and stops flapping, the penalty is reduced by half after each half-life period expires. The accumulated penalty will be reduced until the penalty drops to the reuse threshold. The configurable range of the half-life period timer is from 1 to 30 seconds. The default half-life period timer is 5 seconds. 
 
### Reuse Threshold
 

 When the accumulated penalty decreases until the penalty drops to the reuse threshold, the route is unsuppressed and made available to other devices in the network. The range of the reuse value is from 1 to 20000 penalties. The default value is 1000 penalties. 
 
### Maximum Suppress Time
 

 The maximum suppress time represents the maximum time an interface can remain dampened when a penalty is assigned to an interface. The maximum suppress time can be configured from 1 to 255 seconds. The maximum penalty is truncated to maximum 20000 unit. The maximum value of the accumulated penalty is calculated based on the maximum suppress time, reuse threshold, and half-life period. 
 

IP event dampening configuration command applies dampening to routing protocols for both IP and CLNS. 
 

The first set of parameters ([half-life | reuse | suppress max-suppress]) configure the different parameters of the dampening algorithm. The second set ([restart [penalty] ]) enables dampening penalty to be applied when the interface comes up the first time after reboot. The default restart penalty is applied only if you specify the restart parameter. Both parameter sets are optional 
 
## Affected Components
 

 When an interface is not configured with dampening, or when an interface is configured with dampening but is not suppressed, the routing protocol behavior as a result of interface state transitions is not changed by the IP Event Dampening feature. However, if an interface is suppressed, the routing protocols and routing tables are immune to any further state transitions of the interface until it is unsuppressed. 
 

- [#concept_fyp_x3s_g2b] 
- [#concept_rx5_z3s_g2b] 
### Route Types
 
 
- 				 Connected routes: 
 
- The connected routes of dampened interfaces are not installed into the routing table. 
- When a dampened interface is unsuppressed, the connected routes will be installed into the routing table if the interface is up. 				 			 
- 				 Static routes: 
 
- Static routes assigned to a dampened interface are not installed into the routing table. 
- When a dampened interface is unsuppressed, the static route will be installed into the routing table if the interface is up. 				 			 
 

**Note**
 			 

 Only the primary interface can be configured with this feature, and all subinterfaces are subject to the same dampening configuration as the primary interface. IP Event Dampening does not track the flapping of individual subinterfaces on an interface. 
 		 
 
### Supported Protocols
 

All the protocols that are used are impacted by the IP Event Dampening feature. The IP Event Dampening feature supports Border Gateway Protocol (BGP), Enhanced Interior Gateway Routing Protocol (EIGRP), Hot Standby Routing Protocol (HSRP), Open Shortest Path First (OSPF), Routing Information Protocol (RIP), and VRRP. Ping and SSH to the concerned interface IP address does not work. 
 
 

**Note**
 			 

 The IP Event Dampening feature has no effect on any routing protocols if it is not enabled or an interface is not dampened. 
 		 
 
## How to Configure IP Event Dampening
 

- [#task_ayv_4ps_g2b] 
- [#task_gxh_rps_g2b] 
- [#id_76282] 
### Enabling IP Event Dampening
 			 

 The dampening command is entered in interface configuration mode to enable the IP Event Dampening feature. If this command is applied to an interface that already has dampening configured, all dampening states are reset and the accumulated penalty will be set to 0. If the interface has been dampened, the accumulated penalty will fall into the reuse threshold range, and the dampened interface will be made available to the network. The flap counts, however, are retained. 
 		 
### SUMMARY STEPS
 
 
- 					 						configure terminal 					 				 
- 					 						interface type number 					 				 
- 					 						dampening [half-life-period reuse-threshold] [suppress-threshold max-suppress [restart-penalty]] 				 
- 					 						no dampening 					 				 
- 					 						end 					 				 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 					 						configure terminal 					 				 
 					 

 Enters global configuration mode. 
 				 

**Step 2**
 

 					 						interface type number 					 				 
 					 

 Enters interface configuration mode and configures the specified interface. 
 				 

**Step 3**
 

 					 						dampening [half-life-period reuse-threshold] [suppress-threshold max-suppress [restart-penalty]] 				 
 					 

 Enables interface dampening. 
 					 
 
- 							 

 Entering the dampening command without any arguments enables interface dampening with default configuration parameters. 
 						 
- 							 

 When manually configuring the timer for the restart-penalty argument, the values must be manually entered for all arguments. 
 						 				 

**Step 4**
 

 					 						no dampening 					 				 
 					 

 Disables interface dampening. 
 				 

**Step 5**
 

 					 						end 					 				 
 					 

 Exits interface configuration mode. 
 				 
 
### Verifying IP Event Dampening
 			 

 Use the show 					dampening 					interface or show 					interface 					dampening commands to verify the configuration of the IP Event Dampening feature. 
 		 
### SUMMARY STEPS
 
 
- 					 						show 						ip interface [interface] 				 
- 					 						show 						dampening 						interface 					 				 
- 					 						show 						interface 						dampening 					 				 
### DETAILED STEPS
 
   Command or Action Purpose 

**Step 1**
 

 					 						show 						ip interface [interface] 				 
 					 

 Displays all the configured dampening parameters including penalty information. You see the output only if you have the IP enabled on the interface. 
 				 

**Step 2**
 

 					 						show 						dampening 						interface 					 				 
 					 

 Displays dampened interfaces. 
 				 

**Step 3**
 

 					 						show 						interface 						dampening 					 				 
 					 

 Displays dampened interfaces on the local router. 
 				 
 
### Default Settings for IP Dampening Parameters
 
 Table 1. Default values for IP Dampening Parameters 

Parameters 
 

Range 
 

Default
 

 Half-life
 

1-30 
 

5
 

Reuse threshold
 

1-20000
 

800
 

Suppress threshold
 

1-20000
 

2000
 

Max suppress time
 

1-255  seconds
 

20 seconds
 

Apply restart penalty
 

False
 

Restart penalty
 

true / false
 

false
 
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/en/us/services/order-services.html]
