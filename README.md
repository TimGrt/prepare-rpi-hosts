# Bootstrap Raspberry Pi Hosts 
Ansible Playbook to prepare Raspberry Pi hosts with initial configurations depending the operating systems used.

The playbook supports the following operating systems:
* CentOS 7

## Requirements Master Node
The Master node is running the Playbook.
* Ansible v2.9.x or higher

## Requirements Managed Nodes
Every Raspberry Pi Node needs to have an OS installed, all further configuration is done through this playbook.

1. Download and install operating system on SD card (e.g. [CentOS 7 Minimal Image](http://ftp.rz.uni-frankfurt.de/pub/mirrors/centos-altarch/7.8.2003/isos/aarch64/images/CentOS-Userland-7-aarch64-RaspberryPI-Minimal-4-2003-sda.raw.xz)).
2. Insert SD card and start Raspberry Pi.
3. Ensure SSH is running.


*This playbook is tested on Raspberry Pi 4 Nodes with 32GB SD card.*
