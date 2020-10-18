.PHONY: typecheck test


typecheck:
	poetry run pyre

test:
	poetry run pytest tests/ --disable-pytest-warnings

