# Cisco Nexus 9000 Series NX-OS Programmability Guide, Release 9.3(x)

**Source:** b-cisco-nexus-9000-series-nx-os-programmability-guide-93x.html

**Tags:** programmability, nx-os, nx-api, python, automation, netconf, restconf, grpc, telemetry, yang, ansible, puppet, chef, docker

**Updated:** September 11, 2023

---

## Book Table of Contents

This guide covers programmability features for Cisco Nexus 9000 Series switches running NX-OS Release 9.3(x).

### Preface
- Documentation conventions and support information

### New and Changed Information
- Release-specific updates and feature additions

### Platform Support for Programmability Features
- Hardware platform compatibility matrix

### Overview
- Introduction to NX-OS programmability architecture

---

## Shells and Scripting

### Bash
- Accessing and using the Bash shell
- Bash scripting capabilities
- Command-line utilities

### Guest Shell
- Guest shell architecture and setup
- Running Linux tools on NX-OS
- Container support within Guest Shell

### Broadcom Shell
- Hardware-level debugging shell
- ASIC-specific commands and diagnostics

### Python API
- NX-OS Python API reference
- Writing Python scripts for automation
- Cisco NX-API Python library

### Scripting with Tcl
- Tcl scripting support on NX-OS
- Tcl command reference

### iPXE
- iPXE network boot configuration
- Automated deployment with iPXE

### Kernel Stack
- NX-OS kernel architecture
- Kernel-level networking stack

---

## Applications

### Third-Party Applications
- Installing and managing third-party applications
- Application hosting framework

### Ansible
- Ansible modules for NX-OS
- Playbook examples
- Connection plugins and inventory

### Puppet Agent
- Puppet agent configuration
- Manifest examples for NX-OS

### SaltStack
- SaltStack proxy minion configuration
- State file examples

### Using Chef Client with Cisco NX-OS
- Chef client setup
- Recipe development for NX-OS

### Nexus Application Development - Yocto
- Yocto Project integration
- Building custom applications

### Nexus Application Development - SDK
- NX-SDK (Nexus SDK) framework
- C++ and Python SDK development

### NX-SDK
- Native SDK for application development
- API reference and examples

### Using Docker with Cisco NX-OS
- Docker container support
- Container lifecycle management

---

## NX-API

### NX-API CLI
- JSON-RPC interface for CLI commands
- NX-API CLI authentication
- Request/response examples

### NX-API REST
- RESTful API architecture
- Resource URIs and methods
- JSON/XML data formats

### NX-API Developer Sandbox
- Interactive API testing environment
- Code generation tools

---

## Model-Driven Programmability

### Infrastructure Overview
- Model-driven architecture
- YANG data models
- Capabilities and features

### Managing Components
- Component configuration management
- Model-driven configuration workflows

### OpenConfig YANG
- OpenConfig YANG model support
- Implementation details

### NETCONF Agent
- NETCONF protocol support
- RPC operations and notifications
- Configuration with NETCONF

### Converting CLI Commands to Network Configuration Format
- CLI-to-model conversion tools
- Best practices for migration

### RESTConf Agent
- RESTConf protocol implementation
- RESTful operations on YANG models

### gRPC Agent
- gRPC protocol support
- Protocol buffer definitions
- Streaming capabilities

### gNMI - gRPC Network Management Interface
- gNMI protocol implementation
- Subscribe operations
- Telemetry streaming with gNMI

### Dynamic Logger
- Run-time log level adjustment
- Debugging and troubleshooting

### Model Driven Telemetry
- Subscribing to telemetry data
- Model-driven data collection
- Streaming telemetry architecture

---

## XML Management Interface

### XML Management Interface
- XML-based configuration management
- Schema definitions
- Operations and queries

---

## Appendices and Additional Resources

### Streaming Telemetry Sources
- List of supported telemetry paths
- Data source specifications

### WebSocket Subscription
- WebSocket-based telemetry
- Real-time data streaming

### Programmability RFCs
- Relevant RFC documentation
- Standards compliance

---

## Document Download Options

- **PDF - Complete Book** (6.23 MB)
- **ePub - Complete Book** (2.62 MB)
- **Mobi - Complete Book** (6.36 MB)

---

## Related Documents

- [Upgrade and Downgrade Guide](../upgrade/upgrade-downgrade-guide-93x.md)
- [Troubleshooting Guide](../troubleshooting/troubleshooting-guide-93x.md)
- [Verified Scalability Guide](../misc/verified-scalability-guide-931.md)

---

*This document applies to: Nexus 9000 Series Switches*
