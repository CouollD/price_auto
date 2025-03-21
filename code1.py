#coding: UTF-8
# スクレイピング結果をパースするライブラリ
from bs4 import BeautifulSoup
# 動的なページを読み込むためのライブラリ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import peewee

#ブラウザのオプションを格納する変数
options = Options()

# 出力結果を格納する辞書ファイル
data= {}

# Headlessモードを有効にする(コメントアウトするとブラウザが立ち上がる)
options.set_headless(True)

# ブラウザを起動
driver = webdriver.Chrome(chrome_options=options)

# ブラウザでアクセス
driver.get("https://www.net-japan.co.jp/precious_metal/print.html")

# HTMLコードを文字コードUTF-8に変換してから取得
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようパース
soup = BeautifulSoup(html, "html.parser")

# 金、プラチナ、銀、パラジウムアイテム名を取得
items = soup.select("dl dt")
# htmlデータからテキスト部分だけ抽出
items = list(map(lambda item:item.text, items))
print(items)

# 金、プラチナ、銀、パラジウムの公開価格を取得
prices = soup.select("dl dd")
# htmlデータからテキスト部分だけ抽出
prices = list(map(lambda price:price.text, prices))
# 偶数版目の前日比データを除く
prices = prices[0::2]

# 後半は販売価格なので表示しない。
for i in range(4):
    data[items[i]] = prices[i]
print(data)

# idがheikinの要素を表示
# 金
# au = []
# au_prices = soup.select(".au_scrap .col td")
# for au_price in au_prices:
#     price = au_price.text
#     print(au_price)

# print("\n")

# プラチナ
# pt_prices = soup.select(".pt_scrap .col")

# for pt_price in pt_prices:
#     price = pt_price.text
#     print(price)

# print("\n")

# # 銀
# print(soup.select(".ag_scrap"))
# print(soup.find_all(".au_scrap .col td"))

# 辞書ファイルをjsonに整形
market_price = json.dumps(data)
print(market_price)
# 値だけ取り出したい
# print(soup.find_all(class_="ag_scrap"))

