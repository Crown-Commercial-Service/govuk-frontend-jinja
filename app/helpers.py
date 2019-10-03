import json
from pathlib import Path
import yaml

govuk_frontend_repository = Path("node_modules/govuk-frontend-repository").resolve()

config_paths = {
    k: govuk_frontend_repository / v
    for k, v in json.loads(
        (govuk_frontend_repository / "config/paths.json").read_text()
    ).items()
    if isinstance(v, str)
}

all_components = tuple(
    [p.name for p in Path(config_paths["components"]).iterdir() if p.is_dir()]
)


def get_component_data(component_name):
    yaml_path = Path(
        config_paths["components"], component_name, f"{component_name}.yaml"
    )
    return yaml.safe_load(yaml_path.read_text())


def component_name_to_macro_name(component_name):
    """Convert component name to macro name

    This helper function takes a component name and returns the corresponding
    macro name.

    Component names are lowercase, dash-separated strings (button, date-input),
    whilst macro names have a `govuk` prefix and are camel cased (govukButton,
    govukDateInput).

    >>> component_name_to_macro_name('date-input')
    'govukDateInput'
    """

    macro_name = "".join(word.capitalize() for word in component_name.split("-"))
    return f"govuk{macro_name}"


def dump_filter(obj, space=None):
    """Return object in JSON format

    Based on https://mozilla.github.io/nunjucks/templating.html#dump
    """
    return json.dumps(obj)
