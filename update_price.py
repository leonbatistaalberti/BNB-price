import requests

def get_bnb_price():
    response = requests.get("URL_API_HERE")  # آدرس API را جایگزین کن
    data = response.json()

    # چاپ خروجی کامل API برای بررسی
    print("🔍 API Response:", data)  # نمایش خروجی API
    
    # بررسی می‌کنیم که آیا 'price' در پاسخ وجود دارد یا نه
    if "price" in data:
        return float(data["price"])
    else:
        raise ValueError("❌ قیمت در داده‌های API وجود ندارد!")

# تست تابع
if __name__ == "__main__":
    try:
        price = get_bnb_price()
        print(f"🔑 قیمت BNB: {price}")
    except ValueError as e:
        print(e)
