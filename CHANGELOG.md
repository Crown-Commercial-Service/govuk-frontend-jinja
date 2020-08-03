## 2020-08-03 version 0.5.2-alpha

### Bugfixes

* Fix links in README (thanks [@dalepotter](https://gitbhub.com/dalepotter)!) ([#34](https://github.com/alphagov/govuk-frontend-jinja/pull/34))

* You can now use the Nunjucks strict equality operator `===` in templates ([#50](https://github.com/alphagov/govuk-frontend-jinja/pull/50))

## 2019-11-01 version 0.5.1-alpha

### Bugfixes

* Fix issue where indent_njk was not available in Flask ([#40](https://github.com/alphagov/govuk-frontend-jinja/issues/40))

## 2019-10-29 version 0.5.0-alpha

### New features

* Enable autoescaping for Nunjucks templates in Flask ([#37](https://github.com/alphagov/govuk-frontend-jinja/pull/37))

### Bugfixes

* We have 100% coverage for components in GOV.UK Design System v2.13.0! :raised_hands: ([#3](https://github.com/alphagov/govuk-frontend-jinja/issues/3))
* Fix tests for page template ([#32](https://github.com/alphagov/govuk-frontend-jinja/pull/32))
* Fix some instances where Jinja was unable to resolve `params.items` ([#24](https://github.com/alphagov/govuk-frontend-jinja/pull/24))

## 2019-09-27 version 0.4.0-alpha

### New features

* Add support for adding undefined attributes to strings
* Refactor test fixtures to be easier to update with automated tools
* Add a tool to generate expected template output from Nunjucks
* Add tests for accordion component
* Update tests to v2.13.0 of GOV.UK Frontend! :tada:

### Bugfixes

* Include fix for indentation bug, fixes HTML escaping in file upload and text area components
* Include fix for short condexprs, fixes character count component
* We are now all green on checkboxes, file upload, and summary list! :muscle:

## 2019-09-05 version 0.3.0-alpha

### New features

* Add code to handle when Nunjucks template wants length of an array
* Add tests for summary list component

###  Bugfixes

* Fix `flask_ext` to work with Flask 1.0.x

## 2019-08-20 version 0.2.0-alpha

### Breaking changes

* Renamed from `govuk-frontend-python` to `govuk-frontend-jinja`
* Removed default filesystem loader

### New features

* Add Flask extension
* Allow importing `Environment` from top level package

### Bugfixes

* Fix bug with `join_path`

## 2019-08-13 version 0.1.0-alpha

### New features

* Add tests for all components
* Add an extension `NunjucksExtension` that preprocesses Nunjucks templates
* Add an subclass of Undefined, `NunjucksUndefined`, that deals with instances where Nunjucks is more forgiving that Jinja
* Create an example of a Jinja Environment that handles almost all incompatibilities between Nunjucks and Jinja in the govuk-frontend templates
* Add a command-line tool, `scripts/njk-to-j2.py` that can be used for debugging the extension

### Bugfixes

* Fix bug with test helper `normalise_whitespace`

## 2018-09-21 version 0.0.1

* Initial commit
