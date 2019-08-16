
import pytest

import govuk_frontend_jinja.templates


@pytest.mark.xfail
@pytest.mark.datafiles('tests/test_template/template_njk.expected.html')
def test_template_njk(datafiles):
    env = govuk_frontend_jinja.templates.Environment()
    template = env.get_template("template.njk").render()
    with open(datafiles / 'template.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'template_njk.expected.html', 'r') as expected:
        expected = pytest.helpers.normalise_whitespace(expected)
        template = pytest.helpers.normalise_whitespace(template)
        assert expected == template

@pytest.mark.xfail
@pytest.mark.datafiles(
    'tests/test_template/extends_template_njk.input.j2',
    'tests/test_template/extends_template_njk.expected.html',
)
def test_extends_template_njk(datafiles):
    env = govuk_frontend_jinja.templates.Environment()
    with open(datafiles / 'extends_template_njk.input.j2') as f:
        template = env.from_string(f.read()).render()
    with open(datafiles / 'extends_template_njk.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'extends_template_njk.expected.html', 'r') as expected:
        expected = pytest.helpers.normalise_whitespace(expected)
        template = pytest.helpers.normalise_whitespace(template)
        assert expected == template
