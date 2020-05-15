import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack, fft
from pylab import rcParams

# 창 크기 설정
rcParams['figure.figsize'] = 10, 7

fs = 1000

fmax = 1000    # 최대 샘플링 주파수
dt = 1/fs      # 샘플링 주기
N = 1000       # 데이터 길이
t = np.arange(0, 1, 1/fs)  # t의 범위

# 입력 신호
x = 3 * np.cos(2 * np.pi * 10 * t) + 6 * \
    np.sin(2 * np.pi * 15 * t + 3*np.pi/4)

even = x[0::2]  # 짝수항들
odd = x[1::2]  # 홀수항들
T = [np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)]  # 짝수항과 회전인자의 곱

# 짝수항과 홀수항의 합
T_sum = [even[k] + T[k] for k in range(N//2)] + \
    [even[k] - T[k] for k in range(N//2)]

# 입력 신호 그래프 나타내기
plt.subplot(211)
plt.title('Original Signal')
plt.plot(t, T_sum)

df = fmax/N   # df = 1/N = fmax/N
f = np.arange(0, N)*df  # frq = [0, df, ..., (N-1)*df]

# 나눠서 합친 항들을 푸리에 변환
m = np.fft.fft(T_sum)*dt

# 변환된 그래프 나타내기
plt.subplot(212)
plt.title('Fast Fourier Transform')
plt.plot(f[0:int(N/20)], abs(m[0:int(N/20)]))
plt.show()
