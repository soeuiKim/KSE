
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as ulib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns


url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=1000&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=MONTH&ver=1.0'

res = ulib.urlopen(url) #접속해서 xml파일 다운로드
air = BeautifulSoup(res,'html.parser') # dom구조로 변환


df1 = [] #pm10
df2 = [] #pm25
df3 = [] #co
df4 = [] #so2
df5 = [] #no2
df6 = [] #o3
df7 = [] #시간

for item in air.findAll('item'):
    for pm10 in item.findAll('pm10value'):
        df1.append(pm10.string)
    for pm25 in item.findAll('pm25value'):
        df2.append(pm25.string)
    for co in item.findAll('covalue'):
        df3.append(co.string)
    for so2 in item.findAll('so2value'):
        df4.append(so2.string)
    for no2 in item.findAll('no2value'):
        df5.append(no2.string)
    for o3 in item.findAll('o3value'):
        df6.append(o3.string)
    for time in item.findAll('datatime'):
        strt = time.string
        df7.append(strt[11:13])

# =============================================================================
# if pm10.string == '-' :
#             pm10.append(0)
# wine.columns = wine.columns.str.replace(' ','_')
# =============================================================================

data = pd.DataFrame({'pm10':df1,'pm25':df2,'co':df3,'so2':df4,'no2':df5,'o3':df6,'datatime':df7})

data = data[data['pm10'] !='-']
data = data[data['pm25'] !='-']
# print(data.head(20))
# data.to_csv('pm10info.csv', index=False)

# =============================================================================
# 데이터 분석 (회귀분석)
# =============================================================================

Y = data['pm10'] #종속변수
X = data.drop(['pm10'], axis=1, inplace=False) # 독립변수생성
# print(Y.head())
# print(X.head())

X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.3)
# print(X_train.head())
# print(Y_train.head())
# print(X_test.head())
# print(Y_test.head())

lr = LinearRegression() # 선형회귀 객체(model)생성
lr.fit(X_train, Y_train) #훈련(학습) 실행

Y_predict = lr.predict(X_test) #테스트데이터로 예측
# print(Y_predict[0])
# print(Y_test[0])


mse = mean_squared_error(Y_test, Y_predict) # mse추출
rmse = np.sqrt(mse) # 제곱근 취함
print(mse,rmse)
coef = pd.Series(data=np.round(lr.coef_,2), index=X.columns)
# print(lr.coef_, lr.intercept_) #기울기와 y절편
# print(coef)

# =============================================================================
# fig, axs = plt.subplots(figsize=(16,16), ncols=3, nrows=2)
# x_feat = ['pm10','pm25','co','so2','no2','o3','datatime']
# plot_color = ['r','g','b','y','k']
# for i, feat in enumerate(x_feat): #리스트요소를 이용하여 반복
#     row = int(i / 3) # 3개씩 그룹구성
#     col = i % 3 #열번호
#     sns.regplot(x = feat, y = 'pm10', data=data, ax=axs[row][col], color=plot_color[i]) #선형회귀그래프
# =============================================================================

# sns.pairplot(data, hue='pm10')
# plt.show()















