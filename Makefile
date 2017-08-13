install:
	python setup.py develop

lint:
	pep8 setup.py goodreads_api_client

test:
	python setup.py test