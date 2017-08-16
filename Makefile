all: test

clean:
	rm -rf .eggs/ build/ dist/ docs/_build/ *.egg-info/ .tox
	-find . -name '__pycache__' -prune -exec rm -rf "{}" \;
	-find . -name '*.pyc' -delete

.PHONY: docs
docs:
	tox -e docs

install:
	pip install tox
	pip install .[test]

lint-py:
	tox -e flake8

lint-rst:
	tox -e doc8

lint:
	tox -e lint

publish: clean
	tox -e release

publish-test: clean
	tox -e testrelease

test:
	tox -e py35

##################################
# Docker container management
##################################

docker-build:
	docker build -t goodreads-api-client-python .

docker-docs:
	docker run --rm -v `pwd`:/src goodreads-api-client-python make docs

docker-lint:
	docker run --rm goodreads-api-client-python make lint

docker-publish:
	docker run --rm goodreads-api-client-python make publish

docker-run:
	docker run -it --rm goodreads-api-client-python /bin/bash

docker-test:
	docker run --rm goodreads-api-client-python make test