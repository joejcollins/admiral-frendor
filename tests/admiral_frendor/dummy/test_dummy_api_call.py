"""Confirm the dummy api call action works as expected.

The AnsibleCollection Admiral_Frendor has been made a package so we can access
all the modules.
"""

from unittest.mock import Mock

from ansible.plugins import loader

from admiral_frendor.core.file_finder_service import FileFinderService

FILE_FINDER = FileFinderService()

COLLECTION_PATH = (
    f"{FILE_FINDER.find_root()}/src/ansible_collections/"
    "admiral_frendor/dummy/plugins/action"
)


def test_dummy_api_call() -> None:
    """Test the dummy_api_call action."""
    # ARRANGE
    expected_result = {
        "status": "success",
        "input_parameter": "Another test name",
    }
    loader.init_plugin_loader()
    loader.action_loader.add_directory(COLLECTION_PATH)
    dummy_api_call = loader.action_loader.get("dummy_api_call", class_only=True)
    dummy_api_call._supports_async = True  # pylint: disable=protected-access
    task = Mock()
    task.args = {
        "parameter": "Another test name",
    }
    the_instance = dummy_api_call(
        task=task,
        connection=Mock(),
        play_context=Mock(),
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    # ACT
    result = the_instance.run()
    # ASSERT
    assert result == expected_result
