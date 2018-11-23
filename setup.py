#!/usr/bin/env python3
"""
A setuptools based setup module

Based on a template here:
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
import sys
# To use a consistent encoding
from codecs import open
from os import path
from unittest import TestLoader

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

def get_test_suite():
    test_loader = TestLoader()
    return test_loader.discover('test', pattern='*_test.py')

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lendsmart_api',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.6.0',

    description='The official python SDK for LendSmart API v1',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/lendsmart/lendsmart_python',

    # Author details
    author='Smart Labs',
    author_email='infos@lendsmart.ai',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        # This is staying in sync with the api's status
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='prediction ai lendsmart',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'tests']),

    # What do we need for this to run
    install_requires=[
        "future",
        "requests",
    ] if sys.version_info >= (3, 4) else [
        "future",
        "requests",
        "enum34",
    ],

    tests_require=[
        "mock",
    ],
    test_suite= 'setup.get_test_suite'
)
