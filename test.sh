#!/bin/bash

echo ------------------------------------------------------------
echo curl localhost/
curl localhost/

echo ------------------------------------------------------------
echo curl localhost/uploads/test.jpg
curl localhost/uploads/test.jpg

echo ------------------------------------------------------------
echo curl localhost/css/test.css
curl localhost/css/test.css

echo ------------------------------------------------------------
echo curl localhost/img/test.png
curl localhost/img/test.png

echo ------------------------------------------------------------
echo curl localhost/js/test.js
curl localhost/js/test.js

echo ------------------------------------------------------------
echo curl localhost/123
curl localhost/123

echo ------------------------------------------------------------
cat /home/box/web/test.error.log