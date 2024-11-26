from flask import Flask, jsonify, request
import datetime
from flask_cors import CORS
import random
from datetime import datetime
app = Flask(__name__)
CORS(app)

def fake_generator(date):
    now = datetime.now()
    return_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    # 定义特定日期
    if date == "2412":
        target_date = datetime(2024, 12, 20)
    elif date == "2501":
        target_date = datetime(2025, 1, 17)
    elif date == "2503":
        target_date = datetime(2025, 3, 21)
    elif date == "2506":
        target_date = datetime(2025, 6, 20)
    else:
        print("Invalid Contract date")
        return {}

    # 获取当前日期
    current_date = datetime.now()

    # 计算日期差
    date_difference = target_date - current_date

    # 输出天数差
    days_difference = date_difference.days
    contracts_data = {
        f"IH_{date}":{
            "buy_value":random.randint(2500,2700),
            "sell_value":random.randint(2500,2700)
        },
        f"IF_{date}":{
            "buy_value":random.randint(3900,4100),
            "sell_value":random.randint(3900,4100),
        },
        f"IC_{date}": {
            "buy_value":random.randint(5900,6100),
            "sell_value":random.randint(5900,6100),
        },
        f"IM_{date}": {
            "buy_value":random.randint(6000,6200),
            "sell_value":random.randint(6000,6200),
        }
    }
    
    
    res = {
        "data": contracts_data,
        "time": return_time,
        "expired": days_difference
    }
    return res
@app.route("/get-etf-data")
def etf_data_generator():
    # response data 
    etf_data={
        "sh016_value": random.randint(2500,2700),
        "sh300_value": random.randint(3900,4100),
        "sh905_value": random.randint(5900,6100),
        "sh852_value": random.randint(6000,6200)
    }
    now = datetime.now()
    return_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return jsonify({
        'data':etf_data,
        'response_time': return_time
        })

@app.route("/get-contracts-data")
def get_contracts_data():
    list_param = request.args.get('list')
    contracts = list_param.split(",")
    response_origin_raw = {}
    for each in contracts:
        response_origin_raw[each] = fake_generator(each)

    # print(response_origin_raw)
    # print("\n")
    return jsonify(response_origin_raw)

if __name__ == "__main__":
    app.run(host="localhost",debug=True)