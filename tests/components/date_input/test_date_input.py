import pytest


def test_date_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_errors(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_error_on_day_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_error_on_month_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_error_on_year_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_default_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
