import matplotlib.pyplot as plt
import numpy as np


def elu(x, alpha=1):
    a = x[x > 0]
    b = alpha * (np.exp(x[x < 0]) - 1)
    result = np.concatenate((b, a), axis=0)
    return result


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = elu(x)
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
