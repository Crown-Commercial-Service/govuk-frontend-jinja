from pathlib import Path
import json

from flask import (
    Flask,
    render_template,
    render_template_string,
    request,
    send_from_directory,
)
import jinja2

from govuk_frontend_jinja.flask_ext import init_govuk_frontend

from . import helpers
from .helpers import config_paths

app = Flask(__name__.split(".")[0])

app.jinja_options = {
    "autoescape": True,  # output with dangerous characters are escaped automatically
    "lstrip_blocks": True,  # automatically remove trailing newlines from a block/tag
    "trim_blocks": True,  # automatically remove leading whitespace from a block/tag
    "auto_reload": True,  # reload templates when they are changed
}

app.jinja_loader = jinja2.FileSystemLoader(
    [
        config_paths["layouts"].__fspath__(),
        config_paths["views"].__fspath__(),
        config_paths["components"].__fspath__(),
        config_paths["src"].__fspath__(),
    ]
)

init_govuk_frontend(app)

app.add_template_filter(
    helpers.component_name_to_macro_name, name="componentNameToMacroName"
)
app.add_template_filter(helpers.dump_filter, name="dump")


@app.route("/public/<path:filename>")
def public(filename):
    return send_from_directory(config_paths["public"], filename)


@app.route("/docs")
@app.route("/docs/<path:filename>")
def sassdoc(filename="index.html"):
    return send_from_directory(config_paths["sassdoc"], filename)


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(
        config_paths["src"] / "assets", filename, cache_timeout=3600
    )


@app.route("/")
def index():
    components = helpers.all_components
    examples = [f.name for f in config_paths["examples"].iterdir()]
    full_page_examples = [f.name for f in config_paths["fullPageExamples"].iterdir()]

    return render_template(
        "index.njk",
        componentsDirectory=components,
        examplesDirectory=examples,
        fullPageExamplesDirectory=full_page_examples,
    )


@app.route("/components/<component>")
def component(component):
    component_data = helpers.get_component_data(component)

    return render_template(
        "component.njk",
        componentData=component_data,
        componentPath=component,
        legacyQuery="",
    )


@app.route("/components/<component>/preview")
@app.route("/components/<component>/<example>/preview")
def component_preview(component, example="default"):
    component_data = helpers.get_component_data(component)
    preview_layout = component_data.get("previewLayout", "layout")
    example_config = [
        c for c in component_data["examples"] if c["name"].replace(" ", "-") == example
    ][0]

    macro_name = helpers.component_name_to_macro_name(component)
    macro_parameters = json.dumps(example_config["data"])

    component_view = render_template_string(
        f"""{{% from '{component}/macro.njk' import {macro_name} %}}
        {{{{ {macro_name}({macro_parameters}) }}}}"""
    )

    body_classes = (
        "app-iframe-in-component-preview" if request.args.get("iframe") else ""
    )

    return render_template(
        "component-preview.njk",
        bodyClasses=body_classes,
        componentPath=component,
        componentView=component_view,
        legacyQuery="",
        previewLayout=preview_layout,
    )
