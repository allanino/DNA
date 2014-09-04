DNA 
===

[![Code Health](https://landscape.io/github/allanino/DNA/master/landscape.png)](https://landscape.io/github/allanino/DNA/master)

This is a python script to encode/decode arbitrary computer files into DNA sequences.
It is a straight implementation of a method published in [this][1] Nature's paper.
The details of the method can be found in the [Supplementary Information][2] report.
The source code organization follows the article steps and nomenclature, so it should be easy to understand.

How to use
----------


The script accepts four types of operations passed as arguments together with the file name:

    ./dna.py <arg> <inputfile>

The following arguments are accepted:
* -e: encode <inputfile> and save as <inputfile>.dna
* -d: decode <inputfile(.dna)> and save as <inputfile>.decoded
* -s: encode <inputfile> splitting into various DNA segments and save as <inputfile>.splitted.zip
* -j: decode <inputfile(.splitted.zip)> joining the segments and save as <inputfile>.decoded

As a example, we can decode one the [files][3] encoded by the authors of the paper:

    ./dna.py -d examples/DNA_versions/wssnt10.txt.dna
    
To see the decoded file:

    cat examples/DNA_versions/wssnt10.txt.decoded

[1]:http://www.nature.com/nature/journal/v494/n7435/full/nature11875.html
[2]:http://www.nature.com/nature/journal/v494/n7435/extref/nature11875-s2.pdf
[3]:http://www.ebi.ac.uk/goldman-srv/DNA-storage/orig_files/
