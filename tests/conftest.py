pytest_plugins = ["helpers_namespace"]

import pytest

from itertools import filterfalse
import json
import re
from textwrap import dedent
from typing import Iterator, Union, TextIO, Tuple

import jinja2
import govuk_frontend_jinja


@pytest.helpers.register
def IS_LINE_JUNK(line):
    return bool(re.match(r"^\s*$", line))


@pytest.helpers.register
def readlines(buf: Union[str, TextIO]) -> Iterator[str]:
    if isinstance(buf, str):
        return buf.splitlines(keepends=True)
    else:
        return buf.readlines()


@pytest.helpers.register
def normalise_whitespace(buf: Union[str, TextIO]) -> str:
    """Delete lines that are empty/contain only whitespace"""
    lines = filterfalse(IS_LINE_JUNK, readlines(buf))
    return dedent("".join(lines)).strip()


@pytest.helpers.register
def govuk_frontend_version_info() -> Tuple[int, int, int]:
    """Get the version of the govuk-frontend templates

    Useful for skipping depending on whether a component
    is available or not.
    """
    with open("node_modules/govuk-frontend/package.json") as package:
        return tuple(int(v) for v in json.load(package)["version"].split("."))


@pytest.fixture
def loader():
    return jinja2.FileSystemLoader(
        ["node_modules/govuk-frontend", "node_modules/govuk-frontend/components"]
    )


@pytest.fixture
def env(loader):
    return govuk_frontend_jinja.Environment(loader=loader)
