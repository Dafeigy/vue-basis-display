from flask import Flask, jsonify, request
import datetime
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/get-etf-data")
def etf_data_generator():
    # response data 
    etf_data={
        "sh016_value": random.randint(2500,2700),
        "sh300_value": random.randint(3900,4100),
        "sh905_value": random.randint(5900,6100),
        "sh852_value": random.randint(6000,6200)
    }
    now = datetime.datetime.now()
    return_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return jsonify({
        'data':etf_data,
        'response_time': return_time
        })

@app.route("/get-contracts-data")
def get_contracts_data():
    list_param = request.args.get('list')
    return jsonify(list_param)

if __name__ == "__main__":
    app.run(host="localhost")