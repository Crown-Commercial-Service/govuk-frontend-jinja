def test_tabs_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_tabs_with_anchor_in_panel(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_title(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_item_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_panel_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_no_item_list(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_empty_item_list(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_with_falsey_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_idprefix(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


