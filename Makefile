install:
	python setup.py develop

lint:
	pycodestyle setup.py goodreads_api_client

test:
	python setup.py test