import requests
import json

# دریافت قیمت لحظه‌ای BNB از Binance
def get_bnb_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

# به‌روزرسانی فایل JSON در GitHub
def update_price_file():
    price = get_bnb_price()
    
    # داده جدید
    new_data = {
        "symbol": "BNB",
        "price": str(price),
        "currency": "USD",
        "last_updated": "2025-03-13T12:00:00Z"
    }

    # ذخیره در فایل JSON
    with open("price.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)

    print(f"Price updated: {price} USD")

# اجرای تابع
update_price_file()
