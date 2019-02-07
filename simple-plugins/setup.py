# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='simple-plugins',
    version='0.0.1',
    modules=['simple_plugins'],
    entry_points={
        'simple.plugins': [
            'foo = simple_plugins:foo_plugin',
            'bar = simple_plugins:bar_plugin',
        ]
    },
    author='Eugene Prilepin',
    description='A minimal example of python plugins powered by setuptools (Plugins)'
)
