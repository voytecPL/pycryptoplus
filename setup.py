#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pycryptoplus',
      version='0.0.1',
      description='pycryptodome (PyCrypto) Cipher extension. Modified to work with pycryptodome.',
      author='Christophe Oosterlynck. Modified and published by Wojciech Jakubas <wojciech.jakubas@gmail.com>',
      author_email='tiftof@gmail.com',
      url='https://github.com/voytecPL/pycryptoplus',
      packages = find_packages('src'),
      install_requires = ['pycryptodome'],
      package_dir={'': 'src'}
     )

