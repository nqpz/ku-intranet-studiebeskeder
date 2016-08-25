#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

"$base/find.pl" | "$base/format_json.py" > "$base/studiebeskeder.json"

"$base/gen_html.py" < "$base/studiebeskeder.json" > "$base/infoscreen.html"
