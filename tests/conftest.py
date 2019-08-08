
pytest_plugins = ['helpers_namespace']

import pytest

import re
from typing import Iterator, Union, TextIO

@pytest.helpers.register
def IS_LINE_JUNK(line):
    return bool(re.match(r'^\s*$', line))

@pytest.helpers.register
def readlines(buf: Union[str, TextIO]) -> Iterator[str]:
    if isinstance(buf, str):
        return buf.splitlines(keepends=True)
    else:
        return buf.readlines()

@pytest.helpers.register
def normalise_whitespace(buf: Union[str, TextIO]) -> str:
    """Delete lines that are empty/contain only whitespace"""
    lines = filter(IS_LINE_JUNK, readlines(buf))
    return ''.join(lines)