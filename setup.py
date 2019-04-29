#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["Click>=6.0", "vcfpy==0.12.0", "pysam==0.15.2",
                "pandas>=0.24.2", "aiohttp==3.5.4", "aiofiles==0.4.0"]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(  # pragma: no cover
    author="Roberto Preste",
    author_email='robertopreste@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Human mitochondrial variants annotation using HmtVar. ",
    entry_points={
        'console_scripts': [
            'hmtnote=hmtnote.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords='hmtnote',
    name='hmtnote',
    packages=find_packages(include=['hmtnote']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/robertopreste/hmtnote',
    version='0.5.1',
    zip_safe=False,
)
