#!/usr/bin/env python

import os
import sys
import json
import random

base = os.path.dirname(__file__)

sys.stdout.write('''<!doctype html>
<html>
  <head>
    <title>Studiebeskeder</title>
    <style type="text/css">
body {
  overflow: hidden;
  margin: 0;
  font-family: 'URW Palladio L';
}

.nyhed {
  width: 940px;
  height: 970px;
  float: left;
  margin: 5px;
  padding: 3px;
  overflow: hidden;
  border: 1px dotted silver;
  background-color: azure;
}

h1, h2, h3, p {
  margin: 0 0 5px 0;
}

h1.container {
  margin: 5px 0 0 0;
  font-size: 70px;
  font-family: Gentium;
  font-style: italic;
  color: red;
  text-align: center;
}
    
h2.container {
  margin: 0;
  font-size: 50px;
}

h3.container {
  margin: 0;
  font-size: 40px;
}

p {
  font-size: 24px;
}

h3 {
  font-size: 30px;
}

h2 {
  font-size: 36px;
}

h1 {
  font-size: 41px;
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
    nyheder = json.load(j, encoding='utf-8')[:10]
    random.shuffle(nyheder)
    for nyhed in nyheder[:2]:
        sys.stdout.write(('''
<div class="nyhed">
  <h2 class="container">%s</h2>
  <hr>
  <h3 class="container">%s</h3>
  <h3 class="container date">%s</h3>
  <hr>
%s
</div>
''' % (nyhed['title'], nyhed['source'], nyhed['date'], nyhed['html'])).encode('utf-8'))
    
sys.stdout.write('''    </div>
  </body>
</html>
''')
