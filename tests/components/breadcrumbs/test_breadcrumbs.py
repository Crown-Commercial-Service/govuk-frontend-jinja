def test_breadcrumbs(env, similar, template, expected):
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


def test_breadcrumbs_with_last_breadcrumb_as_current_page(
    env, similar, template, expected
):
    template = env.from_string(template)
    assert similar(template.render(), expected)
