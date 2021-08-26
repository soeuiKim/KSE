from sklearn.datasets import load_boston
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression #선형회귀분석
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
import seaborn as sns

boston = load_boston() # 데이터셋 다운로드
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names) #데이터프레임으로 저장

# print(boston_df.head())
# =============================================================================
#  CRIM    ZN  INDUS  CHAS    NOX  ...  RAD    TAX  PTRATIO       B  LSTAT
# 0  0.00632  18.0   2.31   0.0  0.538  ...  1.0  296.0     15.3  396.90   4.98
# 1  0.02731   0.0   7.07   0.0  0.469  ...  2.0  242.0     17.8  396.90   9.14
# 2  0.02729   0.0   7.07   0.0  0.469  ...  2.0  242.0     17.8  392.83   4.03
# 3  0.03237   0.0   2.18   0.0  0.458  ...  3.0  222.0     18.7  394.63   2.94
# 4  0.06905   0.0   2.18   0.0  0.458  ...  3.0  222.0     18.7  396.90   5.33
# [5 rows x 13 columns]
# =============================================================================


boston_df['PRICE'] = boston.target #price열 추가
# print(boston_df.head())
# =============================================================================
#  CRIM    ZN  INDUS  CHAS    NOX  ...    TAX  PTRATIO       B  LSTAT  PRICE
# 0  0.00632  18.0   2.31   0.0  0.538  ...  296.0     15.3  396.90   4.98   24.0
# 1  0.02731   0.0   7.07   0.0  0.469  ...  242.0     17.8  396.90   9.14   21.6
# 2  0.02729   0.0   7.07   0.0  0.469  ...  242.0     17.8  392.83   4.03   34.7
# 3  0.03237   0.0   2.18   0.0  0.458  ...  222.0     18.7  394.63   2.94   33.4
# 4  0.06905   0.0   2.18   0.0  0.458  ...  222.0     18.7  396.90   5.33   36.2
# [5 rows x 14 columns]
# =============================================================================

# print(boston_df.info()) #결측값 확인
# =============================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 506 entries, 0 to 505
# Data columns (total 14 columns):
#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   CRIM     506 non-null    float64
#  1   ZN       506 non-null    float64
#  2   INDUS    506 non-null    float64
#  3   CHAS     506 non-null    float64
#  4   NOX      506 non-null    float64
#  5   RM       506 non-null    float64
#  6   AGE      506 non-null    float64
#  7   DIS      506 non-null    float64
#  8   RAD      506 non-null    float64
#  9   TAX      506 non-null    float64
#  10  PTRATIO  506 non-null    float64
#  11  B        506 non-null    float64
#  12  LSTAT    506 non-null    float64
#  13  PRICE    506 non-null    float64
# dtypes: float64(14)
# memory usage: 55.5 KB
# None
# =============================================================================


y = boston_df['PRICE']
x = boston_df.drop(['PRICE'], axis=1, inplace=False) #price뺀 13개 독립변수 저장

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
# 훈련 데이터셋과 테스트데이터셋을 분리하여 저장

lr = LinearRegression() #회귀model생성
lr.fit(x_train, y_train) #훈련 실행

y_predict = lr.predict(x_test) # 30% 테스트데이터를 이용하여 예측
# print(y_predict[0])
mse = mean_squared_error(y_test, y_predict) # 정답과 예측결과를 mse로 저장
rmse = np.sqrt(mse) # 제곱근 취함
print(mse,rmse)
print(lr.coef_) #기울기(13개 각각의 회귀계수)
print(lr.intercept_) #y절

# 5행 3열 그래프 영역
fig, axs = plt.subplots(figsize=(16,16), ncols=3, nrows=5)
x_feat = ['CRIM' ,'ZN','INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

# 리스트로 부터 인덱스와 문자열 획들
for i, feat in enumerate(x_feat): 
    row = int(i/3) # 행 결정(0,1,2    3,4,5    6,7,8 ........)
    col = i % 3 # 열 결정
    sns.regplot(x = feat, y='PRICE', data = boston_df, ax = axs[row][col])
    # 회귀그래프























