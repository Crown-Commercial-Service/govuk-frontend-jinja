def test_file_upload_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_hint_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_error_message_and_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_value(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_optional_form_group_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_hint_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_error(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_error_and_describedby(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_error_describedby_and_hint(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


