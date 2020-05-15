import numpy as np
from matplotlib import pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 11, 10  # 그래프를 나타낼 창의 크기 설정


def fft(x):
    # FFT 사용자 함수 정의
    N_len = len(x)  # 파라미터 리스트의 길이

    if N_len <= 1:
        return x
    even = fft(x[0::2])  # 짝수 항 0부터 2간격
    odd = fft(x[1::2])  # 홀수 항 1부터 2간격
    T = [np.exp(-2j*np.pi*k/N_len)*odd[k]
         for k in range(N_len//2)]  # 홀수 항과 회전인자의 곱

    # 합치기
    T_sum = [even[k] + T[k] for k in range(N_len//2)] + \
            [even[k] - T[k] for k in range(N_len//2)]
    return T_sum


fs = 512    # 샘플링 주파수
dt = 1/fs   # 샘플링 주기
N = 512     # 데이터 길이

t = np.arange(0, 1, 1/fs)  # 0 <= t <= 1, step

# 입력 신호
r = 3 * np.cos(2 * np.pi * 10 * t) + 6 * \
    np.sin(2 * np.pi * (15 * t - 3/8*pow(np.pi, 2)))

x_list = list(r)    # 입력신호 type list로 변경
x_fft = fft(x_list)  # 입력신호 FFT함수에 입력

# 변환된 그래프가 그려질 주파수 범위 설정
f = np.arange(0, N)

# Original Signal 그래프 나타내기
plt.subplot(211)
plt.title('Original Signal x(t)')  # title of graph
plt.xlabel('time')  # x축 label
plt.plot(t, r)

# 변환된 그래프 나타내기
plt.subplot(212)
plt.title('Fast Fourier Transform Graph X(f)')  # title of graph
plt.xlabel('frequency')  # x축 label
plt.plot(f[0: int(N//20)], x_fft[0:int(N//20)])
plt.savefig('./img/fast_fourier.png')  # 사진으로 저장하기
plt.show()
