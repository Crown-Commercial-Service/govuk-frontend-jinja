def test_skip_link_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_with_focus(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_no_href(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_custom_href(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_custom_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_skip_link_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


