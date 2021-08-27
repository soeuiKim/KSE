# 와인 데이터 분석

# https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv - 자료파일 다운로드 주소
# =============================================================================
# 기본 column
# fixed acidity
# volatile acidity
# citric acid
# residual sugar
# chlorides 
# free  sulfur dioxide 
# total sulfur dioxide 
# density 
# pH
# sulphates 
# alcohol
# quality
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




red_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

# print(red_df.head())

white_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')

# print(white_df.head())
# print(len(red_df),len(white_df))

red_df.insert(0, column='type',value='red') # 열을 추가, 타입항목에 red문자열 추가
white_df.insert(0, column='type',value='white') # white열 추가
# print(red_df.head())
# print(white_df.head())

wine = pd.concat([red_df, white_df]) #데이터프레임 병합
# print(wine.shape) #데이터프레임의 행렬구조

# 공백문자를 밑줄문자로 치환
wine.columns = wine.columns.str.replace(' ','_')
# print(wine.head())
# print(wine.describe()) #데이터프레임의 통계현황 출력(갯수,최대값,최소값,중간값 등)
# print(wine.quality.unique()) #중복제거
# print(wine.quality.value_counts()) #중복되는 항목 카운트

print(wine.groupby('type')['quality'].describe()) # 와인타입각각의 퀄리티 통계현황
print(wine.groupby('type')['quality'].mean()) # 평균
print(wine.groupby('type')['quality'].std()) # 표준편차

# 와인의 퀄리티를 추출해서 저장(pandas)
red_wine_quality = wine.loc[wine['type'] == 'red','quality']
white_wine_quality = wine.loc[wine['type'] == 'white','quality']

# print(red_wine_quality)
sns.distplot(red_wine_quality, kde=True, label='red wine') # 히스토그램
sns.distplot(white_wine_quality, kde=True, label='white wine') # 히스토그램
plt.title('Quality of Wine')
plt.legend()
plt.show()











