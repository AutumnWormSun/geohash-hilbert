# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import find_packages, setup

setup_cython = dict()
try:
    from Cython.Build import cythonize
    setup_cython = dict(ext_modules=cythonize('geohash_hilbert/_hilbert_cython.pyx'))
except:
    pass

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

version = '0.1'

setup(
    name='geohash-hilbert',
    version=version,
    packages=find_packages(),
    install_requires=[],
    author='Tammo Ippen',
    author_email='tammo.ippen@posteo.de',
    description='Geohash a lng/lat coordinate using the hilbert curve.',
    long_description=long_description,
    url='https://github.com/tammoippen/geohash-hilbert',
    download_url='https://github.com/tammoippen/geohash-hilbert/archive/v{}.tar.gz'.format(version),
    keywords=['geohash', 'hilbert', 'space filling curve', 'geometry'],
    **setup_cython
)