def test_fieldset_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_styled_as_xl_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_styled_as_large_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_styled_as_medium_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_styled_as_small_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_as_page_heading_xl(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_as_page_heading_l(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_as_page_heading_m(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_as_page_heading_s(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_as_page_heading_without_class(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_html_fieldset_content(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_with_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_legend_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_role(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


