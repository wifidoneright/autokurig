#!/bin/bash

APPNAME="autokurig"
echo $APPNAME
APPDIR="/home/pi/$APPNAME"

cd $APPDIR
sudo git pull
sudo cp $APPDIR/$APPNAME.conf /etc/apache2/sites-available/$APPNAME.conf
echo "copied $APPNAME.conf to /etc/apache2/sites-available/$APPNAME.conf"
echo "you must now run 'sudo service apache2 restart'"
# sudo a2ensite /etc/apache2/sites-available/$APPNAME.conf