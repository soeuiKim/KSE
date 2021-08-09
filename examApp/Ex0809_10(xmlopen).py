# xml 불러오기 (공공데이터_ data.go.kr)

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

url ='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%B6%A9%EB%B6%81&ver=1.0'

res = ulib.urlopen(url) # 지정된 주소로 부터 xml 반환 (단순 파일)

air = BeautifulSoup(res,"html.parser") # xml 파싱 (저장)

# 충북지역의 측정소명과 pm10값을 추출
df1 = [] # 측정소명 저장한 빈 리스트 생성
df2 = [] # pm10

for it in air.findAll("item") : # 반복되는 item태그로 부터 it변수에 항목을 반환
    for sn in it.findAll('stationname') : # 모두 소문자로 
        # print(sn.string)
        df1.append(sn.string)
    for pm10 in it.findAll('pm10value') : 
        # print(pm10.string)
        df2.append(pm10.string)
    
# print (df1)
# print (df2)

df = pd.DataFrame({'station' : df1, 'pm10' : df2})
print (df.head()) # 상위 5개(기본값) 항목 출력
df.to_csv('test.csv', encoding='euc-kr') # csv형식 파일 저장(구분자)

