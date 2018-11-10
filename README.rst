lendsmart_python
=============

.. image:: https://secure.travis-ci.org/lendsmart/lendsmart-python.png?branch=master
   :target: http://travis-ci.org/lendsmart/lendsmart-python
.. image:: https://img.shields.io/pypi/v/lendsmart.svg
   :target: https://pypi.python.org/pypi/lendsmart
.. image:: https://img.shields.io/pypi/pyversions/lendsmart.svg
   :target: https://pypi.python.org/pypi/lendsmart



Installation
------------

Install from PyPi using
`pip <http://www.pip-installer.org/en/latest/>`__, a package manager for
Python.

::

   pip install lendsmart

Don't have pip installed? Try installing it, by running this from the
command line:

::

   $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can `download the source code
(ZIP) <https://github.com/lendsmart/lendsmart-python/zipball/master>`__ for
``lendsmart-python``, and then run:

::

   python setup.py install

You may need to run the above commands with ``sudo``.



Getting Started

---------------

Getting started with the LendSmart API couldn't be easier. Create a
``Client`` and you're ready to go.

API Credentials
~~~~~~~~~~~~~~~

The ``LendSmart`` needs your LendSmart credentials. You can either pass these
directly to the constructor (see the code below) or via environment
variables.

.. code:: python

   from lendsmart.rest import Client

   account = "ACXXXXXXXXXXXXXXXXX"
   token = "YYYYYYYYYYYYYYYYYY"
   client = Client(account, token)

Alternately, a ``Client`` constructor without these parameters will look
for ``LENDSMART_ACCOUNT_SID`` and ``LENDSMART_AUTH_TOKEN`` variables inside
the current environment.

We suggest storing your credentials as environment variables. Why?
You'll never have to worry about committing your credentials and
accidentally posting them somewhere public.

.. code:: python

   from lend.rest import Client
   client = Client()


Make Account
~~~~~~~~~~~~~~

.. code:: python

   from lendsmart.rest import Client

   account = "ACXXXXXXXXXXXXXXXXX"
   token = "YYYYYYYYYYYYYYYYYY"
   client = Client(account, token)

   acount = client.accounts.create(email="info@lendsmart.com",
                              password="team#4lendsmart")
                              
   print(acount.token)


Make Document
~~~~~~~~~~~~~

.. code:: python

   from lendsmart.rest import Client

   account = "ACXXXXXXXXXXXXXXXXX"
   token = "YYYYYYYYYYYYYYYYYY"
   client = Client(account, token)

   message = client.document.create(to="+12316851234", from_="+15555555555",
                                    body="Hello there!")


