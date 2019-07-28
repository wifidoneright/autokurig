from flask import Flask, render_template, request, Response
app = Flask(__name__)

import autokurig.views