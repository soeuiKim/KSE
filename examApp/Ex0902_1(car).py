# https://archive.ics.uci.edu - auto검색 - 첫번째사이트 - datafolder - duto_mpg_data
#  -엑셀파일로 열기(텍스트마법사에서 탭과 공백제거하기)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 회기분석용 모듈
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data_df = pd.read_csv('auto_mpg.csv')
# print (data_df.head())

data_df = data_df.drop(['car_name','origin','horsepower'], axis=1, inplace=False) # axis가 1일 경우 열, 0일경우 행 요소 삭제

# print (data_df.head())

# print(data_df.shape) # 행, 열의 갯수
# print(data_df.info()) # 데이터 형식
# print(data_df.describe()) # 통계정보

# ↑ 데이터 전처리


Y = data_df['mpg'] #종속변수
X = data_df.drop(['mpg'], axis=1, inplace=False) # 독립변수생성
# print(Y.head())
# print(X.head())

# 회기분석도 일종의 학습이기 때문에 훈련,실습데이터를 나눔
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
# print(mse,rmse)
# print(lr.coef_, lr.intercept_) #기울기와 y절편
coef = pd.Series(data=np.round(lr.coef_,2), index=X.columns)
# print(coef)

# =============================================================================
# fig, axs = plt.subplots(figsize=(16,16), ncols=3, nrows=2)
# x_feat = ['cylinders', 'displacement', 'weight', 'acceleration', 'model_year']
# plot_color = ['r','g','b','y','k']
# for i, feat in enumerate(x_feat): #리스트요소를 이용하여 반복
#     row = int(i / 3) # 3개씩 그룹구성
#     col = i % 3 #열번호
#     sns.regplot(x = feat, y = 'mpg', data=data_df, ax=axs[row][col], color=plot_color[i]) #선형회귀그래프
# =============================================================================
    

result = lr.predict([[8,350,3200,22,99]])
print(result)

df_corr = data_df.corr(method='pearson') #pearson 상관계수
print(df_corr)
df_corr.to_csv('df_corr.csv')

sns.pairplot(data_df, hue='mpg')
# 산점도와 히스토그램, hue는 종속변수
plt.show()


# =============================================================================
# heatmap_data = data_df[['mpg','cylinders', 'displacement', 'weight', 'acceleration', 'model_year']]
# sns.heatmap(heatmap_data.astype(float).corr(), linewidths=0.1, annot=True)
# plt.show()
# =============================================================================


sns.catplot(x='cylinders', y='weight', hue='mpg', data= data_df)
plt.show()













