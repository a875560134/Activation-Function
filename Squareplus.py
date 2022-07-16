import matplotlib.pyplot as plt
import numpy as np


def Squareplus(x, b=0.2):
    x = 0.5 * (x + np.sqrt(x ** 2 + b))
    return x


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = Squareplus(x)
ax.plot(x, y)
ax.legend()  # 设置图例
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid()  # 设置方格
plt.title("Squareplus")
plt.show()
