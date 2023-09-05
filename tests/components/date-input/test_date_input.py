def test_date_input_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_complete_question(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_errors_only(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_errors_and_hint(env, similar, template, expected):
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


def test_date_input_with_optional_form_group_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_autocomplete_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_input_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_empty_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_custom_pattern(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_custom_inputmode(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_nested_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_id_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_suffixed_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_hint_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_with_error_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_fieldset_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_items_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_date_input_items_without_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


