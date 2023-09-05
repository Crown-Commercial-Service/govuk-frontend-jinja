def test_notification_banner_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_paragraph_as_html_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_text_as_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_type_as_success(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_success_with_custom_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_a_list(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_long_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_lots_of_content(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_auto_focus_disabled_with_type_as_success(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_auto_focus_explicitly_enabled_with_type_as_success(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_rolealert_overridden_to_roleregion_with_type_as_success(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_tabindex(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_title(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_title_as_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_title_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_title_heading_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_title_id(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_title_id_with_type_as_success(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_custom_role(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_notification_banner_with_invalid_type(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


