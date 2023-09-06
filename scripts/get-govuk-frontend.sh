#!/bin/sh
#
# Download the govuk-frontend package with component templates for testing.

# VERSION="4.7.0"
# URL="https://github.com/alphagov/govuk-frontend/archive/v${VERSION}.tar.gz"
# SHA256="7fbe9fee6e78df281b2c0b9eb8542105a23a4f88c0d60411b15340a977755692"

# set -e

# tarball="govuk-frontend-${VERSION}.tar.gz"

# # download
# [ -f "$tarball" ] || curl -OJL "$URL" --fail

# # check
# # echo "$SHA256 $tarball" | sha256sum --check --quiet

# # extract
# mkdir -p node_modules/govuk-frontend
# tar -xf $tarball -C node_modules/govuk-frontend --strip-components=2 "govuk-frontend-${VERSION}/package"

# echo "Installed govuk-frontend v${VERSION} to node_modules"
