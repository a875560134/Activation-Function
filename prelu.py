import matplotlib.pyplot as plt
import numpy as np


def prelu(x):
    return np.maximum(0.25 * x, x)


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = prelu(x)

ax.plot(x, y)
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("Sigmoid")
plt.show()
