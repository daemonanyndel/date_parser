.PHONY: test

test:
	pytest --log-cli-level=INFO time_parser_test.py
