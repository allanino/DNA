DNA
===

.. image:: https://landscape.io/github/allanino/DNA/master/landscape.png
        :target: https://landscape.io/github/allanino/DNA/master

.. image:: https://travis-ci.org/allanino/DNA.svg?branch=master
        :target: https://travis-ci.org/allanino/DNA/builds


This is a python script to encode/decode arbitrary computer files into
DNA sequences. It is a straight implementation of a method published in
`this`_ Nature’s paper. The details of the method can be found in the
`Supplementary Information`_ report. The source code organization
follows the article steps and nomenclature, so it should be easy to
understand.

How to use
----------

Install it using pip:

.. code-block:: console

    $ pip install file2dna

The installed script will be called :code:`dna` and accepts four types of operations passed as arguments together
with the file name:

.. code-block:: console

    $ dna -h
    usage: dna [-h] [-e | -s | -d | -j] file

    positional arguments:
      file        File to be encoded/decoded.

    optional arguments:
      -h, --help  show this help message and exit
      -e          encode file and save it as .dna
      -s          encode file and save it as .splitted.zip
      -d          decode .dna file and save as .decoded
      -j          decoded .splitted.zip file and save it as .decoded

As a example, we can decode one the `files`_ encoded by the authors of
the paper. Suppose you have cloned this repo with its examples folder:

.. code-block:: console

    $ dna -d examples/DNA_versions/wssnt10.txt.dna

To see the decoded file:

.. code-block:: console

    $ cat examples/DNA_versions/wssnt10.txt.decoded

.. _this: http://www.nature.com/nature/journal/v494/n7435/full/nature11875.html
.. _Supplementary Information: http://www.nature.com/nature/journal/v494/n7435/extref/nature11875-s2.pdf
.. _files: http://www.ebi.ac.uk/goldman-srv/DNA-storage/orig_files/
