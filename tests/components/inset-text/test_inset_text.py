def test_inset_text_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


