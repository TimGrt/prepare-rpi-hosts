# Bootstrap Raspberry Pi Hosts 
Ansible Playbook to prepare Raspberry Pi hosts with initial configurations depending on the operating system used.

[![CodeFactor](https://www.codefactor.io/repository/github/timgrt/prepare-rpi-hosts/badge)](https://www.codefactor.io/repository/github/timgrt/prepare-rpi-hosts)

The playbook supports the following operating systems:
* CentOS 7

## Requirements Master Node
The Master node is running the Playbook.
* Ansible v2.9.x or higher

The following Ansible Collections are necessary:
* ansible.posix

Missing collections can be installed with the provided `requirements.yml` file.
```bash
ansible-galaxy collection install -r requirements.yml
```

## Requirements Managed Nodes
Every Raspberry Pi Node needs to have an OS installed, all further configuration is done through this playbook.

1. Download and install operating system on SD card (e.g. [CentOS 7 Minimal Image](http://ftp.rz.uni-frankfurt.de/pub/mirrors/centos-altarch/7.8.2003/isos/aarch64/images/CentOS-Userland-7-aarch64-RaspberryPI-Minimal-4-2003-sda.raw.xz)).
2. Insert SD card and start Raspberry Pi.
3. Ensure SSH is running.

## Execution
Prepare the Raspberry Pi nodes according to the requirements section and adjust the inventory file.  
Execute the playbook:
```bash
ansible-playbook -i hosts main.yml
```

Shutdown the Pi nodes:
```bash
ansible-playbook -i hosts shutdown.yml
```

## Author
Created 2021 by Tim Grützmacher
