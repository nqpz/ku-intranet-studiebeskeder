#!/usr/bin/env python

import sys
import json

print json.dumps(json.load(sys.stdin, encoding='utf-8'),
                 sort_keys=True, indent=2, ensure_ascii=False).encode('utf-8')
