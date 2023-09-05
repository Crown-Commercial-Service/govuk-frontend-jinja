def test_table_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_table_with_head(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_table_with_head_and_caption(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_head_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_head_with_rowspan_and_colspan(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_head_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_with_firstcellisheader_true(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_firstcellisheader_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_firstcellisheader_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_firstcellisheader_with_html_as_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_firstcellisheader_with_rowspan_and_colspan(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_firstcellisheader_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_with_falsey_items(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_rows_with_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_rows_with_rowspan_and_colspan(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_rows_with_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


