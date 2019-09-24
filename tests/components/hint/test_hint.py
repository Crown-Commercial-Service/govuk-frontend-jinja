def test_hint(env, template, expected):
    template = env.from_string(template)
    assert template.render() == expected
