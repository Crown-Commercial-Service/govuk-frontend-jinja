def test_breadcrumbs_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_with_one_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_with_multiple_levels(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_without_the_home_section(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_with_last_breadcrumb_as_current_page(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_with_collapse_on_mobile(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_with_inverted_colours(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_item_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_breadcrumbs_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


