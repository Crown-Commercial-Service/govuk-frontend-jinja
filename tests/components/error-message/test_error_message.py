def test_error_message_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_translated(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_with_visually_hidden_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_message_visually_hidden_text_removed(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


