def test_phase_banner(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_with_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
