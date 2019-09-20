def test_panel(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_panel_custom_heading_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
