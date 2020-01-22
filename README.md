
GOV.UK Frontend (Jinja) ·
[![Build Status](https://travis-ci.com/alphagov/govuk-frontend-jinja.svg?branch=master)](https://travis-ci.com/alphagov/govuk-frontend-jinja)
=========================

This Python package includes classes and modules to make it easier to use the
[GOV.UK Frontend] in your [Jinja2][Jinja]-powered Python web app.

> **NOTE**: This repository is maintained by GDS developers, but **not** the
> GOV.UK Design System team. If you have questions or need support raise an
> issue against this repo [here](https://github.com/alphagov/govuk-frontend-jinja/issues).

## Installing

```shell
pip install git+https://github.com/alphagov/govuk-frontend-jinja.git
```

## Using with Flask

Somewhere in your `app.py` (or wherever you do your app initialisation):

```
import jinja2
from govuk_frontend_jinja.flask_ext import init_govuk_frontend

app.jinja_loader = jinja2.FileSystemLoader((
    "templates",
    "node_modules/govuk-frontend",  # path to govuk-frontend package
))

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

## Credits

The initial code for this tool was based on work by [HMLR], particularly [@andymantell](https://github.com/andymantell) 🏆

All of the HTML and templates that this tool works on were produced by the [GOV.UK Design System] 🏅

And of course, none of this would be possible without [Nunjucks] and [Jinja] 🥂

## Licence

Unless stated otherwise, the codebase is released under [the MIT License](LICENCE).
This covers both the codebase and any sample code in the documentation.

The documentation is [&copy; Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] licence.

[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

[GOV.UK Design System]: https://design-system.service.gov.uk
[GOV.UK Frontend]: https://github.com/alphagov/govuk-frontend
[HMLR]: https://github.com/LandRegistry
[Jinja]: https://palletsprojects.com/p/jinja/
[Nunjucks]: https://mozilla.github.io/nunjucks/
[Nunjucks-cli]: https://www.npmjs.com/package/nunjucks-cli
[govuk-frontend-review]: https://govuk-frontend-review.herokuapp.com
[tox]: https://tox.readthedocs.io/en/latest/index.html
