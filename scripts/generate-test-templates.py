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


if __name__ == "__main__":
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
                        html_file.write(json.dumps(fixture['options'], indent=4)[2:-2])
                        html_file.write('\n')
                        html_file.write(f"}}) }}}}")

                    with open(f'{OUTPUT_PATH}{component_name}/{filename}.x.html', 'w') as html_file:
                        html_file.write(fixture['html'])
