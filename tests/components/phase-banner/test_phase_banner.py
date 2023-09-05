def test_phase_banner_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_tag_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_phase_banner_tag_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


