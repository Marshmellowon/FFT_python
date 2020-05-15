import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack, fft
from pylab import rcParams

rcParams['figure.figsize'] = 13, 11

# Fast Fourier Transform
fs = 100

fmax = 100    # 최대 샘플링 주파수
dt = 1/fs      # 샘플링 주기
N = 100      # 신호 길이

t = np.arange(0, N)*dt   # 0 <= t <= 1, 1/100 step

# 입력 신호
x = 3 * np.cos(2 * np.pi * 10 * t) + 6 * \
    np.sin(2 * np.pi * 15 * t + 3*np.pi/4)

# 입력신호 그래프
plt.subplot(2, 1, 1)
plt.plot(t, x, label='x')
plt.legend()
plt.title('Original Signal')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.grid()

# Fourier spectrum

df = fmax/N   # df = 1/N = fmax/N
f = np.arange(0, N)*df  # frq = [0, df, ..., (N-1)*df]

xf = fftpack.fft(x)*dt  # FFT(x)

# 변환된 그래프
plt.subplot(2, 1, 2)
plt.plot(f[0:int(N/2+1)], np.abs(xf[0:int(N/2+1)]))
plt.title('Fast Fourier Transform')
plt.xlabel('frequency(Hz)')
plt.ylabel('abs(xf)')
plt.grid()
plt.savefig('./img/fast_fourierfft.png')
# plot 띄우기
plt.show()


""" https://m.blog.naver.com/lagrange0115/221029323023 """
