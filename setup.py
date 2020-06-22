#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='demopkg',
      version='1.0',
      description='examplestuff',
      author='Greg Ward',
      author_email='lex@mail.uk',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(include=['examplecode']),
      scripts=["bin/rundemo.py"],
      data_files=[('ansible', ['data/play1.yaml'])],
      include_package_data=True,
      zip_safe=False,
     )




