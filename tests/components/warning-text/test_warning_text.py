def test_warning_text_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_multiple_lines(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_icon_fallback_text_only(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_warning_text_no_icon_fallback_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


