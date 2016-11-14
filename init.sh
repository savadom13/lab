#!/bin/bash

if [ -h /etc/nginx/sites-enabled/default ] 
then
    rm -f /etc/nginx/sites-enabled/default
    echo "delete default conf"
fi


if [ ! -h /etc/nginx/sites-enabled/myconf ] 
then
    ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/myconf
    echo "enable myconf for nginx"
fi

sudo mkdir /etc/gunicorn.d/
sudo ln -s /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.conf
echo "gunicorn conf copy"

sudo service gunicorn restart
echo "nginx restart"

sudo service nginx restart 
echo "nginx restart"
