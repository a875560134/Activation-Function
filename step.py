import matplotlib.pyplot as plt
import numpy as np

def step_function(x):
    return np.array(x > 0, dtype = np.int)


fig, ax = plt.subplots()

x = np.linspace(-10, 10, 100)
y = step_function(x)
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
