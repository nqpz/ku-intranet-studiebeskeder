#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

./gen_json.sh

./gen_html.sh
