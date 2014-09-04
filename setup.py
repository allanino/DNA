
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='file2dna',
    version='0.1',
    author = 'Allan Inocencio de Souza Costa',
    author_email = 'allaninocencio@yahoo.com.br',
    description = 'A script o encode/decode arbitrary computer files into DNA sequences.',
    packages=['dna',],
    license='MIT',
    keywords= 'dna encoding decoding file',
    long_description=read('README.md'),
    entry_points = {
        'console_scripts': ['dna=dna.dna:main'],
    }
)