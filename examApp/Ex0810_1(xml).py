
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=5&pageNo=1&stationName=%EC%9A%A9%EB%8B%B4%EB%8F%99&dataTerm=DAILY&ver=1.0'

res = ulib.urlopen(url) #접속해서 xml파일 다운로드
air = BeautifulSoup(res,'html.parser') # dom구조로 변환


df1 = []
df2 = []
df3 = []
data = []

for it in air.findAll('item'):
    for pm10 in it.findAll('pm10value'):
        df1.append(pm10.string)
    for pm25 in it.findAll('pm25value'):
        df2.append(pm25.string)
    for time in it.findAll('datatime'):
        df3.append(time.string)

data = pd.DataFrame({'datatime':df3,'pm10':df1,'pm25':df2})

print(data)

data.to_csv('station.csv' )

