def test_input(env, template, expected):
    template = env.from_string(template)
    assert template.render() == expected


def test_input_with_hint_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_input_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_input_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
