
from io import StringIO
import unittest.mock as mock
import pytest

from govuk_frontend.templates import NunjucksFileSystemLoader


@pytest.fixture
def environment():
    return mock.Mock()


@pytest.fixture(autouse=True)
def template_file():
    mock_open = mock.mock_open(read_data=b"foobar")
    with mock.patch("jinja2.utils.open", mock_open):
        yield mock_open


@pytest.fixture
def loader():
    return NunjucksFileSystemLoader("node_modules/govuk-frontend")


def test_gets_source_from_filesystem(environment, template_file, loader):
    contents, _, _ = loader.get_source(environment, "template.njk")
    assert contents == "foobar"
    assert template_file.call_count == 1
