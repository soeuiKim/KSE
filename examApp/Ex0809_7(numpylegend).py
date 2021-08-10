# 그래프 범례표시

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3], label='Line 1', linestyle='--')
plt.plot([3,2,1], label='Line 2', linewidth= 3)

plt.legend() # 범례 표시 (레이블에 있던것을 표시)

plt.show()