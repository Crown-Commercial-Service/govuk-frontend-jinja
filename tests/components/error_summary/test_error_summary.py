def test_error_summary(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
