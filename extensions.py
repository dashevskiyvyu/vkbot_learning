import requests
import json


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        base = base.lower()
        quote = quote.lower()

        currencies = {
            "евро": "EUR",
            "доллар": "USD",
            "рубль": "RUB"
        }

        if base == quote:
            raise APIException("Нельзя переводить одинаковые валюты.")

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")

        url = f"https://api.exchangerate-api.com/v4/latest/{base_ticker}"
        response = requests.get(url)

        data = json.loads(response.text)

        rate = data["rates"][quote_ticker]
        total = rate * amount

        return round(total, 2)