#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

echo 'Content-type: text/html; charset=utf-8'
echo

"$base/gen_html.py"
