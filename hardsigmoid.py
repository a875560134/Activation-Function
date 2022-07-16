import matplotlib.pyplot as plt
import numpy as np


def Hard_Sigmoid(x):
    f = (2 * x + 5) / 10
    return np.where(np.where(f > 1, 1, f) < 0, 0, np.where(f > 1, 1, f))


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = Hard_Sigmoid(x)
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
