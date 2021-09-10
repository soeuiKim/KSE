# https://docs.streamlit.io/en/stable/tutoria 

import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 데이터 로드 표시
data_load_state = st.text('데이터 로딩중')
# 만개의 데이터 로드
data = load_data(10000)
# 로드 성공 표시
data_load_state.text("로드 끝! (using st.cache)")

with st.form("my_form"):
    st.write("ok")
    slider_val = st.slider("slider")
    checkbox_val = st.checkbox("checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Yes ok!")

# st.subheader('Raw data')
# st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
    )[0]

if st.checkbox('show histogram'):
    with st.container():
        st.subheader('Number of pickups by hour')
        st.bar_chart(hist_values)


# st.subheader('Map of all pickups')
# st.map(data)

# hour_to_filter = 17
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# 상호작용 자동제출을 버튼으로 ( 3가지 방식)
# with st.form(key='my_form'):
#     text_input = st.text_input(label='Enter your name')
#     submit_button = st.form_submit_button(label='Submit')

# form = st.form(key='my_form')
# form.text_input(label='Enter some text')
# submit_button = form.form_submit_button(label='Submit')

# if submit_button:
#     st.write(f'hello {name}')


# # Get some data.
# data_1 = np.random.randn(10, 2)

# # Show the data as a chart.
# chart = st.line_chart(data_1)

# # Wait 1 second, so the change is clearer.
# time.sleep(1)

# # Grab some more data.
# data_2 = np.random.randn(10, 2)

# # Append the new data to the existing chart.
# chart.add_rows(data_2)


progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()
