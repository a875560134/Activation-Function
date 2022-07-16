import matplotlib.pyplot as plt
import numpy as np


def ReLU6(x):
    return np.where(np.where(x < 0, 0, x) > 6, 6, np.where(x < 0, 0, x))

fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = ReLU6(x)
ax.plot(x, y)
ax.legend()  # 设置图例
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("ELU")
plt.show()
