#!/bin/sh

base="$(dirname "$0")"

"$base/find.pl" | "$base/format.py" > "$base"/gen.json
