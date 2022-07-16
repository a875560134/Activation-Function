
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def swish(x):
    return sigmoid(x) * x

fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = swish(x)
ax.plot(x, y)
ax.legend() # 设置图例
# 画轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('axes', 0.5))
plt.grid() # 设置方格
plt.title("Swish")
plt.show()
