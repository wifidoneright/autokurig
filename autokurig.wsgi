#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/autokurig/')
import autokurig as application
# from autokurig import autokurig as application
application.secret_key = 'anything you wish'