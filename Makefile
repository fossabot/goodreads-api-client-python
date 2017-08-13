clean:
	rm -rf build dist .eggs *.egg-info

install:
	python setup.py develop && pip install .[test]

lint:
	pycodestyle setup.py goodreads_api_client

publish: clean
	python setup.py sdist bdist_wheel upload

test:
	python setup.py test