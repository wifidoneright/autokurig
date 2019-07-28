#!/bin/bash

APPNAME = autokurig
APPDIR = /home/pi/$APPNAME
cd $APPDIR
git pull
sudo mv $APPDIR/$APPNAME.conf /etc/apache2/sites-available/$APPNAME.conf
sudo service apache2 restart
# sudo a2ensite /etc/apache2/sites-available/$APPNAME.conf