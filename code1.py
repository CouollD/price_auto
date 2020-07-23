#coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ブラウザのオプションを格納する変数
options = Options()

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

# idがheikinの要素を表示
# 金
# print(soup.select(".au_scrap .col"))
print(soup.select(".au_scrap .col td"))
print("\n")
# プラチナ
print(soup.select(".pt_scrap .col"))

print("\n")
# 銀
print(soup.select(".ag_scrap td"))
# print(soup.find_all(".au_scrap .col td"))