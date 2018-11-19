
import pytest

import govuk_frontend.templates

@pytest.mark.datafiles('tests/test_template_html/template.expected.html')
def test_template_njk(datafiles):
    env = govuk_frontend.templates.Environment()
    template = env.get_template("template.njk").render() + '\n'
    with open(datafiles / 'template.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'template.expected.html', 'r') as expected:
        assert expected.read() == template

@pytest.mark.datafiles('tests/test_template_html/template.expected.html')
def test_extends_template_njk(datafiles):
    env = govuk_frontend.templates.Environment()
    template = env.from_string("""{% extends "template.njk" %}""").render() + '\n'
    with open(datafiles / 'template.out.html', 'w') as out:
        out.write(template)
    with open(datafiles / 'template.expected.html', 'r') as expected:
        assert expected.read() == template
