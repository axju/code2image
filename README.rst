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

  $ python examples/shadow.py

.. image:: https://raw.githubusercontent.com/axju/code2image/master/examples/shadow.png
   :align: center

This package was developed to automate some boring image creation process. But
it has also a script for some command line fun.

.. code-block:: shell

  $ code2image --help
  usage: code2image [-h] [--kind {simple,shadow,background}]
                    [--imagename IMAGENAME] [--code CODE]
                    [--background BACKGROUND] [--font-size FONT_SIZE]
                    [--font-name FONT_NAME] [--line_pad LINE_PAD]
                    [--line-numbers] [--shadow-color SHADOW_COLOR]
                    [--shadow-dt SHADOW_DT] [--offset OFFSET] [--blur BLUR]
                    [--epilog EPILOG]
                    codefile

  Create nice code snippets

  positional arguments:
    codefile              The code file

  optional arguments:
    -h, --help            show this help message and exit
    --kind {simple,shadow,background}
                          Change the result
    --imagename IMAGENAME
                          The output image
    --code CODE           Code background color
    --background BACKGROUND
                          Image background color
    --font-size FONT_SIZE
                          font size
    --font-name FONT_NAME
                          font name
    --line_pad LINE_PAD   line pad
    --line-numbers        line numbers
    --shadow-color SHADOW_COLOR
                          Shadow color
    --shadow-dt SHADOW_DT
                          Shadow offset
    --offset OFFSET       Border width
    --blur BLUR           Shadow blur
    --epilog EPILOG       A epilog


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
