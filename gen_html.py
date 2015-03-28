#!/usr/bin/env python

import os
import sys
import json


def shorten(html):
    return html

base = os.path.dirname(__file__)
with open(os.path.join(base, 'gen.html'), 'w') as f:
    f.write('''<!doctype html>
<html>
  <head>
    <title>Studiebeskeder</title>
    <style type="text/css">
body {
  margin: 0;
  font-family: 'URW Palladio L';
}

.nyhed {
  width: 460px;
  height: 325px;
  float: left;
  margin: 5px;
  padding: 3px;
  overflow: hidden;
  border: 1px dotted silver;
  background-color: lightblue;
}

h1, h2, h3, p {
  margin: 0 0 5px 0;
}

h1.container {
  margin: 5px 0 0 0;
  font-size: 35px;
  font-family: Gentium;
  font-style: italic;
  color: red;
  text-align: center;
}
    
h2.container {
  margin: 0;
  font-size: 30px;
}

h3.container {
  margin: 0;
  font-size: 20px;
}

.date {
  font-style: italic;
  color: #333;
  text-align: right;
}

    </style>
  </head>
  <body>
    <h1 class="container">Studiebeskeder</h1>
    <div id="nyheder">
''')

    with open(os.path.join(base, 'gen.json')) as j:
        for nyhed in json.load(j, encoding='utf-8')[:(4 * 3)]:
            f.write(('''
<div class="nyhed">
  <h2 class="container">%s</h2>
  <hr>
  <h3 class="container">%s</h3>
  <h3 class="container date">%s</h3>
  <hr>
%s
</div>
''' % (nyhed['title'], nyhed['source'], nyhed['date'], shorten(nyhed['html']))).encode('utf-8'))
    
    f.write('''    </div>
  </body>
</html>
''')
