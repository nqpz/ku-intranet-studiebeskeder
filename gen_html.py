#!/usr/bin/env python

import os
import sys
import json
import random

base = os.path.dirname(__file__)

sys.stdout.write('''<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Studiebeskeder</title>
    <style type="text/css">
body {
  overflow: hidden;
  font-family: 'URW Palladio L', Gentium, sans;
  background-color: #f2ffee;
  color: #000464;
}

* {
  margin: 0;
  padding: 0;
}

h1 {
  text-align: center;
  font-family: Gentium;
  font-size: 90px;
  font-style: italic;
  font-weight: bold;
  color: red;
  margin-top: 10px;
  margin-bottom: 20px;
}

h2 {
  font-size: 40px;
  margin: 0 5px;
}

h2 div {
  float: left;
}

.date {
  width: 290px;
  margin-right: 10px;
  color: grey;
  text-align: right;
}

.title {
  width: 1600px;
}

    </style>
  </head>
  <body>
    <h1>Studiebeskeder fra KUnet</h1>
    <div id="nyheder">
''')

nyheder = json.load(sys.stdin, encoding='utf-8')[:14]
for i in range(len(nyheder)):
    nyhed = nyheder[i]
    h2size = 60 - i * 2
    sys.stdout.write(('''
<div>
  <hr>
  <h2 style="font-size: ''' + str(h2size) + '''px;"><div class="date">%s</div><div class="title">%s</div></h2>
  <div style="clear: both;"></div>
</div>
''' % (nyhed['date'], nyhed['title'])).encode('utf-8'))
    
sys.stdout.write('''    </div>
  </body>
</html>
''')
