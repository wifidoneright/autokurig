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
# default_host = "https://titan.wal-mart.com:443"
authToken = ""

def send_request(url="", requestType="GET", payload="", titanPayload=None):
    ''' function will send RESTFUL requests to Mist's API'''
    try:

        print("Payload=",payload)

        headers = {
        'Authorization': "Token " + authToken,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

        response = requests.request(requestType, url, headers=headers,
                                    verify=False, proxies=proxyDict, data=payload)

        print("#### RESPONSE  #####")

        if response.status_code != 200:
            print("HTTP CODE: {} ERROR RESPONSE: {}".format(response.status_code, response.text))
            if titanPayload != None:
                for i in titanPayload:
                    # write error to titan item
                    # prov_stat_update(i['id'], "error", i['user'], "received error code " + str(response.status_code))
                    data = json.loads(response.text)
                # return json.loads(response.text)
                return data
            else:
                print("HTTP CODE: {} SUCCESS RESPONSE: {}".format(response.status_code, response.text))
                data = json.loads(response.text)

            return data

        if response.status_code in range(400, 599):
            print("HTTP CODE: {} ERROR RESPONSE: {}".format(
                response.status_code, response.text))
            if titanPayload != None:
                for i in titanPayload:
                    # write error to titan item
                    data = json.loads(response.text)
                return data
            else:
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
@app.route('/api/brew/<size>', methods=['POST'])
def make(size):
    ''' Route will brew a coffee '''

    # url = "https://api.mist.com/api/v1/orgs/"+ org +"/sites"

    # responseData = send_request(url) #4754 8209 0001

    # for item in responseData:
    #     if siteNumber != item['name']:
    #         continue
    #     else:
    #         return Response(json.dumps({"Success":True}), mimetype='application/json')

    return Response(json.dumps({"Brew":"Success"}), mimetype='application/json')

@app.route('/api/water', methods=['GET'])
def water():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    mode = GPIO.getmode()
    wLevel = 16
    # Setup Pins
    GPIO.setup(wLevel, GPIO.OUT)


    GPIO.output(wLevel,1) #set water to full

    # set channel
    # GPIO.setup(channel, GPIO.IN)
    # GPIO.setup(channel, GPIO.OUT)
    # GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
    # read channel
    # GPIO.input(channel)
    # GPIO.output(channel, state)
    # State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

    # GPIO.setup(wLevel, GPIO.OUT)
    # while True:
    #     GPIO.output(wLevel,1)
    #     time.sleep(1)
    #     GPIO.output(wLevel,0)
    #     time.sleep(1)


    GPIO.cleanup()
    return Response("water is now Full")

    
if __name__ == "__main__":
    app.run(debug=True,port=80, host='0.0.0.0')