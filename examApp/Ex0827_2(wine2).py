# 와인데이터 딥러닝

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

red_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
white_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')

red_df['type'] = 0 #열이 존재하지 않을 경우 새로 생성됨
white_df['type'] = 1
# print(red_df.head())
# print(white_df.head()) # 타입 입력확인

wine = pd.concat([red_df, white_df]) #데이터병합
# print(wine.head())
# print(wine.tail()) # 위쪽과 아래쪽 타입 확인
# print(wine.describe()) # 통계량

# plt.hist(wine['type']) #타입기준 히스토그램
# plt.xticks([0,1]) #0,1 눈 금
# plt.show()

wine_norm = (wine - wine.min()) / (wine.max() - wine.min()) # 0~1정규화
# print(wine_norm.head())

wine_shuffle = wine_norm.sample(frac=1) # 비복원 추출(랜덤)
# print(wine_shuffle.head())

wine_np = wine_shuffle.to_numpy() #데이터프레임을 넘파이배열로 변환(형식변환)
# print(wine_np[:5]) #0~4까지 출력

train_idx = int(len(wine_np) * 0.8) # 80% 위치인덱스 추출
train_x, train_y = wine_np[:train_idx, :-1], wine_np[:train_idx, -1]
# 80% 데이터에대해 마지막열 직전까지 추출해서 x에저장, y는 마지막열 저장
test_x, test_y = wine_np[:train_idx, :-1], wine_np[:train_idx, -1]
# 80% 위치부터 마지막까지
# print(train_x[0])
# print(train_y[0])
# print(test_x[0])
# print(test_y[0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=48, activation='relu', input_shape=(12,)),
    tf.keras.layers.Dense(units=24, activation='relu'),
    tf.keras.layers.Dense(units=12, activation='relu'),
    tf.keras.layers.Dense(units=2, activation='softmax')
    ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07),loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
# 분류문제에 accuracy를 출력해야 정확도를 확인가능

model.summary()

hist = model.fit(train_x, train_y, epochs=25, batch_size=32, validation_split=0.2)
# 신경망 실행하면서 loss, accuracy 저장



plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(hist.history['loss'], 'b--', label='loss')
plt.plot(hist.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1,2,2)
plt.plot(hist.history['accuracy'], 'b--', label='accuracy')
plt.plot(hist.history['val_accuracy'], 'r--', label='val_accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.show()

model.evaluate(test_x, test_y)





















