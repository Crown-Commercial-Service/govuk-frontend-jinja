def test_checkboxes_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_pre_checked_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_divider_and_none(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_divider_none_and_conditional_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_id_and_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_hints_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_disabled_item(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_legend_as_a_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_a_medium_legend(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_without_fieldset(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_single_option_set_aria_describedby_on_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_single_option_and_hint_set_aria_describedby_on_input(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_fieldset_and_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_message_and_hints_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_very_long_option_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_conditional_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_conditional_items_with_special_characters(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_conditional_item_checked(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_optional_form_group_classes_showing_group_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small_with_long_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small_with_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small_with_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small_with_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_small_with_conditional_reveal(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_idprefix(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_falsey_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_fieldset_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_checked_item(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_items_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_empty_conditional(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_label_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_multiple_hints(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_message_and_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_hint_and_fieldset_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_label_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_fieldset_params(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_fieldset_html_params(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_single_option_set_aria_describedby_on_input_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_single_option_and_hint_set_aria_describedby_on_input_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_and_idprefix(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_with_error_message_and_fieldset_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_checkboxes_item_checked_overrides_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


