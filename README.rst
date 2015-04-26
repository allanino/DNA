DNA
===

.. image:: https://travis-ci.org/allanino/DNA.svg?branch=master
        :target: https://travis-ci.org/allanino/DNA/builds

.. image:: https://landscape.io/github/allanino/DNA/master/landscape.png
        :target: https://landscape.io/github/allanino/DNA/master

.. image:: https://img.shields.io/pypi/v/file2dna.svg
    :target: https://pypi.python.org/pypi/file2dna/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/file2dna.svg
    :target: https://pypi.python.org/pypi/file2dna
    :alt: License

|

This is a Python script to encode/decode arbitrary computer files into
DNA sequences. It is a straight implementation of a method published in
`this`_ Nature’s paper. The details of the method can be found in the
`Supplementary Information`_ report. Another version of report can be 
`found here`_. The source code organization follows the article steps and 
nomenclature, so it should be easy to understand. 

How to use
----------

Install it using pip:

.. code-block:: console

    $ sudo pip install file2dna

The installed script will be called ``dna`` and accepts four types of operations passed as arguments together
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
      -j          decode .splitted.zip file and save it as .decoded

As an example, we can decode one the `files`_ encoded by the authors of
the paper. Suppose you have cloned this repo with its examples folder:

.. code-block:: console

    $ dna -d examples/DNA_versions/wssnt10.txt.dna

To see the decoded file:

.. code-block:: console

    $ cat examples/DNA_versions/wssnt10.txt.decoded

Additional information about this work
----------

`Nick Goldman talking about DNA Hard Drivers at the WEF2015`_

`Goldman group DNA storage`_

`Emily Leprous talking about DNA storage`_

`Towards practical, high-capacity, low-maintenance information storage in synthesized DNA`_

Additional information about DNA storage in general
----------

`Hidding messages in DNA microdots`_

`An improved Huffman coding method for archiving text, images, and music characters in DNA`_

`Bacterial based storage and encryption device`_

`The Xenotext Experiment`_

`If You Were a Secret Message, Where in the Human Genome Would You Hide?`_

`Store digital files for eons in silica-encased DNA`_

.. _this: http://www.nature.com/nature/journal/v494/n7435/full/nature11875.html
.. _Supplementary Information: http://www.nature.com/nature/journal/v494/n7435/extref/nature11875-s2.pdf
.. _files: http://www.ebi.ac.uk/goldman-srv/DNA-storage/orig_files/
.. _found here: http://www.ebi.ac.uk/sites/ebi.ac.uk/files/groups/goldman/file2features_2.0.pdf
.. _Goldman group DNA storage: http://www.ebi.ac.uk/research/goldman/dna-storage
.. _Emily Leprous talking about DNA storage: https://vimeo.com/119612296
.. _Nick Goldman talking about DNA Hard Drivers at the WEF2015: https://www.youtube.com/watch?v=tBvd7OSDGgQ
.. _Hidding messages in DNA microdots: http://www.researchgate.net/profile/Carter_Bancroft/publication/12921709_Hiding_messages_in_DNA_microdots/links/0922b4f2ac1d18eb73000000.pdf
.. _An improved Huffman coding method for archiving text, images, and music characters in DNA: http://www.biotechniques.com/multimedia/archive/00055/Supplementary_Materi_55848a.pdf
.. _Towards practical, high-capacity, low-maintenance information storage in synthesized DNA: http://courses.cs.vt.edu/cs2104/Spring13Onufriev/LectureNotes/DNA.storage.pdf
.. _Bacterial based storage and encryption device: http://2010.igem.org/files/presentation/Hong_Kong-CUHK.pdf
.. _The Xenotext Experiment: http://triplehelixblog.com/2014/01/the-xenotext-experiment/
.. _If You Were a Secret Message, Where in the Human Genome Would You Hide?: http://nautil.us/blog/-if-you-were-a-secret-message-where-in-the-human-genome-would-you-hide
.. _Store digital files for eons in silica-encased DNA: http://hackaday.com/2015/02/21/store-digital-files-for-eons-in-silica-encased-dna