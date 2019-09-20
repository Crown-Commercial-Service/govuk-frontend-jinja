def test_table(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_with_head(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_table_with_head_and_caption(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
