
import jinja2

import os.path as path


def njk_to_j2(template):
    return template


class Environment(jinja2.Environment):
    def __init__(self, **kwargs):
        kwargs.setdefault("loader",
            jinja2.loaders.FileSystemLoader([
                "node_modules/govuk-frontend",
                "node_modules/govuk-frontend/components",
        ]))
        super().__init__(**kwargs)

    def join_path(self, template, parent):
        """Enable the use of relative paths in template import statements"""
        return path.normpath(path.join(path.dirname(parent), template))
