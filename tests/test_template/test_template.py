
import pytest

import govuk_frontend.templates


@pytest.mark.datafiles('tests/test_template/template_njk.expected.html')
def test_template_njk(datafiles):
    env = govuk_frontend.templates.Environment()
    template = env.get_template("template.njk").render() + '\n'
    with open(datafiles / 'template.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'template_njk.expected.html', 'r') as expected:
        assert expected.read() == template

@pytest.mark.datafiles(
    'tests/test_template/extends_template_njk.input.j2',
    'tests/test_template/extends_template_njk.expected.html',
)
def test_extends_template_njk(datafiles):
    env = govuk_frontend.templates.Environment()
    with open(datafiles / 'extends_template_njk.input.j2') as f:
        template = env.from_string(f.read()).render()
    with open(datafiles / 'extends_template_njk.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'extends_template_njk.expected.html', 'r') as expected:
        assert expected.read() == template
