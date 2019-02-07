# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='simple-core',
    version='0.0.1',
    modules=['simple_core'],
    entry_points={
        'console_scripts': [
            'simple_core = simple_core:main'
        ]
    },
    author='Eugene Prilepin',
    description='A minimal example of python plugins powered by setuptools (Core)'
)
