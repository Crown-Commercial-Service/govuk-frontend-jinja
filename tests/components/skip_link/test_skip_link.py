def test_skip_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
