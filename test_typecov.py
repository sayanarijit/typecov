# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from random import randint
from subprocess import PIPE, Popen


def test_file_is_empty() -> None:
    emptyfilepath = "/tmp/emptyfile_{}".format(randint(0, 9999))
    open(emptyfilepath, "w").close()

    p = Popen(
        ["python", "-m", "typecov", "100", emptyfilepath], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = p.communicate()

    os.remove(emptyfilepath)

    assert p.returncode == 3
    assert stdout.decode() == ""
    assert stderr.decode() == "error: {}: File is empty.\n".format(emptyfilepath)


def test_invalid_format() -> None:
    reportfilepath = "/tmp/reportfile_{}".format(randint(0, 9999))

    with open(reportfilepath, "w") as f:
        f.write("20/100")

    p = Popen(
        ["python", "-m", "typecov", "100", reportfilepath], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = p.communicate()

    os.remove(reportfilepath)

    assert p.returncode == 3
    assert stdout.decode() == ""
    assert stderr.decode() == "error: {}: Incorrect format of coverage report.\n".format(
        reportfilepath
    )

def test_minmum_coverage_canot_greater_than_100() -> None:
    reportfilepath = "/tmp/reportfile_{}".format(randint(0, 9999))

    with open(reportfilepath, "w") as f:
        f.write("20/100")

    p = Popen(
        ["python", "-m", "typecov", "100.001", reportfilepath], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = p.communicate()

    os.remove(reportfilepath)

    assert p.returncode == 3
    assert stdout.decode() == ""
    assert stderr.decode() == "error: minimum coverage can't be greater than 100.\n"


def test_coverage_not_achieved() -> None:
    reportfilepath = "/tmp/reportfile_{}".format(randint(0, 9999))

    with open(reportfilepath, "w") as f:
        f.write("49 50")

    p = Popen(
        ["python", "-m", "typecov", "98.001", reportfilepath], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = p.communicate()

    os.remove(reportfilepath)

    assert p.returncode == 1
    assert stdout.decode() == ""
    assert stderr.decode() == (
        "fail: Required minimum type coverage of 98.001% not achieved."
        " Total coverage: 98.0%\n"
    )


def test_success() -> None:
    reportfilepath = "/tmp/reportfile_{}".format(randint(0, 9999))

    with open(reportfilepath, "w") as f:
        f.write("50 50")

    p = Popen(
        ["python", "-m", "typecov", "100", reportfilepath], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = p.communicate()

    os.remove(reportfilepath)

    assert p.returncode == 0
    assert stdout.decode() == "Total type coverage: 100.0%\n"
    assert stderr.decode() == ""
