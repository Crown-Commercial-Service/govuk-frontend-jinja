def test_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
