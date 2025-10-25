"""Tests to confirm that the random_words lookup is working correctly.

Rather than loading the LookupModule class directly as you might expect (hope),
the lookup plugins have to be loaded somehow.  This could be done with a custom
plugin loader, that looks in the directory where the the plugins are.  The
community.general collection is installed in the virtual environment, so the
path is in the virtual environment.

```python
CUSTOM_LOOKUP_LOADER = PluginLoader(
    class_name="LookupModule",
    package="ansible_collections.community.general.plugins",
    config=[
        ".venv/lib/python3.12/site-packages/ansible_collections/community/general/plugins"
    ],
    subdir="lookup",
    required_base_class="LookupBase",
)
```

This is useful to know but most of the parameters are not needed in this case.
A simpler way is to use the add_directory method of the lookup_loader.  Again
handy to know if the plugs are in an unusual place.

```python
COLLECTION_PATH = (
    f"{site.getsitepackages()[0]}/ansible_collections/community/general/plugins/lookup"
)
lookup_loader.add_directory(COLLECTION_PATH)
```

Normally the lookup_loader only loads the default Ansible lookup paths,
['/home/username/.ansible/plugins/lookup', '/usr/share/ansible/plugins/lookup']
but initializing the plugin_loader will includes the plugins in the virtual
environment.

```python
loader.init_plugin_loader()
random_words = loader.lookup_loader.get("community.general.random_words")
```

"""

import site

from ansible.plugins import loader

COLLECTION_PATH = (
    f"{site.getsitepackages()[0]}"
    "/ansible_collections/community/general/plugins/lookup"
)


def test_random_words() -> None:
    """Run the random words lookup module.

    This is largely to confirm that xkcdpass is installed.  At the time of
    writing the `xkcdpass` package is not automatically installed as a
    dependency of the `community.general` collection, so it is referenced in the
    `pyproject.toml` file.  This test will fail if `xkcdpass` is not installed.
    """
    # ARRANGE
    terms: list = []
    variables = None
    kwargs: dict = {"numwords": 3, "delimiter": "-", "case": "capitalize"}
    expected_number_of_dashes = 2
    # Load the lookup plugin
    loader.init_plugin_loader()
    loader.lookup_loader.add_directory(COLLECTION_PATH)
    random_words = loader.lookup_loader.get("random_words")
    # ACT
    passwords = random_words.run(terms, variables, **kwargs)
    # ASSERT
    assert random_words is not None
    assert isinstance(passwords, list)
    assert passwords[0].count("-") == expected_number_of_dashes
