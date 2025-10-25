"""Documentation for the module."""

DOCUMENTATION = r"""
---
module: dummy_api_call
version_added: 0.0.1
short_description: Demonstrates fixed-value action plugin functionality
description:
  - This is a virtual module that delegates all work to its action plugin.
  - It returns a fixed, dummy JSON structure for demonstration.
author:
  - Joe J Collins
options:
  parameter:
    description:
      - The feature flag name to "request" (for demo purposes).
    required: true
    type: str
"""

EXAMPLES = r"""
- name: Get a fixed feature flag status using the action plugin
  mycollection.dummy_api_call:
    parameter: "experimental_feature_toggle"
  register: api_result
"""

RETURN = r"""
fixed_result:
    description: A fixed dictionary structure returned by the action plugin.
    type: dict
    returned: always
    contains:
        status:
            description: Always 'success' for this demo.
            type: str
            sample: success
        is_enabled:
            description: The fixed feature flag status.
            type: bool
            sample: True
"""
