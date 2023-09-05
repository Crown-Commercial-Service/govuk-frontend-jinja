def test_textarea_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_default_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_custom_rows(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_optional_form_group_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_autocomplete_attribute(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_spellcheck_enabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_spellcheck_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_hint_and_described_by(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_error_message_and_described_by(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_hint_and_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_textarea_with_hint_error_message_and_described_by(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


