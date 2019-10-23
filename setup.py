#!/usr/bin/python
import os
import sys
from setuptools import setup

version = '0.1.1'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print(" git tag -a %s -m 'version %s'" % (version, version))
    print(" git push --tags")
    sys.exit()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='sendgrid-newsletter',
    version=version,
    author='Buddy Lindsey, Jr.',
    author_email='blindsey@consumeraffairs.com',
    include_package_data=True,
    url='https://github.com/ConsumerAffairs/sendgrid-newsletter',
    description='Library for using SendGrids newsletter api',
    install_requires=['requests==2.20.0'],
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
