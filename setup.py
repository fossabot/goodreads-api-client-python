# -*- coding: utf-8 -*-
"""
Goodreads API Client
=====

Goodreads API Client is a non-official Python client for `Goodreads <http://goodreads.com/>`.
"""
import ast
import re
from setuptools import setup


_version_re = re.compile(r'VERSION\s+=\s+(.*)')

with open('goodreads_api_client/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


tests_require = [
    'vcrpy==1.11.1',
]

install_requires = [
    'requests==2.18.3',
    'xmltodict==0.11.0',
]

setup(
    name='goodreads_api_client',
    version=version,
    url='https://github.com/mdzhang/goodreads-api-client-python',
    author='Michelle D. Zhang',
    author_email='zhang.michelle.d@gmail.com',
    description='A non-official client for Goodreads (https://goodreads.com)',
    long_description=__doc__,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=['goodreads_api_client'],
    tests_require=tests_require,
    install_requires=install_requires,
    test_suite='goodreads_api_client.tests',
    include_package_data=True,
    zip_safe=False,
    platforms=[],
)