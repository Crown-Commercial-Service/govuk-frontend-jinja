import pytest

import warnings


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
    version_info = pytest.helpers.govuk_frontend_version_info()
    # assert check_type(version_info, Tuple[int, int, int])
    assert isinstance(version_info, tuple)
    assert all(isinstance(i, int) for i in version_info)

    def warn_if_not_matching_version(want, got):
        if want != got:
            warnings.warn(
                f"Found govuk-frontend version {got}, expected {want} - some tests may fail because of this! To ensure you have the correct version downloaded run ./scripts/get-govuk-frontend.sh",
                stacklevel=2,
            )

    warn_if_not_matching_version((2, 13, 0), version_info)
