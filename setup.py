#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='iata_codes',
        version='0.1',
        description='A database for iata codes',
        author='Elijah Eaton',
        author_email='eaton.elijah@gmail.com',
        install_requires=[
            'pandas',
            'beautifulsoup4',
            'lxml',
        ],
    )
