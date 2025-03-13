import requests
import json

# دریافت قیمت لحظه‌ای BNB از CoinGecko
def get_bnb_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return float(data["binancecoin"]["usd"])  # مسیر درست برای دریافت قیمت

# به‌روزرسانی فایل JSON در GitHub
def update_price_file():
    price = get_bnb_price()
    
    new_data = {
        "symbol": "BNB",
        "price": str(price),
        "currency": "USD",
        "last_updated": "2025-03-13T12:00:00Z"
    }

    with open("price.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)

    print(f"Price updated: {price} USD")

# اجرای تابع
update_price_file()
