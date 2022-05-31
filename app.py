from flask.globals import request
from flask import Flask, request
from flask_cors import CORS
import numpy as np
import csv
from numpy import genfromtxt
import io
from PIL import Image
import pandas as pd
from services import *


#region config
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['CORS_EXPOSE_HEADERS'] = ['x-min-api-ver', 'content-type', 'authorization']
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024



@app.route("/", methods=["GET"])
def healthCheck(): 
    return 'Welcome'

@app.route("/resize-image", methods=["GET"])
def resizeImg():
    return resizeImage('img[1][1].csv')

@app.route("/image-frames", methods=["GET"])
def getImageFrames(): 
    depthMin =  float(request.args.get('min_depth'))
    depthMax =  float(request.args.get('max_depth'))

    return getFrames(depthMin, depthMax)


@app.route("/top-plants", methods=["GET"])
def topPlantsByANG():
    n = request.args.get('number')
    return topPlants(int(n))


@app.route("/filter-by-state", methods=["GET"])
def filterState():
    state = request.args.get('state')
    return filterByState(state)


@app.route("/net-by-state", methods=["GET"])
def netByState():
    return netGenerationByState()