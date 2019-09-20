import pytest


def test_checkboxes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_id_and_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_hints_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_disabled_item(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_legend_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_a_medium_legend(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_without_fieldset(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_all_fieldset_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
