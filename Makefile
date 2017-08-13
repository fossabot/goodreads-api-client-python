install:
	python setup.py develop && pip install .[test]

lint:
	pycodestyle setup.py goodreads_api_client

test:
	python setup.py test