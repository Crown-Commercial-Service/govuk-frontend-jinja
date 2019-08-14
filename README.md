GOV.UK Frontend Jinja Client
=============================

This Python package includes classes and modules to make it easier to use the
[GOV.UK Frontend] in your Jinja-powered Python web app.

## Using with Flask

Somewhere in your `app.py` (or wherever you do your app initialisation):

```
from govuk_frontend.flask_ext import init_govuk_frontend

init_govuk_frontend(app)
```

## Developing

This repo uses [tox] for testing; if you are hacking on the code all you need
to do to test things out is run `tox` at the command line.

If for some reason you need a virtualenv with `govuk_frontend` installed you
can run `tox --devenv venv` which will create `venv` for you (requires a recent
version of tox).

## Adding Tests

`govuk_frontend_jinja` should match the output of using [Nunjucks] with
[GOV.UK Frontend] as much as possible.

If you want to see what the output of Nunjucks would be or to create a fixture
file you can use [Nunjucks-cli].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This
covers both the codebase and any sample code in the documentation. The
documentation is &copy; Crown copyright and available under the terms of the
Open Government 3.0 licence.

[GOV.UK Frontend]: https://github.com/alphagov/govuk-frontend
[Nunjucks]: https://mozilla.github.io/nunjucks/
[Nunjucks-cli]: https://www.npmjs.com/package/nunjucks-cli
[tox]: https://tox.readthedocs.io/en/latest/index.html
