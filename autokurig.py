#! /usr/bin/python3
import flask
from flask import request, Response
from flask_cors import CORS, cross_origin
import requests, json
import urllib3
import re
import pdb
import optparse
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
SSL_VERIFY = False

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Set up the command-line options
# default_host = "https://titan.wal-mart.com:443"
default_host = "https://oser502444.homeoffice.wal-mart.com:8080"
default_key = "a4545186-441a-45d6-9518-ab3de59e4c86"
default_test = "prod"
parser = optparse.OptionParser()
parser.add_option("-H", "--host",
    help="Hostname of the Flask app " + \
        "[default %s]" % default_host,
    default=default_host)
parser.add_option("-K", "--key",
    help="Key used to authenticate to titan " + \
        "[default %s]" % default_key,
    default=default_key)
parser.add_option("-T", "--test",
    help="Test=<type of test>" + \
        "[default %s]" % default_test,
    default=default_test)

options, _ = parser.parse_args()


def send_request(url="", requestType="GET", payload="", titanPayload=None):
    ''' function will send RESTFUL requests to Mist's API'''
    try:
        http_proxy  = "sysproxy.wal-mart.com:8080"
        https_proxy = "sysproxy.wal-mart.com:8080"

        proxyDict = { 
                    "http"  : http_proxy, 
                    "https" : https_proxy
                    }

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
    return "You have reached the Mist Cutover API."

# Check if site exists
@app.route('/api/v1/exist/<siteNumber>', methods=['GET'])
def check(siteNumber):
    ''' Route will validate if a site exists '''
## if there are ever any sites that have the same name then only the first match will return
## need to handle that
    for org in orgList:

        url = "https://api.mist.com/api/v1/orgs/"+ org +"/sites"

        responseData = send_request(url) #4754 8209 0001

        for item in responseData:
            if siteNumber != item['name']:
                continue
            else:
                return Response(json.dumps({"Success":True}), mimetype='application/json')

    return Response(json.dumps({"Success":False}), mimetype='application/json')


try:
    import RPi.GPIO as GPIO
    import time
    
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


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
