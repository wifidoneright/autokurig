#! /usr/bin/python3

try:
    from autokurig import app
    from flask import render_template, request, Response
    # from flask_cors import CORS, cross_origin
    import requests, json
    # import urllib3
    # import re
    # import pdb
    # import optparse
    # from datetime import datetime
    # from requests.packages.urllib3.exceptions import InsecureRequestWarning
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # SSL_VERIFY = False
    import RPi.GPIO as GPIO
    import time
    
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


app.config["DEBUG"] = True
# Set up the command-line options
# default_host = ""
authToken = ""

def send_request(url="", requestType="GET", payload=""):
    try:

        print("Payload=",payload)

        headers = {
        'Authorization': "Token " + authToken,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

        response = requests.request(requestType, url, headers=headers,
                                    verify=False, data=payload)

        print("#### RESPONSE  #####")

        if response.status_code != 200:
            print("HTTP CODE: {} ERROR RESPONSE: {}".format(response.status_code, response.text))
        else:
            print("HTTP CODE: {} SUCCESS RESPONSE: {}".format(response.status_code, response.text))
            data = json.loads(response.text)

            return data

        if response.status_code in range(400, 599):
            print("HTTP CODE: {} ERROR RESPONSE: {}".format(
            response.status_code, response.text))
            data = json.loads(response.text)

            return data

        data = json.loads(response.text)
        return data
    ## add logging in the whole thing

    except Exception as e:
        print("ya done broke it")
        raise e
        
        
# @cross_origin(supports_credentials=True)  ##CORS
#index or default API page
@app.route('/', methods=['GET'])
def home():
    templateData = { 'title' : 'AUTOKURIG'}
    return render_template('index.html', **templateData)


# Check if site exists
@app.route('/api/brew/<size>', methods=['GET'])
def make(size):
    ''' Route will brew a coffee based on 
    the size given (small, medium, large)'''
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    mode = GPIO.getmode()
    pwrButton = 11
    lidSensor = 15
    brewLarge = 29
    brewMed = 33
    brewSmall = 36

    if size == "small":
        brew = brewSmall
    if size == "medium":
        brew = brewMed
    if size == "large":
        brew = brewLarge
    
    
    # Setup Pins
    try:
        print("activating pins")
        GPIO.setup(pwrButton, GPIO.OUT,initial=1)
        GPIO.setup(lidSensor, GPIO.OUT,initial=1)
        GPIO.setup(brewLarge, GPIO.OUT,initial=1)
        GPIO.setup(brewMed, GPIO.OUT,initial=1)
        GPIO.setup(brewSmall, GPIO.OUT,initial=1)
    except Exception as e:
        return Response(e)

    #power on
    GPIO.output(pwrButton,0) 
    time.sleep(1)
    GPIO.output(pwrButton,1)

    time.sleep(5)

    #trip the lid sensor
    GPIO.output(lidSensor,0) 
    time.sleep(1)
    GPIO.output(lidSensor,1)

    time.sleep(5)
    
    #Cup Size
    GPIO.output(brew,0) 
    time.sleep(1)
    GPIO.output(brew,1)

    time.sleep(50)

     #power off
    GPIO.output(pwrButton,0) 
    time.sleep(1)
    GPIO.output(pwrButton,1)


    GPIO.cleanup()
    return Response(json.dumps({"Brew":"Success"}), mimetype='application/json')

    
if __name__ == "__main__":
    app.run(debug=True,port=80, host='0.0.0.0')
