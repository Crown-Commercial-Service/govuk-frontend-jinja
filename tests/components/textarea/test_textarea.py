def test_textarea(env, similar, template, expected):
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
