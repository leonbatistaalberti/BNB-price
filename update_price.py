import requests
import json

# دریافت قیمت لحظه‌ای BNB از CoinGecko
def get_bnb_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # چاپ داده دریافتی برای اشکال‌زدایی
    print("API Response:", data)

    # بررسی اینکه آیا کلیدهای مورد نیاز در پاسخ هستند یا نه
    if "binancecoin" in data and "usd" in data["binancecoin"]:
        return float(data["binancecoin"]["usd"])
    else:
        raise ValueError("Invalid response from API")

# به‌روزرسانی فایل JSON
def update_price_file():
    try:
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

    except Exception as e:
        print("Error:", e)

# اجرای تابع
update_price_file()
