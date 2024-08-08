# Installation and dependencies management
install: # Install the project's dependencies using Poetry.
	poetry install

update-deps: # Update all dependencies to the latest versions.
	poetry update

# Code quality and testing
test: # Run the tests using pytest within the Poetry environment.
	poetry run pytest

test-coverage: # Run tests with coverage reporting enabled and output the result in XML format.
	poetry run pytest --cov=gendiff --cov-report xml

lint: # Run flake8 linter on the gendiff module to check for code style issues.
	poetry run flake8 gendiff

isort: # Sort imports in the gendiff module according to the isort tool.
	poetry run isort gendiff

# Checks and assembly
selfcheck: # Run Poetry's built-in checks to verify the project's configuration.
	poetry check

check: selfcheck test lint # Run selfcheck, tests, and linter in sequence to ensure code quality.

build: check # Run checks and then build the project packages (source and wheel).
	poetry build

# Cleaning and support
clean: # Remove temporary files and build artifacts.
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf dist/ build/ *.egg-info

# Publication and release
publish: # Perform a dry run of publishing the package to PyPI (without actual upload).
	poetry publish --dry-run

release-checklist: # Run all necessary checks and tasks before a release.
	make clean
	make test
	make lint
	make build

# Installation of a package
package-install: # Install the built package from the dist directory using pip.
	python3 -m pip install dist/*.whl

.PHONY: install test lint isort selfcheck check build publish package-install clean update-deps release-checklist
