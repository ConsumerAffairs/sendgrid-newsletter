#!/usr/bin/python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='sendgrid-newsletter',
    version='0.1',
    author='Buddy Lindsey, Jr.',
    author_email='blindsey@consumeraffairs.com',
    url='https://github.com/ConsumerAffairs/sendgrid-newsletter',
    description='Library for using SendGrids newsletter api',
    install_requires=['requests==2.2.1'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Email'
    ],
    packages=['sendgridnewsletter'],
    long_description=read('README.md')
)
