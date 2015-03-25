#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

echo 'Content-type: application/json; charset=utf-8'
echo
f=gen.json
if ! [ -f $f ]; then
    "$base"/gen.sh
fi
cat $f
