
import pytest

def test_normalise_whitespace_deletes_empty_lines():
    assert (
        pytest.helpers.normalise_whitespace(
"""
Hello world
  
  
  
This is a line below a bunch of lines which are empty except for whitespace.
"""
        )
        ==
        "Hello world\nThis is a line below a bunch of lines which are empty except for whitespace."
    )


def test_normalise_whitespace_dedents():
    assert (
        pytest.helpers.normalise_whitespace(
            """
            This is a multiline string which has been indented
            in the Python source code for readability.
            """
        )
        ==
"""This is a multiline string which has been indented\nin the Python source code for readability."""
    )


@pytest.mark.xfail
def test_normalise_whitespace_can_be_imported_with_another_name():
    from pytest.helpers import normalise_whitespace as s
    assert (
        s("""
        What's going on?

        I don't know.
        """)
        ==
        "What's going on?\nI don't know."
    )


def test_govuk_frontend_version():
    assert pytest.helpers.govuk_frontend_version_info() == (2, 4, 0)
