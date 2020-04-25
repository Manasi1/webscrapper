from flask import Flask
from flask import render_template
from flask import request
from flask import Response
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

# recipr search API returns the recipe for keyword
@app.route('/storeData/', methods = ['POST'])
def storeData():

	data = request.json
	str1 = data['0'].replace(',', '')
	str1 = str1[1:]
	str2 = data['1'].replace(',', '')
	str2 = str2[1:]
	str3= data['2'].replace(',', '')
	str3= str3[1:]
	
	conn = None
	cursor = None
	try:
		conn = mysql.connector.connect(host='localhost',database='healthcamp',user='manasi',password='yL06hbxRY4NjkcYx',port='3306')
		cursor = conn.cursor()
		sql = "INSERT INTO healthcamp.webcrapper (confirmed, death, recovered) VALUES (%s, %s,%s)"
		val = (str1, str2,str3)
		cursor.execute(sql, val)
		conn.commit()
	except:
		print("Connection Failed!")
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

# App run, debug mode true to avoid rerunning after changes
app.run(debug=True)
