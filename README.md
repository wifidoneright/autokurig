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

#### Install mod_wsgi
for python 3.6 (preferable)
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```

## download to your PI

``` 
cd ~
git clone https://github.com/eventuallyiwin/autokurig.git
 ```

### move .conf file to the active sites directory
``` sudo mv /home/pi/autokurig/autokurig.conf /etc/apache2/sites-available/autokurig.conf
```
### activate site
```sudo a2ensite /etc/apache2/sites-available/autokurig.conf```

### Restart your Apache service
```
apache2 -f /etc/apache2/apache2.conf -k stop
apache2 -f /etc/apache2/apache2.conf -k start
```

# Referenced pages
https://www.codementor.io/abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft