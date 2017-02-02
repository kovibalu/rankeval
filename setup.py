
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='sample',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='Implementation of ranking metrics nDCG and MRR',

    # The project's main homepage.
    url='https://github.com/kovibalu/rankeval',

    # Author details
    author='Eleftherios Avramidis',
    author_email='',

    # Choose your license
    license='GNU GPL',

    # What does your project relate to?
    keywords='ranking metrics ndcg mrr',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
)
