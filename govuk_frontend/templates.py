
import jinja2

import os.path as path
import re


# copied from https://github.com/pallets/jinja/commit/19133d40593ced72eb28e230588abcc70d8b9f82
class ChainableUndefined(jinja2.runtime.Undefined):
    """An undefined that is chainable, where both
    __getattr__ and __getitem__ return itself rather than
    raising an :exc:`UndefinedError`:
    >>> foo = ChainableUndefined(name='foo')
    >>> str(foo.bar['baz'])
    ''
    >>> foo.bar['baz'] + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    .. versionadded:: 2.11
    """
    __slots__ = ()

    def __getattr__(self, _):
        return self

    __getitem__ = __getattr__


class NunjucksLoaderMixin:
    def get_source(self, environment, template):
        contents, filename, uptodate = super().get_source(environment, template)

        # Some component templates (such as radios) use `items` as the key of
        # an object element. However `items` is also the name of a dictionary
        # method in Python, and Jinja2 will prefer to return this attribute
        # over the dict item.
        contents = contents.replace(".items", "['items']")

        # Some component templates (such as radios) append the loop index to a
        # string. As the loop index is an integer this causes a TypeError in
        # Python. Jinja2 has an operator `~` for string concatenation that
        # converts integers to strings.
        contents = contents.replace("+ loop.index", "~ loop.index")

        # Some component templates (such as radios) use an inline if-expression
        # without an else statement to assemble a CSS class string.
        contents = re.sub(r"\b(.+) if \1(?! else)", r"\1 if \1 else ''", contents)

        return contents, filename, uptodate


class NunjucksFileSystemLoader(NunjucksLoaderMixin, jinja2.loaders.FileSystemLoader):
    pass


class Environment(jinja2.Environment):
    def __init__(self, **kwargs):
        kwargs.setdefault("loader", NunjucksFileSystemLoader("node_modules/govuk-frontend"))
        kwargs.setdefault("undefined", ChainableUndefined)
        super().__init__(**kwargs)

    def join_path(self, template, parent):
        """Enable the use of relative paths in template import statements"""
        return path.normpath(path.join(path.dirname(parent), template))
