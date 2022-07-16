import math

import matplotlib.pyplot as plt
import numpy as np

e = math.e


def softplus(x):
    return math.log(1 + pow(e, x))


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
for i in range(100):
    y[i] = softplus(x[i])
ax.plot(x, y)
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("Sigmoid")
plt.show()
