# Cisco Nexus 9000 NX-OS Release Notes - Release 9.3(16)

## Revision History

| Date | Description |
|---|---|
| September 4, 2025 | Cisco NX-OS Release 9.3(16) became available. |
| Product ID | Description |

## Introduction

Introduction Cisco NX-OS Release 9.3(16) contains only security fixes; therefore, this document does not have open and resolved bug caveats. Also, there are no EPLD related changes in Cisco NX-OS Release 9.3(16). Note: The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. Date Description September 4, 2025 Cisco NX-OS Release 9.3(16) became available.

## New and Enhanced Software/Hardware Features

New and Enhanced Software/Hardware Features There are no new or enhanced software and hardware features introduced in Cisco NX-OS Release 9.3(16).

## Unsupported Hardware

Unsupported Hardware Beginning with Cisco NX-OS Release 9.3(16) the following PIDs are not supported. &middot; N9K-C9316D-GX &middot; N9K-C93600CD-GX &middot; N9K-C9364C-GX

## Device Hardware

Device Hardware The following tables list the Cisco Nexus 9000 Series hardware that Cisco NX-OS Release 9.3(16) supports. For additional information about the supported hardware, see the Hardware Installation Guide for your Cisco Nexus 9000 Series device. Table 1. Cisco Nexus 9500 Switches Product ID Description N9K-C9504 7.1-RU modular switch with slots for up to 4 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 4 power supplies. N9K-C9508 13-RU modular switch with slots for up to 8 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 8 power supplies. N9K-C9516 21-RU modular switch with slots for up to 16 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 10 power supplies. Table 2. Cisco Nexus 9500 Cloud Scale Line Cards Product ID Description Maximum Quantity Cisco Nexus 9504 Cisco Nexus 9508 Cisco Nexus 9516 N9K-X97160YC-EX Cisco Nexus 9500 48-port 10/25-Gigabit Ethernet SFP28 and 4-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 N9K-X9732C-EX Cisco Nexus 9500 32-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 N9K-X9732C-FX Cisco Nexus 9500 32-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 N9K-X9736C-EX Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 N9K-X9736C-FX Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 N9K-X9788TC-FX Cisco Nexus 9500 48-port 1/10-G BASE-T Ethernet and 4-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 16 Table 3. Cisco Nexus 9500 R-Series Line Cards Product ID Description Maximum Quantity Cisco Nexus 9504 Cisco Nexus 9508 N9K-X9636C-R Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 N9K-X9636C-RX Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card 4 8 N9K-X9636Q-R Cisco Nexus 9500 36-port 40 Gigabit Ethernet QSFP line card 4 8 N9K-X96136YC-R Cisco Nexus 9500

## Optics

Optics To determine which transceivers and cables are supported by a switch, see the Transceiver Module (TMG) Compatibility Matrix . To see the transceiver specifications and installation information, see the Install and Upgrade Guides .

## Cisco Network Insights

Cisco Network Insights Cisco NX-OS Release 9.3(16) supports the Cisco Network Insights Advisor (NIA) and Cisco Network Insights for Resources (NIR) on Cisco Nexus 9200, 9300-EX, and 9300-FX platform switches and 9500 platform switches with -EX/FX line cards. For more information, see the Cisco Network Insights documentation .

## Upgrade and Downgrade

Upgrade and Downgrade To perform a software upgrade or downgrade, follow the instructions in the Cisco Nexus 9000 Series NX-OS Software Upgrade and Downgrade Guide, Release 9.3(x). For information about an In Service Software Upgrade (ISSU), see the Cisco NX-OS ISSU Support Matrix .

## Exceptions

Exceptions Cisco Nexus 9200, 9300-EX, and 9300-FX Platform Switches The following features are not supported for the Cisco Nexus 9200, 9300-EX, and 9300-FX platform switches: ● 64-bit ALPM routing mode ● Cisco Nexus 9272PQ and Cisco Nexus 92160YC platforms do not support the PXE boot of the Cisco NX-OS image from the loader. ● ACL filters to span sub interface traffic on the parent interface ● Egress port ACLs ● Egress QoS policer (not supported for Cisco Nexus 9200 platform switches). The only policer action supported is drop. Remark action is not supported on the egress policer. ● FEX (not supported for Cisco Nexus 9200 platform switches) ● GRE v4 payload over v6 tunnels ● IP length-based matches ● IP-in-IP (not supported on the Cisco Nexus 92160 switch) ● Maximum Transmission Unit (MTU) checks for packets received with an MPLS header ● NetFlow (not supported on Cisco Nexus 9200 platform switches) ● Packet-based statistics for Traffic Storm Control (only byte-based statistics are supported) ● PVLANs (not supported on Cisco Nexus 9200 platform switches) ● PXE boot of the Cisco NX-OS image from the loader (not supported for Cisco Nexus 9272PQ and 92160YC switches) ● Q-in-VNI (not supported on Cisco Nexus 9200 platform switches) ● Q-in-Q for VXLAN (not supported on Cisco Nexus 9200 and 9300-EX platform switches) ● Q-in-VNI (not supported on Cisco Nexus 9200 platform switches) ● Resilient hashing for port channels ● Rx SPAN for multicast if the SPAN source and destination are on the same slice and no forwarding interface is on the slice ● SVI uplinks with Q-in-VNI (not supported for Cisco Nexus 9300-EX platform switches) ● Traffic Storm Control for copy-to-CPU packets ● Traffic Storm Control with unknown multicast traffic ● Tx SPAN for multicast, unknown multicast, and broadcast traffic ● VACL redirects for TAP aggregation Cisco Nexus 9300-FX3 Platform Switches The following features are not supported for the Cisco Nexus 9300-FX3 Platform switches: ● ACL with DSCP Wil

## Related Content

Related Content Cisco Nexus 9000 Series documentation : Cisco Nexus 9000 Series Switches Cisco Nexus 9000 and 3000 Series NX-OS Switch License Navigator : Cisco Nexus 9000 and 3000 Series NX-OS Switch License Navigator Cisco Nexus 9000 Series Software Upgrade and Downgrade Guide: Cisco Nexus 9000 Series NX-OS Software Upgrade and Downgrade Guide, Release 9.3(x) Cisco Nexus 9000 Series FPGA/EPLD Upgrade Release Notes: Cisco Nexus 9000 Series FPGA/EPLD Upgrade Release Notes, Release 9.3(16) Cisco Nexus 3000 and 9000 Series NX-API REST SDK User Guide and API Reference : Cisco Nexus NX-API Reference Cisco NX-OS Supported MIBs: https://cisco.github.io/cisco-mibs/supportlists/nexus9000/Nexus9000MIBSupportList.html Supported FEX modules : Cisco Nexus 9000 Series Switch FEX Support Matrix Licensing Information: Cisco NX-OS Licensing

## Documentation Feedback

Documentation Feedback To provide technical feedback on this document, or to report an error or omission, send your comments to nexus9k-docfeedback@cisco.com . We appreciate your feedback.

## Legal Information

Legal Information Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: https://www.cisco.com/c/en/us/about/legal/trademarks.html . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1721R) Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental. &copy; 2025 Cisco Systems, Inc. All rights reserved.

## Hardware Support Tables

| Date | Description |
|---|---|
| September 4, 2025 | Cisco NX-OS Release 9.3(16) became available. |

| Product ID | Description |
|---|---|
| N9K-C9504 | 7.1-RU modular switch with slots for up to 4 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 4 power supplies. |
| N9K-C9508 | 13-RU modular switch with slots for up to 8 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 8 power supplies. |
| N9K-C9516 | 21-RU modular switch with slots for up to 16 line cards in addition to two supervisors, 2 system controllers, 3 to 6 fabric modules, 3 fan trays, and up to 10 power supplies. |

| Product ID | Description | Maximum Quantity |
|---|---|---|
| Cisco Nexus 9504 | Cisco Nexus 9508 | Cisco Nexus 9516 |
| N9K-X97160YC-EX | Cisco Nexus 9500 48-port 10/25-Gigabit Ethernet SFP28 and 4-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |
| N9K-X9732C-EX | Cisco Nexus 9500 32-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |
| N9K-X9732C-FX | Cisco Nexus 9500 32-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |
| N9K-X9736C-EX | Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |
| N9K-X9736C-FX | Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |
| N9K-X9788TC-FX | Cisco Nexus 9500 48-port 1/10-G BASE-T Ethernet and 4-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | 16 |

| Product ID | Description | Maximum Quantity |
|---|---|---|
| Cisco Nexus 9504 | Cisco Nexus 9508 |
| N9K-X9636C-R | Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 |
| N9K-X9636C-RX | Cisco Nexus 9500 36-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 |
| N9K-X9636Q-R | Cisco Nexus 9500 36-port 40 Gigabit Ethernet QSFP line card | 4 | 8 |
| N9K-X96136YC-R | Cisco Nexus 9500 16-port 1/10 Gigabit, 32-port 10/25 Gigabit, and 4-port 40/100 Gigabit Ethernet line card | 4 | 8 |

| Product ID | Description | Maximum Quantity |
|---|---|---|
| Cisco Nexus 9504 | Cisco Nexus 9508 | Cisco Nexus 9516 |
| N9K-X9408C-CFP2 | Line card with 8 100 Gigabit CFP2 ports | 4 | 8 | 16 |
| N9K-X9432C-S | Cisco Nexus 9500 32-port 40/100 Gigabit Ethernet QSFP28 line card | 4 | 8 | N/A |
| N9K-X9432PQ | Cisco Nexus 9500 32-port 40 Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9636PQ | Cisco Nexus 9500 36-port 40 Gigabit Ethernet QSFP+ line card | 4 | 8 | N/A |
| N9K-X9464PX | Cisco Nexus 9500 48 1/10-Gigabit SFP+ and 4-port 40-Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9464TX | Cisco Nexus 9500 48 port 1/10-Gigabit BASE-T Ethernet and 4-port 40-Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9464TX2 | Cisco Nexus 9500 48 port 1/10-Gigabit BASE-T Ethernet and 4-port 40-Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9536PQ | Cisco Nexus 9500 36-port 40 Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9564PX | Cisco Nexus 9500 48 1/10-Gigabit SFP+ and 4 port 40-Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |
| N9K-X9564TX | Cisco Nexus 9500 48 port 1/10-Gigabit BASE-T Ethernet and 4 port 40-Gigabit Ethernet QSFP+ line card | 4 | 8 | 16 |

| Product ID | Description | Minimum | Maximum |
|---|---|---|---|
| N9K-C9504-FM-E | Cisco Nexus 9504 100-Gigabit cloud scale fabric module | 4 | 5 |
| N9K-C9508-FM-E | Cisco Nexus 9508 100-Gigabit cloud scale fabric module | 4 | 5 |
| N9K-C9508-FM-E2 | Cisco Nexus 9508 100-Gigabit cloud scale fabric module | 4 | 5 |
| N9K-C9516-FM-E | Cisco Nexus 9516 50-Gigabit cloud scale fabric module | 4 | 5 |
| N9K-C9516-FM-E2 | Cisco Nexus 9516 100-Gigabit cloud scale fabric module | 4 | 5 |

| Product ID | Description | Minimum | Maximum |
|---|---|---|---|
| N9K-C9504-FM-R | Cisco Nexus 9504 100-Gigabit R-Series fabric module | 4 | 6 |
| N9K-C9508-FM-R | Cisco Nexus 9508 100-Gigabit R-Series fabric module | 4 | 6 |

| Product ID | Description | Minimum | Maximum |
|---|---|---|---|
| N9K-C9504-FM | Cisco Nexus 9504 40-Gigabit fabric module | 3 | 6 |
| N9K-C9508-FM | Cisco Nexus 9508 40-Gigabit fabric module | 3 | 6 |
| N9K-C9516-FM | Cisco Nexus 9516 40-Gigabit fabric module | 3 | 6 |
| N9K-C9504-FM-S | Cisco Nexus 9504 100-Gigabit fabric module | 4 | 4 |
| N9K-C9508-FM-S | Cisco Nexus 9508 100-Gigabit fabric module | 4 | 4 |

| Product ID | Description | Minimum | Maximum |
|---|---|---|---|
| N9K-C9508-FM-Z | Cisco Nexus 9508 Fabric blank with Fan Tray Power Connector module | N/A | 2 |
| N9K-C9516-FM-Z | Cisco Nexus 9516 Fabric blank with Fan Tray Power Connector module | N/A | 2 |

| Supervisor | Description | Quantity |
|---|---|---|
| N9K-SUP-A | 1.8-GHz supervisor module with 4 cores, 4 threads, and 16 GB of memory | 2 |
| N9K-SUP-A+ | 1.8-GHz supervisor module with 4 cores, 8 threads, and 16 GB of memory | 2 |
| N9K-SUP-B | 2.2-GHz supervisor module with 6 cores, 12 threads, and 24 GB of memory | 2 |
| N9K-SUP-B+ | 1.9-GHz supervisor module with 6 cores, 12 threads, and 32 GB of memory | 2 |


---

**Source:** cisco-nexus-9000-nxos-release-notes-9316.html
**Tags:** release-notes, nx-os, cisco-nexus, 9.3(16), hardware-support, documentation
