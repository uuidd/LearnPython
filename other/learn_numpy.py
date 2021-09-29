import numpy as np
import matplotlib.pyplot as plt

# def mandelbrot(h, w, max_it=20):
#     y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
#     c = x + y * 1j
#     z = c
#     div_time = max_it + np.zeros(z.shape, dtype=int)
#
#     for i in range(max_it):
#         z = z ** 2 + c
#         diverge = z * np.conj(z) > 2 ** 2
#         div_now = diverge & (div_time == max_it)
#         div_time[div_now] = i
#         z[diverge] = 2
#
#     return div_time


# plt.imshow(mandelbrot(400, 400))
# plt.show()
# mu, sigma = 6, 0.5
# v = np.random.normal(mu, sigma, 10000)
# plt.hist(v, bins=50, density=1)
# plt.show()
plt.figure()
R = 300
delta = 0.6
f = 0.466 * R
y = np.arange((-R) / 2, R / 2, 0.01)
z = R - ((R ** 2) - (y ** 2)) ** 0.5
plt.plot(y, z)
z1 = 1 / (4 * (f + delta)) * (y ** 2) - delta
plt.plot(y, z1, 'r')
plt.xlim((-50, 50))
plt.ylim((-2, 6))
ax = plt.gca()  # 获取当前坐标的位置
# 去掉坐标图的上和右 spine翻译成脊梁
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')
# 指定坐标的位置
ax.xaxis.set_ticks_position('bottom')  # 设置bottom为x轴
ax.yaxis.set_ticks_position('left')  # 设置left为x轴
ax.spines['bottom'].set_position(('data', 0))  # 这个位置的括号要注意
ax.spines['left'].set_position(('data', 0))
plt.show()
