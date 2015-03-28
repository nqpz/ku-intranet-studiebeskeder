#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

"$base/gen_json.sh"

"$base/gen_html.py"
