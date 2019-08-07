
import jinja2

import os.path as path


class NunjucksLoaderMixin:
    pass


class NunjucksFileSystemLoader(NunjucksLoaderMixin, jinja2.loaders.FileSystemLoader):
    pass


class Environment(jinja2.Environment):
    def __init__(self, **kwargs):
        kwargs.setdefault("loader", NunjucksFileSystemLoader("node_modules/govuk-frontend"))
        super().__init__(**kwargs)

    def join_path(self, template, parent):
        """Enable the use of relative paths in template import statements"""
        return path.normpath(path.join(path.dirname(parent), template))
