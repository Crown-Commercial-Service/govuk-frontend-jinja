def test_label_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_with_bold_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_styled_as_xl_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_styled_as_large_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_styled_as_medium_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_styled_as_small_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_as_page_heading_xl(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_as_page_heading_l(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_as_page_heading_m(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_as_page_heading_s(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_as_page_heading_without_class(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_empty(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_for(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_label_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


