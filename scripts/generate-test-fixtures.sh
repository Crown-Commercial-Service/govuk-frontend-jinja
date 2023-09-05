#!/bin/sh
#
# Generate the expected output for all test fixture using Nunjucks

if ! command -v nunjucks >/dev/null 2>&1
then
	2>&1 echo "error: this script requires nunjucks-cli but it is not installed"
	2>&1 echo
	2>&1 echo "Please ensure that Node and npm are installed and then run:"
	2>&1 echo "    npm install -g github:lfdebrux/nunjucks-cli#dev"
	exit 1
fi

nunjucks \
	--path tests/components \
	--path node_modules/govuk-frontend/govuk \
	--path node_modules/govuk-frontend/govuk/components \
	--out tests/components \
	--original-extension .t.html \
	--extension x.html \
	'**/*.t.html'
