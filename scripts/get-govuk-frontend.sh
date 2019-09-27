#!/bin/sh
#
# Download the govuk-frontend package with component templates for testing.

VERSION="2.13.0"
URL="https://github.com/alphagov/govuk-frontend/archive/v${VERSION}.tar.gz"
SHA256="785683afedaae367ab106d9469080fadc518e670e6ab13cf9e4e17c641981a92"

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
