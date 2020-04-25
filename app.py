from flask import Flask
from flask import render_template
from flask import request
import requests
import json
import xmltodict
from zeep import Client
import datetime
import mysql.connector
import pandas as pd

app = Flask(__name__, template_folder='template', static_folder='static')

# index element
@app.route('/')
def hello_world():
	return render_template('index.html')

def sqlconnect():
	conn = None
	cursor = None
	try:
		conn = mysql.connector.connect(host='localhost',database='healthcamp',user='manasi',password='yL06hbxRY4NjkcYx')
		cursor = conn.cursor()
		return conn
	except:
		print("Connection Failed!")


# recipr search API returns the recipe for keyword
@app.route('/storeData/', methods = ['POST'])
def storeData():
	print("received")
	#print(requests.request)
	data = request.json
	print(data)
	conn = sqlconnect()
	yelp = pd.read_sql('INSERT INTO webcrapper (confirmed, death, recovered) VALUES (' + data['0']+ ',' + data['1']+','+ data['2']+')' , con=conn)

	resp = Response(js, status=200, mimetype='application/json')

	return resp

# App run, debug mode true to avoid rerunning after changes
app.run(debug=True)
