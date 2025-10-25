"""Demonstration dummy action."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    """Action module class."""

    _VALID_ARGS = frozenset(("parameter",))
    _VALID_ATTRIBUTES = frozenset(("parameter",))
    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        """Run the module."""
        if task_vars is None:
            task_vars = {}

        result = super(ActionModule, self).run(tmp, task_vars)

        feature_flag_name = self._task.args.get("parameter")

        display.v(f"Action Plugin: Running with parameter: {feature_flag_name}")
        result.update(
            {
                "changed": False,
                "fixed_result": {
                    "status": "success",
                    "module_used": "dummy_api_call",
                    "input_parameter": feature_flag_name,
                    "is_enabled": True,
                    "message": "This is a fixed, demo API response.",
                },
            }
        )

        return result
