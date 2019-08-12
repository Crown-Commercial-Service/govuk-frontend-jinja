
import jinja2
import jinja2.ext

import os.path as path


def njk_to_j2(template):
    return template


class NunjucksExtension(jinja2.ext.Extension):
    def preprocess(self, source, name, filename=None):
        if filename and filename.endswith(".njk"):
            return njk_to_j2(source)
        else:
            return source


class NunjucksUndefined(jinja2.runtime.Undefined):
    __slots__ = ()


class Environment(jinja2.Environment):
    def __init__(self, **kwargs):
        kwargs.setdefault("extensions", [NunjucksExtension])
        kwargs.setdefault("loader",
            jinja2.FileSystemLoader([
                "node_modules/govuk-frontend",
                "node_modules/govuk-frontend/components",
        ]))
        kwargs.setdefault("undefined", NunjucksUndefined)
        super().__init__(**kwargs)

    def join_path(self, template, parent):
        """Enable the use of relative paths in template import statements"""
        return path.normpath(path.join(path.dirname(parent), template))
