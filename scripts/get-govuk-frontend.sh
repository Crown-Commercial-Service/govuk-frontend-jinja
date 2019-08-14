#!/bin/sh
#
# Download the govuk-frontend package with component templates for testing.

VERSION="2.4.0"
URL="https://github.com/alphagov/govuk-frontend/archive/v${VERSION}.tar.gz"
SHA256="a8be5ab794aefa906e3710db5ae3520da800182985cd2d44397ab1cbe82544b9"

set -e

tarball="govuk-frontend-${VERSION}.tar.gz"

# download
[ -f "$tarball" ] || curl -OJL "$URL" --fail

# check
echo "$SHA256 $tarball" | sha256sum --check --quiet

# extract
mkdir -p node_modules/govuk-frontend
tar -xf $tarball -C node_modules/govuk-frontend --strip-components=2 "govuk-frontend-${VERSION}/package/"

echo "Installed govuk-frontend v${VERSION} to node_modules"
