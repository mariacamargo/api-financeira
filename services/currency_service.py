import requests

def get_currency_data(pair="USD-BRL"):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{pair}"
        response = requests.get(url)
        data = response.json()

        if not data:
            return {"error": "Par de moedas inválido."}

        key = list(data.keys())[0]
        quote = data[key]

        return {
            "pair": pair,
            "name": f"{quote['name']}",
            "bid": quote['bid'],
            "ask": quote['ask'],
            "variation": quote['pctChange'],
            "updated_at": quote['create_date']
        }
    except Exception as e:
        return {"error": str(e)}
