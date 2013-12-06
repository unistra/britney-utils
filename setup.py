#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]

setup(
    name='britney-utils',
    version='0.1.2',
    author='Arnaud Grausem',
    author_email='arnaud.grausem@gmail.com',
    maintainer='Arnaud Grausem',
    maintainer_email='arnaud.grausem@gmail.com',
    url='https://github.com/unistra/britney-utils',
    license='PSF',
    description='Utilities for the Python SPORE client called Britney',
    long_description=long_description,
    py_modules=['britney_utils'],
    download_url='http://pypi.python.org/pypi/britney-utils',
    keywords=['SPORE', 'REST Api', 'client', 'britney'],
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
