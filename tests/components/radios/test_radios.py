def test_radios(env, similar, template, expected):
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


def test_radios_with_a_conditional(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_hints_on_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_without_fieldset(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_radios_with_all_fieldset_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
