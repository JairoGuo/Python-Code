import requests
from bs4 import BeautifulSoup
import re
import bs4
import json
import os


while(True):
	os.system('cls')
	print("天气查询系统")
	print("-"*50)
	w = input("请输入城市：")
	d = requests.get("http://open.weather.sina.com.cn/api/location/getSuggestion/"+w)
	d = d.text
	j = json.loads(d)
	if j['result']['data']['total'] == '0':
		os.system('pause')
		print("查询不到城市，请继续")
	else:
		break
	
weizhi = j['result']['data']['data'][0]['url']
url = "http://weather.sina.com.cn/" + weizhi
h = requests.get(url)
h.encoding = h.apparent_encoding
# print(h.status_code)
# print(r.raise_for_stats())
h = h.text # h.h.conten
soup = BeautifulSoup(h, "html.parser")

print("{}当前天气".format(soup.body.find('h4','slider_ct_name').string))
print("-"*50)
print("当前温度:{} ".format(soup.body.find('div','slider_degree').string),end="")
print(soup.body.find('p','slider_detail').string.replace(' ',''))

for a in soup.body.find('p','wt_fc_c0_i_times').children:
    if isinstance(a,bs4.element.Tag):
        print("{}:".format(a.string),sep='/',end='')
    


print(soup.body.find('p','wt_fc_c0_i_temp').string)
print("风向:{} ".format(soup.body.find('p','wt_fc_c0_i_tip').string))
print('污染指数: {}'.format(soup.body.find('li','l').string),end='')
print(" [{}]".format(soup.body.find('li','r').string),end='')
print("\n")

print("{}未来10天天气".format(soup.body.find('h4','slider_ct_name').string))
for a in soup.body.find('div','blk_fc_c0_scroll').children:
	if isinstance(a,bs4.element.Tag):	
		print(a.find("p","wt_fc_c0_i_date").string)
		print(a.find("p","wt_fc_c0_i_day").string)
		k = a('span')
		for i in k:
			print(i.string,end=" ")
		print("")
		print(a.find("p","wt_fc_c0_i_temp").string)
		print("风向:{} ".format(a.find('p','wt_fc_c0_i_tip').string))
		try:
			print('污染指数: {}'.format(a.find('li','l').string),end='')
			print(" [{}]".format(a.find('li','r').string),end='')
		except  AttributeError:
			print("污染指数: [暂未结果]")
	print("")



#"data":{"total":"0"}}
#"data":{"data":[{"loc_code":"43-48-30-39-30-33-30-35","name":"","type":"1","url":"guyuan","chinese_name":"\u6cbd\u6e90","parent_name":"\u6cb3\u5317"}],"total":"1"}}}