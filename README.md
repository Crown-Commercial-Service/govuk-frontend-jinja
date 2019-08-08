GOV.UK Frontend Python Client
=============================

This Python package includes classes and modules to make it easier to use the
[GOV.UK Frontend] in your Python web app.

## Developing

This repo uses [tox] for testing; if you are hacking on the code all you need
to do to test things out is run `tox` at the command line.

If for some reason you need a virtualenv with `govuk_frontend` installed you
can run `tox -e develop` which will create `venv` for you.

## Adding Tests

`govuk_frontend_python` should match the output of using [Nunjucks] with
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