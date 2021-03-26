# COVID-19 한국 일일 확진자 표

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

nums = []
circles = []
dates = []
before_list = []
today_list = []

for item in soup.select("div.liveNum_today_new"):
    for data in item.select("span.data"):
        today_list.append(data.string)

for item in soup.select("div.chart_d"):
    for data in item.select("span.num_rnum"):
        circles.append(data.string)

for item in soup.select("div.liveNum"):
    for data in item.select("span.num"):
        nums.append(data.string)
        
for item in soup.select("div.liveNum"):
    for data in item.select("span.before"):
        before_list.append(data.string)

for stem in soup.select("div.liveNumOuter"):
    for data in stem.select("span.livedate"):
        dates.append(data.string)
        

print("\tCOVID-19 한국 상황도")
print()
print("환자 현황", dates[0])
print("\t일일확진자")
print("국내발생 {} | 해외유입 {}".format(today_list[0], today_list[1]))
print()
print("확진환자:",circles[1] + before_list[0])
print("격리해제:", nums[1] +"\t ", before_list[1])
print("치료 중: ", nums[2] + "\t\t ", before_list[2])
print("사망:    ", nums[3] + "\t\t ", before_list[3])
