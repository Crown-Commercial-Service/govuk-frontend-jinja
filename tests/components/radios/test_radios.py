def test_radios_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_inline(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_legend_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_a_medium_legend(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_a_divider(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_hints_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_without_fieldset(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_fieldset_and_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_very_long_option_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_conditional_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_conditional_items_with_special_characters(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_conditional_item_checked(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_prechecked(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_prechecked_using_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_conditional_items_and_pre_checked_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_optional_form_group_classes_showing_group_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_long_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_conditional_reveal(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_inline(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_inline_extreme(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_small_with_a_divider(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_idprefix(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_minimal_items_and_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_falsey_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_fieldset_with_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_items_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_empty_conditional(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_label_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_hints_on_parent_and_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_describedby_and_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_error_message_and_idprefix(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_hint_and_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_hint_error_message_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_label_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_fieldset_params(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_fieldset_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_fieldset_error_message_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_item_checked_overrides_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


