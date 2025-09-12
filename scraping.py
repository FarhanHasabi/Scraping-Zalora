import requests
import pandas as pd
import time

url = "https://api.zalora.co.id/v1/dynproducts/datajet/list"


base_params = {
    "query": "sepatu running pria",
    "shop": "m",
    "limit": 100,  
    "image_format": "webp",
    "image_quality": 70,
    "image_resize": "533.4x770",
    "enableRelevanceClassifier": "true",
    "fullFacetCategory": "true"
}
payload = {}
headers = {
    "Accept": "application/json",  
    "User-Agent": "Mozilla/5.0",   # header mirip browser
    'Cookie': '_cdn=cf'
}

all_records = []
total_needed = 500  
offset = 0

while len(all_records) < total_needed:
    params = base_params.copy()
    params["offset"] = offset

    resp = requests.get(url, headers=headers, data=payload,params=params)
    resp.raise_for_status()
    data = resp.json()
    

    products = data['data']['Products']
    if not products:
        break  # sudah habis produknya

    for p in products:
        # cek field tambahan jika ada
        review_stats = p.get("ReviewStatistics", {}) or {}

        all_records.append({
            "sku": p.get("ConfigSku"),
            "name": p.get("Name"),
            "brand": p.get("Brand"),
            "price": p.get("Price"),
            "special_price": p.get("SpecialPrice"),
            "url": "https://www.zalora.co.id/" + p.get("ProductUrl", ""),
            "image": p.get("MainImageUrl"),
            "discount": p.get("MarkdownLabel"),
            "seller_name": p.get("SupplierName"),
            "rating": review_stats.get("AvgRating"),
            "review_count": review_stats.get("ReviewCount")
        })

    offset += len(products)  # geser offset sesuai jumlah produk
    print(f"Fetched {len(all_records)} items so far")
    time.sleep(0.5)  # jaga-jaga jangan terlalu cepat hit API


all_records = all_records[:total_needed]

df = pd.DataFrame(all_records)
df.to_csv("zalora_500_products.csv", index=False)
print("Done:", len(df), "products saved.")