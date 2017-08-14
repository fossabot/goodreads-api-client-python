clean:
	rm -rf build dist .eggs *.egg-info docs/_build

.PHONY: docs
docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

install-dev:
	python setup.py develop

install-docs:
	pip install .[docs]

install-publish:
	pip install .[publish]

install-test:
	pip install .[test]

install: install-dev install-docs install-publish install-test

lint:
	pycodestyle setup.py goodreads_api_client

publish: clean install-publish
	python setup.py sdist bdist_wheel
	twine upload dist/*

publish-test: clean install-publish
	python setup.py sdist bdist_wheel
	twine upload dist/* -r pypitest

test:
	python setup.py test