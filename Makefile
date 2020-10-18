.PHONY: test

test:
	poetry run pytest tests/ --disable-pytest-warnings

