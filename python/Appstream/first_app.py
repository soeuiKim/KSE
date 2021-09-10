# streamlit inport해서 웹 퍼브리싱이 되도록 한다.

import streamlit as st
import numpy as np
import pandas as pd

# 간단한 문자열을 출력
st.title('hellow')

# 데이터프레임 출력
st.write('데이터프레임구성, 테이블을 만들어 보자')
st.write(pd.DataFrame({
    'column1':[1,2,3,4],
    'column2':[10,20,30,40]
}))

# Use magic 
"""
# 안녕하세요
데이터프레임 구성, 테이블 만들기
"""

df = pd.DataFrame({
    ' 학번 ' : [2001,2002,2003,2004],
    '  성명 ' : ['홍길동','춘향이','갑돌이','갑순이']
})
df

# 차트chart와 map맵
#  line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']     
)
st.line_chart(chart_data)

#  plot map ( 랜덤 / [ 표시 위치 범위(반경)] + [위도 경도])
map_data = pd.DataFrame(
    np.random.randn(300,2) / [10, 10] + [36.643917, 127.487620],
    columns=['lat','lon']
)
st.map(map_data)