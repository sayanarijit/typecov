# -*- coding: utf-8 -*-

import sys
from codecs import open
from os import path

from setuptools import find_packages, setup

from typecov import (__author__, __description__, __email__, __homepage__,
                     __license__, __version__)

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup_requires = ["pytest-runner"]

tests_require = ["pytest", "pytest-cov", "mypy"]

dev_requires = ["tox"]

install_requires = []

setup(
    name="typecov",
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__homepage__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    py_modules=["typecov"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
    ],
    platforms=["Any"],
    keywords="type coverage",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require={"testing": tests_require, "dev": dev_requires},
    entry_points={"console_scripts": ["typecov = typecov:main"]},
)
