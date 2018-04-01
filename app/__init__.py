import time
import json
from datetime import datetime
from flask import Flask, jsonify


app = Flask(__name__)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomber", "November", "December"]

@app.route('/<string:data>', methods=['GET'])
def index(data):
	data_splited = data.split(' ')
	date_stamp = None
	date_string = None
	
	if len(data_splited) > 1 and data_splited[0] in months and int(data_splited[1][0:2]) in range(1,32) and len(data_splited[2]) == 4:
		s = [data_splited[1][0:2], str(months.index(data_splited[0])+1), data_splited[2]]
		s = '/'.join(s)
		date_stamp = str(int(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())))
		date_string = data
	else:
		try:
			date_string = datetime.fromtimestamp(int(data)).strftime('%Y-%m-%d')
			print("entry 2")
			date_string = date_string.split("-")
			date_string = ' '.join([months[int(date_string[1])-1], date_string[2] + ",", date_string[0]])
			date_stamp = data
		except:
			pass

	return jsonify({ "unix": date_stamp, "natural": date_string })


