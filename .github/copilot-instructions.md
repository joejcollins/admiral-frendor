# Copilot Instructions for admiral-frendor

## Project Overview
- This is an Ansible-based automation project, organized as a collection (`local.admiral_fendor`) with plugins, modules, roles, and tests.
- Python code lives in `src/admiral_frendor/` (core logic) and `collections/local/admiral_fendor/plugins/module_utils/` (Ansible plugin utilities).
- The project root is identified by `pyproject.toml`.

## Architecture & Patterns
- **Service Pattern:** Utility services (e.g., `FileFinderService`) use dependency injection for testability. See `file_finder_service.py` in both `src/admiral_frendor/core/` and `plugins/module_utils/`.
- **Testing:** Tests are in `tests/` and `collections/local/admiral_fendor/tests/helpers/`. Use pytest conventions. Mocks are injected via constructor arguments.
- **Plugins:** Ansible plugins are organized by type under `collections/local/admiral_fendor/plugins/` (see README there for structure).
- **Documentation:** Uses MkDocs (`mkdocs.yml`, `docs/`). Serve docs with `make docs`.

## Developer Workflows
- **Environment:** Use `make venv` to create and sync the Python environment (uses `uv` and `.venv`).
- **Testing:** Run all tests with `make test`. Coverage: `pytest --cov=src`.
- **Linting:** Run `make lint` for Python (ruff), YAML, and Ansible linting.
- **Cleaning:** `make clean` removes build artifacts and caches.
- **Playbooks:** Run example playbook with `make ap-dummy`.
- **Docs:** Serve docs locally with `make docs`, publish with `make publish`.

## Conventions & Integration
- **Python:** Follows Google Python Style Guide (see `.github/instructions/python.instructions.md`).
- **Dependencies:** Managed in `pyproject.toml`. Use `uv` for environment management.
- **Ansible Collections:** Installed via `ansible-galaxy` in `make venv`.
- **Project Root Discovery:** Use `FileFinderService.find_root()` to locate the root directory.
- **External Integrations:** Some dependencies (e.g., `google-auth`, `google-cloud-storage`, `xkcdpass`) are required for specific Ansible collections.

## Examples
- **Service Usage:**
  ```python
  from admiral_frendor.core.file_finder_service import FileFinderService
  root = FileFinderService().find_root()
  ```
- **Test Pattern:**
  ```python
  def test_file_found_in_a_parent_directory():
      def mock_isfile(path):
          return path == "/home/user/setting.json"
      file_finder = FileFinderService(isfile=mock_isfile)
      result = file_finder.find_file_upwards("setting.json", "/home/user/documents/projects")
      assert result == "/home/user/setting.json"
  ```

## Key Files & Directories
- `Makefile`: Developer tasks and workflows
- `pyproject.toml`: Python dependencies and config
- `collections/local/admiral_fendor/plugins/`: Ansible plugin structure
- `src/admiral_frendor/core/`: Core Python logic
- `tests/`: Pytest-based tests
- `docs/`, `mkdocs.yml`: Documentation

---
_If any section is unclear or missing important project-specific details, please provide feedback to improve these instructions._
