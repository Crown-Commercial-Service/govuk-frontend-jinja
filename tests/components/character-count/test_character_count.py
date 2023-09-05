def test_character_count_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_custom_textarea_description(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_default_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_default_value_exceeding_limit(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_custom_rows(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_word_count(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_threshold(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_translations(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_formgroup_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_custom_classes_on_countmessage(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_spellcheck_enabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_spellcheck_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_custom_classes_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_id_starting_with_number(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_id_with_special_characters(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_with_textarea_maxlength_attribute(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_to_configure_in_javascript(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_when_neither_maxlength_nor_maxwords_are_set(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_character_count_when_neither_maxlengthmaxwords_nor_textarea_description_are_set(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


