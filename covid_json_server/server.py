import os, json, csv
from flask import Flask
from flask_cors import CORS,cross_origin


from covid_data import CovidData

curr_path = os.path.dirname(os.path.abspath(__file__))
filename = "data.csv"
data_path = f"{curr_path}/{filename}"

data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

dt = None

def downloadUrl(url, path):
	os.system(f"wget -q {url} -O {data_path}")

# downloadUrl(data_url, data_path)
dt = CovidData(data_path)
jsdt = json.dumps(dt.getDict())

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route("/", methods=["GET"])
@cross_origin(supports_credentials=True)
def data():
    return jsdt