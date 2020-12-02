from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location')
def get_location():
    response = jsonify({
        'locations': util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/house_prediction', methods=['POST'])
def house_prediction():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'predicted_price': util.get_prices(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print('Start python flask server')
    util.load_saved_data()
    app.run()
