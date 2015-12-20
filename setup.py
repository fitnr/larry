#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of larry
from setuptools import setup

setup(
    name='larry',

    version='0.1',

    description='larry',

    url='http://github.com/fitnr/larry',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    license='All rights reserved',

    packages=[
        'larry',
    ],

    entry_points={
        'console_scripts': [
            'larry=larry:main',
        ],
    },

    zip_safe=True,

    install_requires=[
        'Pillow>=3,<3.1',
        'moviepy>=0.2.2.11,<0.3',
    ],
)
