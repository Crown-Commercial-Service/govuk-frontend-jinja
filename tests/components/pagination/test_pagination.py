def test_pagination_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_custom_navigation_landmark(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_custom_link_and_item_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_custom_accessible_labels_on_item_links(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_many_pages(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_first_page(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_last_page(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_prev_and_next_only(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_prev_and_next_only_and_labels(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_prev_and_next_only_and_very_long_labels(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_prev_and_next_only_in_a_different_language(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_previous_only(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_next_only(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_custom_classes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_pagination_with_custom_attributes(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


