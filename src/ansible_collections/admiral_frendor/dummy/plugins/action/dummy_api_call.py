"""Demonstration dummy action."""

from __future__ import absolute_import, division, print_function

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

DISPLAY = Display()


class ActionModule(ActionBase):
    """Action module class."""

    _VALID_ARGS = frozenset(("parameter",))
    _VALID_ATTRIBUTES = frozenset(("parameter",))
    TRANSFERS_FILES = False

    def run(
        self, tmp: str | None = None, task_vars: dict | None = None
    ) -> dict:
        """Run the module."""
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)

        the_parameter = self._task.args.get("parameter")

        DISPLAY.v(f"Action Plugin: Running with parameter: {the_parameter}")
        result.update(
            {
                "status": "success",
                "input_parameter": the_parameter,
            }
        )

        return result
