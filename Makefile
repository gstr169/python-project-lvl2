install:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish:
	poetry publish -r test_pypi

test:
	poetry run pytest gendiff/tests

coverage:
	poetry run coverage run -m pytest gendiff

coverage_report:
	poetry run coverage report

.PHONY: install lint selfcheck check build publish