#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

out=$(mktemp)

"$base/find.pl" | "$base/format.py" > $out

cat $out > "$base"/gen.json
