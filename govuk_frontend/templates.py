
import jinja2
import jinja2.ext

import os.path as path
import re


def njk_to_j2(template):

    # Some component templates (such as radios) use `items` as the key of
    # an object element. However `items` is also the name of a dictionary
    # method in Python, and Jinja2 will prefer to return this attribute
    # over the dict item.
    template = template.replace(".items", "['items']")

    # Some component templates (such as radios) append the loop index to a
    # string. As the loop index is an integer this causes a TypeError in
    # Python. Jinja2 has an operator `~` for string concatenation that
    # converts integers to strings.
    template = template.replace("+ loop.index", "~ loop.index")

    # Some component templates (such as radios and character-count) use an
    # inline if-expression without an else statement to assemble a CSS
    # class string.
    template = re.sub(r"\b(.+) if \1(?! else)", r"\1 if \1 else ''", template)

    # Nunjucks uses elseif, Jinja uses elif
    template = template.replace("elseif", "elif")

    # Some component templates (such as input) call macros with params as
    # an object which has unqoted keys. This causes Jinja to silently
    # ignore the values.
    template = re.sub(r"""^([ ]*)([^ '"#\r\n:]+?)\s*:""", r"\1'\2':", template, flags=re.M)

    # govukFieldset can accept a call block argument, however the Jinja
    # compiler does not detect this as the macro body is included from
    # the template file. A workaround is to patch the declaration of the
    # macro to include an explicit caller argument.
    template = template.replace("macro govukFieldset(params)",
                                "macro govukFieldset(params, caller=none)")

    return template


class NunjucksExtension(jinja2.ext.Extension):
    def preprocess(self, source, name, filename=None):
        if filename and filename.endswith(".njk"):
            return njk_to_j2(source)
        else:
            return source


class NunjucksUndefined(jinja2.runtime.Undefined):
    __slots__ = ()

    # copied from https://github.com/pallets/jinja/commit/19133d40593ced72eb28e230588abcc70d8b9f82
    def __getattr__(self, _):
        """Make undefined that is chainable, where both
        __getattr__ and __getitem__ return itself rather than
        raising an :exc:`UndefinedError`:
        >>> foo = ChainableUndefined(name='foo')
        >>> str(foo.bar['baz'])
        ''
        >>> foo.bar['baz'] + 42
        Traceback (most recent call last):
          ...
        jinja2.exceptions.UndefinedError: 'foo' is undefined
        """
        return self

    __getitem__ = __getattr__


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
