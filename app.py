from flask import Flask, jsonify
from services.yahoo_service import get_stock_data
from services.currency_service import get_currency_data

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API Financeira ativa!"})

@app.route('/api/stock/<ticker>', methods=['GET'])
def stock(ticker):
    data = get_stock_data(ticker)
    return jsonify(data)

@app.route('/api/currency/<pair>', methods=['GET'])
def currency(pair):
    data = get_currency_data(pair)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
