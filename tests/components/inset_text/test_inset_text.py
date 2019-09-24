def test_inset_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_inset_text_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
