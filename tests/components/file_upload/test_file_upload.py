def test_file_upload(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_hint_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_error_message(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_value_and_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_file_upload_with_label_as_page_heading(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
