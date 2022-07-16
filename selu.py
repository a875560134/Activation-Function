import math

import matplotlib.pyplot as plt
import numpy as np

e = math.e


def selu(x, a=1, b=1):
    return a * np.where(x > 0, x, b * ((e ** x) - 1))


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = selu(x)

ax.plot(x, y)
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("Sigmoid")
plt.show()
