
from io import StringIO
import unittest.mock as mock
import pytest

from govuk_frontend.templates import NunjucksFileSystemLoader


@pytest.fixture
def environment():
    return mock.Mock()


@pytest.fixture
def loader():
    return NunjucksFileSystemLoader("node_modules/govuk-frontend")


def test_gets_source_from_filesystem(environment, loader):
    mock_open = mock.mock_open(read_data=b"foobar")
    with mock.patch("jinja2.utils.open", mock_open) as m:
        contents, _, _ = loader.get_source(environment, "template.njk")

        assert contents == "foobar"
        assert m.call_count == 1
