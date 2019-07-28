APPNAME = "autokurig"
APPDIR = "/home/pi/" + APPNAME
cd APPDIR
git pull
sudo mv /home/pi/autokurig/autokurig.conf /etc/apache2/sites-available/autokurig.conf
sudo service apache2 restart
# sudo a2ensite /etc/apache2/sites-available/autokurig.conf