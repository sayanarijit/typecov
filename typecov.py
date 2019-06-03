# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser, FileType

__author__ = "Arijit Basu"
__email__ = "sayanarijit@gmail.com"
__homepage__ = "https://github.com/sayanarijit/typecov"
__version__ = "v0.2.1"
__description__ = "Run type coverage checks."
__license__ = "MIT"


def main() -> int:
    """Run type coverage check."""

    parser = ArgumentParser("typecov", description=__description__)

    parser.add_argument("coverage", type=float, help="minimum coverage required.")

    parser.add_argument(
        "reportfile",
        type=FileType("r"),
        help="path to the type coverage report with line counts.",
    )

    parser.add_argument(
        "-V", "--version", action="version", version="typecov {}".format(__version__)
    )

    args = parser.parse_args()
    coverage_summary = args.reportfile.read().strip()
    if not coverage_summary:
        print("error: {}: File is empty.".format(args.reportfile.name), file=sys.stderr)
        return 3

    try:
        covered, total, *_ = coverage_summary.split()
    except ValueError:
        print(
            "error: {}: Incorrect format of coverage report.".format(
                args.reportfile.name
            ),
            file=sys.stderr,
        )
        return 3

    coverage = (int(covered) * 100) / int(total)

    if coverage < args.coverage:
        print(
            (
                "fail: Required minimum type coverage of {}% not achieved."
                " Total coverage: {}%"
            ).format(args.coverage, coverage),
            file=sys.stderr,
        )
        return 1

    print("Total type coverage: {}%".format(coverage))
    return 0


if __name__ == "__main__":
    sys.exit(main())
