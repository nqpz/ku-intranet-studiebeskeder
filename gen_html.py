#!/usr/bin/env python

import os
import sys
import json
import random


sys.stdout.write('''<!doctype html>
<html>
  <head>
    <title>Studiebeskeder</title>
    <style type="text/css">
body {
  margin: 0;
  font-family: 'URW Palladio L';
}

.nyhed {
  width: 620px;
  height: 490px;
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

p {
  25px;
}

h3 {
  26px;
}

h2 {
  28px;
}

h1 {
  30px;
}

h1.container {
  margin: 5px 0 0 0;
  font-size: 50px;
  font-family: Gentium;
  font-style: italic;
  color: red;
  text-align: center;
}
    
h2.container {
  margin: 0;
  font-size: 40px;
}

h3.container {
  margin: 0;
  font-size: 30px;
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
    nyheder = json.load(j, encoding='utf-8')
    random.shuffle(nyheder)
    for nyhed in nyheder[:(3 * 2)]:
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
