import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\user\\forecast.pkl', 'rb'))

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/forecast', methods=['POST'])
def forecast():
    # if request.method == "GET":
    #     return jsonify({"response": "Get Request Called"})
    if request.method == "POST":
        req_Json = request.json
        forecasts = req_Json['forecasts']
        print(forecasts)
        prediction = model.predict(np.array(forecasts).tolist()).tolist()
        return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, port=9090)
