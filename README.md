# Zalora Product Scraper
Script ini digunakan untuk mengambil data produk dari endpoint publik Zalora:

Contoh penggunaannya ada pada file Python di repo ini.

## Contoh Respons API (potongan)

```json
{
  "ConfigSku": "12949SH3F8B93AGS",
  "Name": "Downshifter 12 Men's Road Running Shoes",
  "Price": "Rp 819.000",
  "SpecialPrice": "",
  "Brand": "Nike",
  "ImageList": ["...", "..."],
  "MainImageUrl": "...",
  "Breadcrumbs": ["Sports","Pria","Sepatu Running"],
  "MarkdownLabel": "",
  "SpecialLabel": "trending",
  "SupplierName": "ZALORA",
  "ReviewStatistics": {
    "AvgRating": 4.9,
    "ReviewCount": 26
  },
  "ProductUrl": "p/nike-downshifter-12-men-s-road-running-shoes-grey-3837262"
}
Penjelasan Parameter Utama
Parameter	Keterangan
ConfigSku	SKU unik produk di Zalora
Name	Nama produk
Brand	Merek produk
Price	Harga normal dalam string
SpecialPrice	Harga promo (jika ada)
PriceInDecimal	Harga normal dalam angka
SpecialPriceInDecimal	Harga promo dalam angka
ImageList	Daftar URL gambar produk
MainImageUrl	URL gambar utama produk
Breadcrumbs	Hirarki kategori produk
MarkdownLabel	Label diskon/promosi (bila ada)
SpecialLabel	Label khusus seperti “trending”
SupplierName	Nama penjual/supplier (misalnya “ZALORA”)
ReviewStatistics.AvgRating	Rata-rata rating produk
ReviewStatistics.ReviewCount	Jumlah ulasan yang diterima produk
ProductUrl	Path URL produk (gabungkan dengan https://www.zalora.co.id/)
