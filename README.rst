==========
code2image
==========

.. image:: https://img.shields.io/pypi/v/code2image.svg
        :target: https://pypi.python.org/pypi/code2image

Create code snippet with pygments and pillow.



Install
-------
.. code-block:: shell

  $ pip install code2image

Basic uses
----------
.. code-block:: shell

  $ code2image examples/shadow.py

.. image:: https://raw.githubusercontent.com/axju/code2image/master/examples/shadow.png
   :align: center

This package was developed to automate some boring image creation process. But
it has also a script for some command line fun.

.. code-block:: shell

  $ code2image --help


Python examples
---------------

.. code-block:: python

  from code2image.cls import Code2Image

  c2i = Code2Image()

  # load the source code from this file
  with open(__file__) as f:
      code = f.read()

  # create the image with highlighted code
  img = c2i.highlight(code)

  # save the image
  img.save('simple.png')

See the "examples" folder for more.


Development
-----------
Clone repo

.. code-block:: shell

  $ git clone https://github.com/axju/code2image.git

Create virtual environment for linux

.. code-block:: shell

  $ python3 -m venv venv
  $ source venv/bin/activate

.. code-block:: shell

or create virtual environment for windows

.. code-block:: shell

  $ python -m venv venv
  $ venv/Scripts/activate

update dev-tools

.. code-block:: shell

  $ python -m pip install --upgrade wheel pip setuptools twine tox flake8

Install local

.. code-block:: shell

  $ pip install -e .

Publish the packages

.. code-block:: shell

  $ python setup.py sdist bdist_wheel
  $ twine upload dist/*

Run some tests

.. code-block:: shell

  $ flake8 code2image
  $ python setup.py test
  $ python -m unittest discover -v
  $ tox

I do not know why, but tox will fail :(
