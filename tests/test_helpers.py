
import pytest

def test_normalise_whitespace():
    assert (
        pytest.helpers.normalise_whitespace(
"""

  Hello world
  
  
  
  This is a line below a bunch of lines which are empty except for whitespace.
"""
        )
        ==
"""  Hello world
  This is a line below a bunch of lines which are empty except for whitespace.
"""
    )
