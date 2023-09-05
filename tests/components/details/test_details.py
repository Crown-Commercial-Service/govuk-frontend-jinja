def test_details_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_expanded(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_summary_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_summary_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


