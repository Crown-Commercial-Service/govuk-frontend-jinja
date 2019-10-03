#!/bin/sh

if ! command -v gulp >/dev/null 2>&1
then
	2>&1 echo "error: this script requires gulp-cli but it is not installed"
	exit 1
fi

set -ex

cd node_modules/govuk-frontend-repository
[ -d node_modules ] || npm install

gulp clean copy-assets sassdoc --series

gulp watch &

cd ../..

FLASK_ENV=development flask run
