# note.comのハッシュタグデータ取得
import re
import pandas as pd
import sys
sys.path.append("lib.bs4")
import openpyxl
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutExcept

# ハッシュタグページを取得する関数
def get_hashtag_page():
  
   export_list = []

   # driverのセットアップ
   options = webdriver.ChromeOptions()
   options.add_argument('--headless')
   driver = webdriver.Chrome(options=options)
   driver.implicitly_wait(30)

   # データの取得
   url="https://note.com/hashtag?page=1"
   driver.get(url)

   # ページがロードされ切るまで待機
   WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

   # ハッシュタグのデータを含むタグを取得
   html = driver.page_source.encode('utf-8')
   soup = BeautifulSoup(html, "lxml")

   divs = soup.find_all("div",class_="p-tags__item")

   for div in divs:
       index1 = div.find(class_="p-tags__link").text.rfind("(")
       hashtag_name = div.find(class_="p-tags__link").text[0:index1]

       hashtag_count = div.find(class_="p-tags__count").text[1:-1]
       hashtag_count = int(re.sub("\\D", "", hashtag_count))

       temp=[]
       temp.append(hashtag_name)
       temp.append(hashtag_count)

       export_list.append(temp)

   # 仮想ブラウザを閉じる
   driver.close()
   driver.quit()

   # エクセルファイルに保存
   df = pd.DataFrame(export_list, columns=["hashtag_name","hashtag_cnt"])
   df.to_excel("ノート人気ハッシュタグ.xlsx")
          
get_hashtag_page()
print("ok")