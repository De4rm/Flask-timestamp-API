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
	print(data_splited[1][0:len(data_splited[1])-1])
	
	if (len(data_splited) > 1):
		month = data_splited[0]
		day = data_splited[1][0:len(data_splited[1])-1]
		year = data_splited[2]
		if (month in months) and (int(day) in range(1,32)):
			year_len = len(year)
			if year_len < 4:
				addition_to_year = ["","0","00","000"]
				year = addition_to_year[4-year_len] + year
			elif year_len > 4:
				year = year[0:4]

			print(year)
			s = [day, str(months.index(month)+1), year]
			s = '/'.join(s)
			date_stamp = int(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple()))
			date_string = " ".join([month, data_splited[1], str(int(year))])
	else:
		try:
			int_data = int(data)
			date_string = datetime.fromtimestamp(int_data).strftime('%Y-%m-%d')
			date_string = date_string.split("-")
			date_string = ' '.join([months[int(date_string[1])-1], date_string[2] + ",", date_string[0]])
			date_stamp = int_data
		except:
			pass

	return jsonify({ "unix": date_stamp, "natural": date_string })


