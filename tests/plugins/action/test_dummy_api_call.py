"""Confirm the dummy api call action works as expected."""

from ansible_collections.dummy.actions import dummy_api_call


def test_dummy_api_call() -> None:
    """Test the dummy_api_call action."""
    result = dummy_api_call.perform_action(param1="value1", param2="value2")
    assert result == {"status": "success", "data": {"param1": "value1"}}
