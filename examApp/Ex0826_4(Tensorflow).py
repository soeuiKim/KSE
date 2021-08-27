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


# 정규분포를 이용한 정규화
x_mean = train_x.mean() # 평균
x_std = train_x.std() #표준편차

print(x_mean)
# 69.79277358530084

# 데이터 정규화 과정(데이터 전처리 공식)
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
test_y /= y_std   # 데이터 전처리 과정



# # 0 ~ 1 정규화
# train_x = (train_x - train_x.min()) / (train_x.max() - train_x.min())
# train_y = (train_y - train_y.min()) / (train_y.max() - train_y.min())
# test_x = (test_x - test_x.min()) / (test_x.max() - test_x.min())
# test_y = (test_y - test_y.min()) / (test_y.max() - test_y.min())



print(train_x[0])
print(train_y[0])   
print(test_x[0])
print(test_y[0])




model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=39, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='relu'),
    tf.keras.layers.Dense(units=1)
    ])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse')
                                    # learning_rate학습률, loss손실함수(평균제곱오차)
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

history = model.fit(train_x, train_y, batch_size=32, epochs=25, validation_split=0.2)
# 훈련데이터 정답데이터 배치사이즈 반복횟수 검증용 데이터 비율
# 학습실행하면서 로그를 저장

plt.plot(history.history['loss'], 'b--',label='loss')
plt.plot(history.history['val_loss'], 'r--',label='val_loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

model.evaluate(test_x, test_y) #테스트데이터로 검증
pred_y = model.predict(test_x) #테스트데이터로 예측결과 반환

plt.figure(figsize=(5,5))
plt.plot(test_y, pred_y, 'b.') #결과비교그래프
plt.axis([min(test_y),max(test_y),min(test_y),max(test_y)]) #x,y축 동일하게
plt.plot([min(test_y),max(test_y)],[min(test_y),max(test_y)], ls='--',c='r')
plt.xlabel('test_y') #정답
plt.ylabel('pred_y') #예측
plt.show()
















