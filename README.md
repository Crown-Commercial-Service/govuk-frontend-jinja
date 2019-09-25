GOV.UK Frontend Jinja2 Client
=============================

This Python package includes classes and modules to make it easier to use the
[GOV.UK Frontend] in your Jinja2-powered Python web app.

> **NOTE**: This repository is maintained by GDS developers, but **not** the
> GOV.UK Design System team. If you have questions or need support raise an
> issue against this repo [here](#issues).

## Using with Flask

Somewhere in your `app.py` (or wherever you do your app initialisation):

```
from govuk_frontend_jinja.flask_ext import init_govuk_frontend

init_govuk_frontend(app)
```

## Developing

This repo uses [tox] for testing; if you are hacking on the code all you need
to do to test things out is run `tox` at the command line.

If for some reason you need a virtualenv with `govuk_frontend_jinja` installed
you can run `tox --devenv venv` which will create `venv` for you (requires a
recent version of tox).

## Adding Tests

`govuk_frontend_jinja` should match the output of using [Nunjucks] with
[GOV.UK Frontend] as much as possible.

The GOV.UK Design System hosts a website with examples for all components that
can be used to get tests fixtures at [govuk-frontend-review].

Tests for individual components should go in a file named
`tests/components/<component_name>/test_<component_name>.py`. For instance:

    # tests for accordion component
    tests/
    └── components/
        └── accordion/
            └── test_accordion.py

To aid in copying tests from govuk-frontend the test suite has support for
fixture files that follow a set naming scheme. Files containing a template
should be named `test_<component_name>_<test_name>.t.html`. Files
containing the expected output of the template engine should be named
`test_<component_name>_<test_name>.x.html`.

For example, for a test of the accordion component with one section open, the
test suite expects the following structure of files and folders:

    # tests for accordion component with fixture files
    tests/
    └── components/
        └── accordion/
            ├── test_accordion.py
            ├── test_accordion_with_one_section_open.t.html
            └── test_accordion_with_one_section_open.x.html

To use the fixture files a test must be written that reads and processes them.
There are two pytest fixtures in our test suite called `template` and
`expected` that simplify this. To use these, the test function must have the
same name as the fixture file; returning to our example:

    # test_accordion.py
    def test_accordion_with_one_section_open(env, template, expected, similar):
        template = env.from_string(template)
        assert similar(template.render(), expected)

Autogenerating the pytest test function based on the fixture files so you don't
need to write it yourself is planned as a future feature.

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This
covers both the codebase and any sample code in the documentation. The
documentation is &copy; Crown copyright and available under the terms of the
Open Government 3.0 licence.

[GOV.UK Frontend]: https://github.com/alphagov/govuk-frontend
[Nunjucks]: https://mozilla.github.io/nunjucks/
[Nunjucks-cli]: https://www.npmjs.com/package/nunjucks-cli
[govuk-frontend-review]: https://govuk-frontend-review.herokuapp.com
[tox]: https://tox.readthedocs.io/en/latest/index.html
