def test_panel_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_custom_heading_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_title_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_title_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_body_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_body_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_title_with_no_body_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


