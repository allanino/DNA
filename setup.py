try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Encode and decode files in DNA',
    'author': 'Allan Costa',
    'url': 'www.github.com/Allanino/DNA',
    'download_url': 'www.github.com/Allanino/DNA',
    'author_email': 'allaninocencio@yahoo.com.br',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['DNA'],
    'scripts': [],
    'name': 'DNA'
}

setup(**config)