######################
###### AM_DSB ########
######################
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

# Parâmetros
Fs = 500  # Frequência de amostragem
T = 1/Fs  # Período de amostragem
t = np.arange(0, 1, T)  # Vetor de tempo

# Sinal de mensagem m(t)
fm = 5  # Frequência da mensagem
mt = np.cos(2 * np.pi * fm * t)

# Portadora c(t)
fc = 50  # Frequência da portadora
ct = np.cos(2 * np.pi * fc * t)

# AM-DSB
am_dsb = (1 + mt) * ct

# Plotagem no domínio do tempo
plt.figure(figsize=(12, 8))



plt.subplot(2, 1, 1)
plt.plot(t, mt +1, '--r')
plt.plot(t, -mt -1, '--r')
plt.plot(t, am_dsb)
plt.title('AM-DSB')

# Transformada de Fourier para obter a representação em frequência
frequencies = np.fft.fftfreq(len(am_dsb), T)
am_dsb_freq = np.fft.fft(am_dsb)

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(am_dsb_freq))
plt.title('AM-DSB no Domínio da Frequência')
plt.xlabel('Frequência (Hz)')

plt.tight_layout()
plt.show()
