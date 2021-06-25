#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for om_conns
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'opengear'
}

DOCUMENTATION = """
---
module: om_conns
version_added: 1.0.0
short_description: 'Manages connection attributes of opengear om conns'
description: 'Manages connection attributes of opengear om conns.'
author: Adrian Van Katwyk
options:
  config:
    description: Read and manipulate the network connections on the Operations Manager appliance.
    type: list
    elements: dict
    suboptions:
      id:
        type: str
      name:
        type: str
      mode:
        type: str
      physif:
        type: str
      ipv4_static_settings:
        type: dict
        suboptions:
          netmask:
            type: str
          address:
            type: str
          broadcast:
            type: str
          gateway:
            type: str
          dns1:
            type: str
          dns2:
            type: str
      ipv6_static_settings:
        type: dict
        suboptions:
          prefix_length:
            type: str
          address:
            type: str
          gateway:
            type: str
          dns1:
            type: str
          dns2:
            type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """
# Using deleted

<placeholder for the configuration example prior to module invocation>

- name: Configure interfaces
  myos_interfaces:
    operation: deleted

<placeholder for the configuration example after module invocation>


# Using merged

<placeholder for the configuration example prior to module invocation>

- name: Configure interfaces
  nxos_interfaces:
    config:
      - name: Ethernet1/1
        description: 'Configured by Ansible'
        enable: True
      - name: Ethernet1/2
        description: 'Configured by Ansible'
        enable: False
    operation: merged

<placeholder for the configuration example after module invocation>


# Using overridden

<placeholder for the configuration example prior to module invocation>

- name: Configure interfaces
  myos_interfaces:
    config:
      - name: Ethernet1/1
        description: 'Configured by Ansible'
        enable: True
      - name: Ethernet1/2
        description: 'Configured by Ansible'
        enable: False
    operation: overridden

<placeholder for the configuration example after module invocation>


# Using replaced

<placeholder for the configuration example prior to module invocation>

- name: Configure interfaces
  nxos_interfaces:
    config:
      - name: Ethernet1/1
        description: 'Configured by Ansible'
        enable: True
      - name: Ethernet1/2
        description: 'Configured by Ansible'
        enable: False
    operation: replaced

<placeholder for the configuration example after module invocation>


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.opengear.om.plugins.module_utils.network.om.argspec.conns.conns import ConnsArgs
from ansible_collections.opengear.om.plugins.module_utils.network.om.config.conns.conns import Conns


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=ConnsArgs.argument_spec,
                           supports_check_mode=True)

    result = Conns(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
