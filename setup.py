#!/usr/bin/env python
import importlib
import os
import sys
import warnings

from setuptools import setup

if sys.version_info[0:2] < (3, 6):
    warnings.warn('This package is tested with Python version 3.6+')

root_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root_path, 'README.rst')) as readme:
    README = readme.read()

package_info = importlib.import_module('mt940_writer')

install_requires = []
tests_require = [
    'flake8', 'flake8-bugbear', 'flake8-quotes', 'flake8-blind-except', 'flake8-debugger', 'pep8-naming',
]

setup(
    name='mt940-writer',
    version=package_info.__version__,
    author=package_info.__author__,
    author_email='dev@digital.justice.gov.uk',
    url='https://github.com/ministryofjustice/mt940-writer',
    py_modules=['mt940_writer'],
    include_package_data=True,
    license='MIT',
    description='Writer for MT-940 bank statements',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='tests',
)
