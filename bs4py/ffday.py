import requests
from bs4 import BeautifulSoup

home = "http://www.f-2.com.tw"
# 設定活動主頁面
ff = home + "/index.php?q=category/%E6%B4%BB%E5%8B%95/ff"
ffget = requests.get(ff)
# 尋找ff活動
ffsoup = BeautifulSoup(ffget.text,"html.parser")
ffsel =  ffsoup.select("h2.title a")
fflist = []
for s in ffsel:
	if("攤位編號" in s.text):
	# 將ff活動頁中包含攤位編號的連結丟出來並設定
		ffdaylist = []
		ffdaylist.append(s.text)
		ffday = home + s["href"]
		ffdayget = requests.get(ffday)
		# 尋找當日攤位
		ffdaysoup = BeautifulSoup(ffdayget.text,"html.parser")
		ffdaysel = ffdaysoup.select("table.tableizer-table tbody tr")
		for n in ffdaysel:
			p = n.text.split("\n")
			# tr,td 分割
			if("," in p[1]):
				x = p[1].split(",")
				for xx in x:
					ffdaylist.append([xx,p[2]])
			# 連攤分割
			else:
				ffdaylist.append([p[1],p[2]])
		fflist.append(ffdaylist)
		# 攤位資訊丟出來
print(fflist)