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
    list(
        map(
            str,
            [
                config_paths["layouts"],
                config_paths["views"],
                config_paths["examples"],
                config_paths["components"],
                config_paths["src"],
            ],
        )
    )
)

init_govuk_frontend(app)

app.add_template_filter(
    helpers.component_name_to_macro_name, name="componentNameToMacroName"
)

app.add_template_filter(helpers.dump_filter, name="dump")

# Replace escape with forceescape
# TODO: why do we need this?
app.add_template_filter(jinja2.filters.do_forceescape, name="e")


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


# Define middleware for all routes
@app.context_processor
def inject_legacy_query():
    return {"legacyQuery": "?legacy=1" if request.args.get("legacy") else ""}


# Define routes


@app.route("/")
def index():
    """Index page - render the component list template"""

    components = helpers.all_components
    examples = [f.name for f in config_paths["examples"].iterdir()]
    full_page_examples = [f.name for f in config_paths["fullPageExamples"].iterdir()]

    return render_template(
        "index.njk",
        componentsDirectory=components,
        examplesDirectory=examples,
        fullPageExamplesDirectory=full_page_examples,
    )


@app.route("/components/all")
def all_components():
    """All components view"""
    component_data = []

    for component in helpers.all_components:
        _component_data = helpers.get_component_data(component)
        default_example = [
            example
            for example in _component_data["examples"]
            if example["name"] == "default"
        ]
        component_data.append({"componentName": component, "examples": default_example})

    return render_template("all-components.njk", componentData=component_data)


@app.route("/components/<component>")
def component(component):
    """Component 'README' page"""
    component_data = helpers.get_component_data(component)

    return render_template(
        "component.njk", componentData=component_data, componentPath=component
    )


@app.route("/components/<component>/preview")
@app.route("/components/<component>/<example>/preview")
def component_preview(component, example="default"):
    """Component example preview"""
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
        previewLayout=preview_layout,
    )


@app.route("/examples/<example>")
def example(example):
    """Example view"""
    return render_template(f"{example}/index.njk")
