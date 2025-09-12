import requests
import json

url = "https://api.zalora.co.id/v1/dynproducts/datajet/list?"

params = {
      
    "anonymous_id": "cbdf4d41-33d5-43c5-8a54-0220a3a460ef",
    "enableRelevanceClassifier": "true",
    "fullFacetCategory": "true",
    "limit": "200",
    "offset": "0",
    "query": "sepatu running pria",  # bisa langsung spasi
    "shop": "m"
}
payload = {}
headers = {
    "Accept": "application/json",  # minta json
    "User-Agent": "Mozilla/5.0",   # header mirip browser
    'Cookie': '_cdn=cf'
}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


resp = requests.get(url, headers=headers, data=payload, params=params)
# data = resp.json()
# print(data.keys())

print(resp.status_code)  # cek kode status
print(resp.headers.get('Content-Type'))  # cek tipe konten
print(resp.text)  # cek 500 karakter pertama
data = resp.json()
products = data['data']['Products']

records = []
for p in products:
    records.append({
        "sku": p["ConfigSku"],
        "name": p["Name"],
        "brand": p["Brand"],
        "price": p["Price"],
        "special_price": p["SpecialPrice"],
        "url": "https://www.zalora.co.id/" + p["ProductUrl"],
        "image": p["MainImageUrl"],
        "discount": p["MarkdownLabel"]
    })


# tampilkan hasil
for p in products:
    print(p)

# atau simpan ke file json
with open("zalora_sepatu.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
