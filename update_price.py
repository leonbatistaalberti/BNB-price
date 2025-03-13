import requests
import json
from datetime import datetime

# دریافت قیمت لحظه‌ای BNB از CoinGecko
def get_bnb_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # بررسی اینکه پاسخ صحیح است یا نه
    if "binancecoin" in data and "usd" in data["binancecoin"]:
        return float(data["binancecoin"]["usd"])
    else:
        raise ValueError("Failed to fetch price from CoinGecko API")

# به‌روزرسانی فایل price.json
def update_price_file():
    price = get_bnb_price()

    # داده جدید
    new_data = {
        "symbol": "BNB",
        "price": str(price),
        "currency": "USD",
        "last_updated": datetime.utcnow().isoformat() + "Z"
    }

    # ذخیره در فایل JSON
    with open("price.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)

    print(f"✅ قیمت به‌روزرسانی شد: {price} USD")

# اجرای تابع
update_price_file()
