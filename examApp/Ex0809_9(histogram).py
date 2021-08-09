# 히스토그램 Histogram

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(10, 3, 20000) # 평균 10, 표준편차3, 개수 200인 정규분포

plt.hist(data, bins = 300 , alpha = 0.5 , color = 'green' , histtype = 'step')
# bins 값을 몇개로 쪼갤지

plt.show() 