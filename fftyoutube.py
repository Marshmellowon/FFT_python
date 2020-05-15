import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack, fft

dt = 0.01
fs = 1/dt
T = 0.16

t = np.arange(0, 1, 1/fs) # t의 범위

y = 3 * np.cos(2 * np.pi * 10 * t) + 6 * \
    np.sin(2 * np.pi * 15 * t + 3*np.pi/4) # 입력 신호


length = len(y)
f = np.linspace(-(fs / 2), fs / 2, length)

Y = fftpack.fft(y)/len(y) # power 
Y_abs = abs(Y)
Y_shift = fftpack.fftshift(Y_abs)

plt.subplot(311)
plt.title("x(t) = 3cos(20πt) + 6sin(30πt - 3/(4π)), (0 <= t <= 1)")
plt.plot(t, y)

plt.subplot(313)
plt.plot(f, Y_shift)
plt.title("Fast Fourier Transform graph")
plt.savefig('./img/fftgraph.png')
plt.show()
