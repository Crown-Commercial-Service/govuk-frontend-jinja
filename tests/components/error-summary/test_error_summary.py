def test_error_summary_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_without_links(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_mixed_with_and_without_links(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_with_everything(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_html_as_titletext(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_title_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_description(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_html_as_descriptiontext(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_description_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_error_list_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_error_list_with_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_error_list_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_error_list_with_html_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_error_list_with_html_as_text_link(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_autofocus_disabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_error_summary_autofocus_explicitly_enabled(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


