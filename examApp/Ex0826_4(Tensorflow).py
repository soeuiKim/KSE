import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import boston_housing

(train_x, train_y),(test_x, test_y) = boston_housing.load_data()
# 보스턴데이터셋을 다운로드하여 훈련데이터셋과 테스트데이터로 저장

# print(len(train_x),len(test_x))
# 총 506개의 데이터가 404, 102로 나뉘어 짐
# print(train_x[0], train_y[0])
# =============================================================================
# [  1.23247   0.        8.14      0.        0.538     6.142    91.7
#    3.9769    4.      307.       21.      396.9      18.72   ] 15.2
# =============================================================================

x_mean = train_x.mean() # 평균
x_std = train_x.std() #표준편차
# =============================================================================
# print(x_mean)
# 69.79277358530084
# =============================================================================

# 데이터 정규화 과정(공식)
train_x -= x_mean
train_x /= x_std
# 테스트 데이터는 훈련데이터셋을 이용하여 정규화함
test_x -= x_mean
test_x /= x_std

y_mean = train_y.mean()
y_std = train_y.std()
train_y -= y_mean
train_y /= y_std
test_y -= y_mean
test_y /= y_std

print(train_x[0])
print(train_y[0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=39, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='relu'),
    tf.keras.layers.Dense(units=1)
    ])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse')
model.summary()
# =============================================================================
# Model: "sequential"
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# dense (Dense)                (None, 52)                728       
# _________________________________________________________________
# dense_1 (Dense)              (None, 39)                2067      
# _________________________________________________________________
# dense_2 (Dense)              (None, 26)                1040      
# _________________________________________________________________
# dense_3 (Dense)              (None, 1)                 27        
# =================================================================
# Total params: 3,862
# Trainable params: 3,862
# Non-trainable params: 0
# _________________________________________________________________
# 
# 2021-08-26 15:45:23.354847: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX AVX2     To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
# 
# (   I tensorflow/core/platform/cpu_feature_guard.cc:142] 이 TensorFlow 바이너리는 성능이 중요한 작업에서 다음 CPU 명령을 사용하도록 oneAPI Deep Neural Network Library(oneDNN)로 최적화되었습니다. AVX AVX2     다른 작업에서 활성화하려면 적절한 컴파일러 플래그를 사용하여 TensorFlow를 다시 빌드하세요.    )
# =============================================================================























