def test_cookie_banner_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_accepted_confirmation_banner(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_rejected_confirmation_banner(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_client_side_implementation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_heading_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_heading_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_custom_aria_label(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_hidden(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_hidden_false(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_default_action(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_link_with_false_button_options(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_link_as_a_button(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_type(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_button_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_button_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_link_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_link_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_cookie_banner_full_banner_hidden(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


