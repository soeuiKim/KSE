# 차트에 상호작용이 가능하도록 함

import streamlit as st
import numpy as np
import pandas as pd
import time

# checkbox 이용, show/hide data
if st.checkbox('show data frame'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a', 'b', 'c']
    )

    chart_data

st.write('interactivity with widget!')

# 옵션 선택을 위한 selectbox
df = pd.DataFrame({
    'number':[1,2,3,4,5,6,7,8,9,10]
})

# option = st.selectbox(
#     '좋아하는 숫자?',
#     df['number']
# )
# '선택결과 : ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['number']
)
'선택결과 : ', option

### option이 겹쳐서 한개만 사용할수있음ㅎ


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


