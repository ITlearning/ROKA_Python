from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

nums = []

for item in soup.select("div.info_core"):
    for data in item.select("span.num"):
        nums.append(data.string)
        
print("오늘 코로나 확진자수:",nums)