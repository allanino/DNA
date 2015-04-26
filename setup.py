import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='file2dna',
    version='0.4',
    author = 'Allan Inocencio de Souza Costa',
    author_email = 'allaninocencio@yahoo.com.br',
    description = 'A script to encode/decode arbitrary computer files into DNA sequences.',
    url= 'https://github.com/allanino/DNA',
    packages=['dna'],
    include_package_data=True,
    license='MIT',
    keywords= 'dna encoding decoding file',
    long_description=read('README.rst'),
    entry_points = {
        'console_scripts': ['dna=dna.dna:main'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)