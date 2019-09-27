import pytest

from pathlib import Path
import warnings


class CoverageWarning(UserWarning):
    pass


def test_should_have_tests_for_all_components(govuk_frontend):
    def find_components(path):
        split_words = str.maketrans("_-", "  ")
        return set(
            p.stem.translate(split_words)
            for p in path.iterdir()
            if p.is_dir() and p.name != "__pycache__"
        )

    def warn_if_tests_missing(want, got):
        if not got >= want:
            missing = want - got
            warnings.warn(
                f"the following components do not have tests: {','.join(missing)}",
                CoverageWarning,
                stacklevel=2,
            )

    expected_components = find_components(govuk_frontend / "components")
    tested_components = find_components(Path(__file__).parent)

    warn_if_tests_missing(expected_components, tested_components)
