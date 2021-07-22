# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='line_botkit',
    version='0.0.1',
    packages=['line_botkit'],
    install_requires=open('requirements.txt').read().splitlines(),
)
