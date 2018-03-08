# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-generator-short-code',  # Required
    version='0.1.0',  # Required
    description='Generate randow short code.',  # Required

    # that file directly (as we have already done above)
    # project.
    author='Bikarys',  # Optional
    author_email='anthony.bayle@gmail.com',  # Optional
    keywords='random code generator shortcode',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
)
