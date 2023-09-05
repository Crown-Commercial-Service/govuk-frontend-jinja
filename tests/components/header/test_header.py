def test_header_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name_but_no_service_url(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_custom_navigation_label(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_custom_menu_button_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_custom_menu_button_label(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name_and_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_large_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_product_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_full_width(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_full_width_with_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_navigation_item_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_navigation_item_with_text_without_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_custom_homepage_url(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_navigation_item_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_navigation_item_with_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_navigation_item_with_html_without_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_custom_navigation_label_and_custom_menu_button_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


