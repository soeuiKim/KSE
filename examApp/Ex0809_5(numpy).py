# numpy 활용 그래프

import matplotlib.pyplot as plt
import numpy as np


'''
# 동일 공간에 그리기
#  range : 연속 정수값 발생 , arange : 연속 실수값 발생
t = np.arange(0.0 , 5.0, 0.2) # 실수 연속 구간 생성
plt.plot(t, t, 'r--', t, t**2, 'b^:', t, t**3, 'go-')
'''
t = np.arange(0.0 , 5.0, 0.2)

# 분리된 공간에 그리기
# x축에 각각의 그래프 제목 표시(t, t**2, t**3)
plt.figure(figsize=(9,3))
plt.subplot(1,3,1) # 1행 3열의 첫번째
plt.plot(t, t, 'r--')
plt.xlabel('y=x')
# plt.title('t')

plt.subplot(1,3,2)
plt.plot(t, t**2, 'bo:')
# plt.title('t**2')
plt.xlabel('y=x**2')

plt.subplot(1,3,3)
plt.plot(t, t**3, 'g^-.')
# plt.title('t**3')
plt.xlabel('y=x**3')

plt.suptitle('Categorical Plotting')

plt.show()