import os
import sys

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

install_requires = []
tests_require = ['flake8']
if sys.version_info[0:2] < (3, 4):
    install_requires.append('enum34')

setup(
    name='mt940-writer',
    version='0.2',
    author='Ministry of Justice',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    tests_require=['flake8'],
    test_suite='tests',
)
