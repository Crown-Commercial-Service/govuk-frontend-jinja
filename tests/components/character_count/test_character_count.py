import pytest


def test_character_count(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


@pytest.mark.xfail(reason="overzealous escaping")
def test_character_count_with_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_default_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_default_value_exceeding_limit(
    env, similar, template, expected
):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_custom_rows(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


@pytest.mark.xfail(reason="overzealous escaping")
def test_character_count_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_word_count(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_threshold(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
