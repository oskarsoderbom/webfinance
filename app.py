from flask import Flask, render_template, request
from OptionFunctions import EuropeanCall, EuropeanPut

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/options', methods=['POST'])
def options():
    option_type = request.form['option_type']
    if option_type == 'call':
        price = float(request.form['asset_price'])
        volatility = float(request.form['asset_volatility'])
        strike = float(request.form['strike_price'])
        time = float(request.form['time_to_expiration'])
        rate = float(request.form['risk_free_rate'])
        option = EuropeanCall(asset_price=price,
                              asset_volatility=volatility,
                              strike_price=strike,
                              time_to_expiration=time,
                              risk_free_rate=rate)
    elif option_type == 'put':
        price = float(request.form['asset_price'])
        volatility = float(request.form['asset_volatility'])
        strike = float(request.form['strike_price'])
        time = float(request.form['time_to_expiration'])
        rate = float(request.form['risk_free_rate'])
        option = EuropeanPut(asset_price=price,
                             asset_volatility=volatility,
                             strike_price=strike,
                             time_to_expiration=time, 
                             risk_free_rate=rate)

    return render_template('results.html', option=option)


if __name__ == '__main__':
    app.run()
