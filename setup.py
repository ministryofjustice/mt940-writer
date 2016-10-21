import os
from setuptools import setup

version = '0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mt940-writer',
    version=version,
    py_modules=['mt940_writer'],
    license='MIT License',
    description='Writer for MT-940 bank statements',
    url='https://github.com/ministryofjustice/mt940-writer',
    long_description=README,
    install_requires=[],
    classifiers=[
        'Intended Audience :: Python Developers',
    ],
)
