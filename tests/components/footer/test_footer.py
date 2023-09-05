def test_footer_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_custom_html_content_licence_and_copyright_notice(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_custom_text_content_licence_and_copyright_notice(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_meta(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_custom_meta(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_meta_links_and_meta_content(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_custom_meta(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_default_width_navigation_one_column(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_default_width_navigation_two_columns(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_full_gds_example(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_three_equal_columns(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_container_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_html_passed_as_text_content(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_empty_meta(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_empty_meta_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_meta_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_meta_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_meta_item_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_empty_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_footer_with_navigation_item_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


