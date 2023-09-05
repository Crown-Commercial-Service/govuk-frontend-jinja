def test_summary_list_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_translated(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_some_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_no_first_action(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_no_border(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_no_border_on_last_row(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_overridden_widths(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_check_your_answers(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_extreme(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_as_a_summary_card_with_a_text_header(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_as_a_summary_card_with_a_custom_header_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_as_a_summary_card_with_a_html_header(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_as_a_summary_card_with_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_as_a_summary_card_with_actions_plus_summary_list_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_falsey_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_key_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_key_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_value_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_actions_href(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_actions_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_actions_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_actions_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_single_action_with_anchor(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_classes_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_empty_items_array(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_rows_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_summary_card_with_custom_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_summary_card_with_custom_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_summary_card_with_only_1_action(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


