def test_label(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_for(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_with_undefined_params(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
