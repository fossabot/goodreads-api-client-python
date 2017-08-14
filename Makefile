all: test

clean:
	rm -rf .eggs/ build/ dist/ docs/_build/ *.egg-info/

.PHONY: docs
docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

install:
	pip install .[docs,publish,test]

lint:
	pycodestyle setup.py goodreads_api_client

publish: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

publish-test: clean
	python setup.py sdist bdist_wheel
	twine upload dist/* -r pypitest

test:
	python setup.py test

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