from flask import Flask, render_template, request, redirect
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

        option_price = option.price
        delta = option.delta
        gamma = option.gamma
        vega = option.vega

        return redirect(f"/results?option_price={option_price}&delta={delta}&gamma={gamma}&vega={vega}")
        
    return render_template('results.html', option=option)


@app.route('/results')
def results():
    option_price = request.args.get('option_price')
    delta = request.args.get('delta')
    gamma = request.args.get('gamma')
    vega = request.args.get('vega')

    if not option_price or not delta or not gamma or not vega:
        return redirect('/')

    return render_template('results.html', option_price=option_price, delta=delta, gamma=gamma, vega=vega)


if __name__ == '__main__':
    app.run()
