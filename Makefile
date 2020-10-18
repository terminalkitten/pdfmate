.PHONY: typecheck test


typecheck:
	poetry run pyre --search-path $(poetry env info -p)/site-packages/	

test:
	poetry run pytest tests/ --disable-pytest-warnings

