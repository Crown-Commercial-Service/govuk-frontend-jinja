def test_select_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_no_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_selected_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_hint_text_and_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_full_width_override(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_optional_form_group_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_attributes_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_with_falsey_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_hint_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_error_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_select_item_selected_overrides_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


