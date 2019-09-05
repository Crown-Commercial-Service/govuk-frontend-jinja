### New features

* Add code to handle when Nunjucks template wants length of an array
* Add tests for summary list component

##  Bugfixes

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
