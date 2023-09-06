#!/usr/bin/env python3

"""
Generate test templates for GOV.UK Frontend
"""

import os
import json
import unicodedata
import re

from pathlib import Path


def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_').replace('-', '_')


COPONENT_AFFECTED_BOOLEAN_FEATURES = {
    'accordion': [
        'test_accordion_with_remember_expanded_off'
    ],
    'button': [
        'test_button_prevent_double_click',
        'test_button_dont_prevent_double_click',
    ],
    'error-summary': [
        'test_error_summary_autofocus_disabled',
        'test_error_summary_autofocus_explicitly_enabled'
    ],
    'exit-this-page': [
        'test_exit_this_page_testing'
    ],
    'input': [
        'test_input_with_spellcheck_enabled',
        'test_input_with_spellcheck_disabled'
    ]
}


COPONENT_AFFECTED_QUOTE_FEATURES = {
    'phase-banner': [
        'test_phase_banner_html_as_text'
    ],
    'footer': [
        'test_footer_with_html_passed_as_text_content',
    ]
}


def replace_boolean_in_options(options, component_name, filename):
    if component_name in COPONENT_AFFECTED_BOOLEAN_FEATURES:
        if filename in COPONENT_AFFECTED_BOOLEAN_FEATURES[component_name]:
            if ": false" in options:
                options = options.replace(': false', ': "false"')
            if ": true" in options:
                options = options.replace(': true', ': "true"')

    return options


def replace_quotes_in_html(html, component_name, filename):
    if component_name in COPONENT_AFFECTED_QUOTE_FEATURES:
        if filename in COPONENT_AFFECTED_QUOTE_FEATURES[component_name]:
            html = html.replace('&quot;', '&#34;')

    return html


def main():
    INPUT_PATH = 'node_modules/govuk-frontend/govuk/components/'
    OUTPUT_PATH = 'tests/components/'

    components = next(os.walk(INPUT_PATH))[1]

    for component in components:
        with open(f'{INPUT_PATH}{component}/fixtures.json', 'r') as json_file:
            fixtures = json.load(json_file)

            component_name = fixtures['component']
            macro_name = f'govuk{component_name.replace("-", " ").title().replace(" ", "")}'

            Path(f'{OUTPUT_PATH}{component_name}').mkdir(parents=True, exist_ok=True)

            with open(f'{OUTPUT_PATH}{component_name}/test_{slugify(component_name)}.py', 'w') as test_file:
                for fixture in fixtures['fixtures']:
                    filename = f'test_{slugify(component_name)}_{slugify(fixture["name"])}'

                    test_file.write(f'def {filename}(env, similar, template, expected):\n')
                    test_file.write('    template = env.from_string(template)\n')
                    test_file.write('    assert similar(template.render(), expected)\n')
                    test_file.write('\n\n')

                    with open(f'{OUTPUT_PATH}{component_name}/{filename}.t.html', 'w') as html_file:
                        html_file.write(f'{{% from "{component_name}/macro.njk" import {macro_name} %}}\n')
                        html_file.write('\n')
                        html_file.write(f"{{{{ {macro_name}({{")
                        html_file.write('\n')

                        options = json.dumps(fixture['options'], indent=4)[2:-2]
                        options = replace_boolean_in_options(options, component_name, filename)

                        html_file.write(options)
                        html_file.write('\n')
                        html_file.write("}) }}")

                    with open(f'{OUTPUT_PATH}{component_name}/{filename}.x.html', 'w') as html_file:
                        html = fixture['html']
                        html = replace_quotes_in_html(html, component_name, filename)
                        html_file.write(html)


if __name__ == "__main__":
    main()
