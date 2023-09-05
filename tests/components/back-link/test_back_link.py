def test_back_link_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_with_custom_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_with_inverted_colours(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_back_link_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


