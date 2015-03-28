#!/bin/sh

set -e # Exit on first error.

base="$(dirname "$0")"

echo 'Content-type: text/html; charset=utf-8'
echo
f=gen.html
if ! [ -f $f ]; then
    "$base"/gen_html.py
fi
cat $f
