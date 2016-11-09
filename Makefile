help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint:	## Run flake8.
	@py.test --flake8

test:   ## Run unit tests and print test coverage.
	@py.test --cov-report term-missing --cov=einder -v tests/


.PHONY: help lint test

.DEFAULT_GOAL := help
