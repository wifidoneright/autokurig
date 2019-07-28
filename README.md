# autokurig
automate my kurig
this project assumes the following
1. you have raspian installed on your raspberry pi nano
# installing requirements
```python -m pip3 install -r requirements.txt```
# linux install pip
```sudo apt install python3-pip```
## Install requirements
``` sudo pip3 install -r requirements.txt```
#### Install Apache
```
sudo apt update
sudo apt install apache2
```
#### Allow user "pi" to run GPIO input/output
```sudo rpi-update```
```sudo adduser pi gpio```

#### Install mod_wsgi
for python 3
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```

## download to your PI
everything is set up to run from the user pi home directory
``` 
cd /home/pi/
git clone https://github.com/eventuallyiwin/autokurig.git
 ```
now run deploy.bash
``` /my/path/deploy.bash ```

## OR you can run the following commands
### move .conf file to the active sites directory
``` sudo mv /home/pi/autokurig/autokurig.conf /etc/apache2/sites-available/autokurig.conf ```
#### restart the apache service
``` sudo service apache2 restart ```
### activate site (do once)
```sudo a2ensite /etc/apache2/sites-available/autokurig.conf```

### Restart your Apache service
```
apache2 -f /etc/apache2/apache2.conf -k stop
apache2 -f /etc/apache2/apache2.conf -k start
```

# Referenced pages
https://www.codementor.io/abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft

https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root

```sudo rpi-update```
```sudo adduser pi gpio```
