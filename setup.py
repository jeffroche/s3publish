from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='s3publish',

    version='0.0.1',

    description='Publish a folder of html to AWS S3',
    long_description=long_description,

    url='https://github.com/jeffroche/s3p',

    author='Jeff Roche',
    author_email='jeff.roche@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='s3 static website',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['botocore'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
