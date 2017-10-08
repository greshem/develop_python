#!/usr/bin/python
#coding:utf-8
import numpy as np
def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

#对比numpy的内置FFT函数，我们来对结果进行仔细检查，
#Python

x = np.random.random(1024)
print np.allclose(DFT_slow(x), np.fft.fft(x))

#x = np.random.random(1024)
#np.allclose(DFT_slow(x), np.fft.fft(x))
