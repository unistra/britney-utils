#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='britney-utils',
    version='0.1',
    author='Arnaud Grausem',
    author_email='arnaud.grausem@gmail.com',
    maintainer='Arnaud Grausem',
    maintainer_email='arnaud.grausem@gmail.com',
    url='https://github.com/unistra/britney-utils',
    license='PSF',
    description='Utilities for the Python SPORE client called Britney',
    long_description=long_description,
    packages=find_packages(),
    download_url='http://pypi.python.org/pypi/britney-utils',
    keywords=['SPORE', 'REST Api', 'client', 'britney'],
    entry_points={},
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    )
)