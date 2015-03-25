#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

"$base/find.pl" | "$base/format.py" > "$base"/gen.json
