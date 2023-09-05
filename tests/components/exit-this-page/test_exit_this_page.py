def test_exit_this_page_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_exit_this_page_translated(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_exit_this_page_testing(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_exit_this_page_testing_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


