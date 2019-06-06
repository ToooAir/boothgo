import requests
from bs4 import BeautifulSoup

home = "http://www.comicworld.com.tw/"
# 設定活動主頁面
cwt = home + "/Act4/89"
# 暫時只能先抓CWT51(89)出來用
cwtget = requests.get(cwt)
# 尋找cwt活動
cwtsoup = BeautifulSoup(cwtget.text,"html.parser")
cwtsel =  cwtsoup.select("ul.tab_box_nav a")
# 尋找表單的href
cwtlist = []
for s in cwtsel:
	if("社團名單" in s.text):
	# 將cwt活動頁中包含攤位編號的表單丟出來並設定
		cwtdaylist = []
		cwtdaylist.append(s.text)
		cwtdaysel = cwtsoup.select("div" + s['href'] + " table tr")
		# 尋找兩天的表格
		for n in cwtdaysel:
			td = n.find_all('td')
			if len(td) == 4:
				# 只取有四個欄位的
				name = td[0].text.replace('\r','').replace('\n','').replace('\t','')
				if("社團名稱" in name):
					continue
					# 把社團名稱那個濾掉
				booth = td[2].text.replace('\r','').replace('\n','').replace('\t','')
				# 無意義字元刪除
				if len(booth) > 3:
					cwtdaylist.append([booth[0:3],name])
					cwtdaylist.append([booth[3:6],name])
					# 連攤處理
				else:
					cwtdaylist.append([booth,name])
		cwtlist.append(cwtdaylist)
		# 攤位資訊丟出來
print(cwtlist)