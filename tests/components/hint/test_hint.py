def test_hint_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_hint_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_hint_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_hint_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_hint_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_hint_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


