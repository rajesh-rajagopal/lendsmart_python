from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = None
with open('lendsmart/__init__.py') as f:
    exec(f.read())

with open('README.rst') as f:
    long_description = f.read()

# To install the lendsmart-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name = "lendsmart",
    version = __version__,
    description = "Lendsmart API client ",
    author = "Lendsmart",
    author_email = "info@lendsmart.com",
    url = "https://github.com/lendsmart/lendsmart_python/",
    keywords = ["lendsmart"],
    install_requires = [
        "six",
        "pytz",
        "PyJWT >= 1.4.2",
    ],
    extras_require={
        ':python_version<"3.0"': [
            "requests[security] >= 2.0.0",
        ],
        ':python_version>="3.0"': [
            "requests >= 2.0.0",
            "pysocks",
        ],
    },
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = long_description
)