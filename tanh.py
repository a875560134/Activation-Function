import matplotlib.pyplot as plt
import numpy as np


def tanh(x):
    return 2 / (1 + np.exp(-2 * x)) - 1


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y1 = tanh(x)

ax.plot(x, y1, '-b', label='Tanh')
ax.legend()  # 设置图例
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("Tanh and Sigmoid")
plt.show()
