def test_tag_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_inactive(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_grey(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_blue(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_turquoise(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_green(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_purple(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_pink(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_red(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_orange(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_yellow(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


