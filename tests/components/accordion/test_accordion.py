def test_accordion_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_additional_descriptions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_long_content_and_description(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_one_section_open(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_all_sections_already_open(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_focusable_elements_inside(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_translations(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_custom_heading_level(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_heading_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_falsey_values(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_remember_expanded_off(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


