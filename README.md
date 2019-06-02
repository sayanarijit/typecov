expandvars
==========
Run type coverage checks.

[![PyPI version](https://img.shields.io/pypi/v/typecov.svg)](https://pypi.org/project/typecov)
[![Build Status](https://travis-ci.org/sayanarijit/typecov.svg?branch=master)](https://travis-ci.org/sayanarijit/typecov)
[![codecov](https://codecov.io/gh/sayanarijit/typecov/branch/master/graph/badge.svg)](https://codecov.io/gh/sayanarijit/typecov)

Usage
-----
```
typecov --help
```

```
usage: typecov [-h] [-V] coverage reportfile

Run type coverage checks.

positional arguments:
  coverage       Minimum coverage required.
  reportfile     Path to the type coverage report with line counts.

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit
```

Example
-------
```
typecov 99 .mypy/typecov_report/linecount.txt
```
