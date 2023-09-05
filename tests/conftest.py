pytest_plugins = ["helpers_namespace"]

import pytest

from itertools import filterfalse
import json
from pathlib import Path
import re
from typing import Iterator, Union, TextIO, Tuple

import jinja2
import govuk_frontend_jinja


@pytest.helpers.register
def govuk_frontend_path():
    return Path(__file__).resolve().parents[1] / "node_modules" / "govuk-frontend" / "govuk"


@pytest.helpers.register
def govuk_frontend_version_info() -> Tuple[int, int, int]:
    """Get the version of the govuk-frontend templates

    Useful for skipping depending on whether a component
    is available or not.
    """
    with open(pytest.helpers.govuk_frontend_path() / "package.json") as package:
        return tuple(int(v) for v in json.load(package)["version"].split("."))


@pytest.fixture
def govuk_frontend():
    return pytest.helpers.govuk_frontend_path()


@pytest.fixture
def loader(govuk_frontend):
    return jinja2.FileSystemLoader(
        [govuk_frontend, govuk_frontend / "components"]
    )


@pytest.fixture
def env(loader):
    return govuk_frontend_jinja.Environment(
        loader=loader,
        autoescape=True,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def fixture_file_factory(name, typ, path):
    """
    >>> fixture_file_factory("test_default", "t", "tests/components/back_link/test_back_link.py")
    Path(tests/components/back_link/test_default.t.html)
    """
    fname = f"{name}.{typ}.html"
    f = Path(path).parent / fname
    return f


@pytest.fixture
def file_factory(request):
    return lambda name, typ: fixture_file_factory(name, typ, request.fspath)


@pytest.fixture(scope="function")
def template(request):
    return fixture_file_factory(request.node.name, "t", request.fspath).read_text()


@pytest.fixture(scope="function")
def expected(request):
    return fixture_file_factory(request.node.name, "x", request.fspath).read_text()


@pytest.helpers.register
def normalise_whitespace(buf: Union[str, TextIO]) -> str:
    """Delete lines that are empty/contain only whitespace"""

    def IS_LINE_JUNK(line):
        return bool(re.match(r"^\s*$", line))

    def readlines(buf: Union[str, TextIO]) -> Iterator[str]:
        if isinstance(buf, str):
            return buf.splitlines(keepends=True)
        else:
            return buf.readlines()

    lines = filterfalse(IS_LINE_JUNK, readlines(buf))
    return ("".join(lines)).strip()


@pytest.fixture
def similar():
    norm = pytest.helpers.normalise_whitespace

    def assert_similar(a, b):
        __tracebackhide__ = True
        assert norm(a) == norm(b)
        return True

    return assert_similar
