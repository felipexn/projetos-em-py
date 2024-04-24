######################
###### AM_DSB_SC ########
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

# AM-DSB-SC
am_dsb_sc = mt * ct

# Plotagem no domínio do tempo
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, mt , '--r')
plt.plot(t, -mt , '--r')
plt.plot(t, am_dsb_sc)
plt.title('AM-DSB-SC')

# Transformada de Fourier para obter a representação em frequência
frequencies_dsb_sc = np.fft.fftfreq(len(am_dsb_sc), T)
#am_dsb_sc_freq = fftshift(fft(am_dsb_sc))
am_dsb_sc_freq = (np.fft.fft(am_dsb_sc))

plt.subplot(4, 1, 2)
plt.plot(frequencies_dsb_sc, np.abs(am_dsb_sc_freq))
plt.title('AM-DSB-SC no Domínio da Frequência')
plt.xlabel('Frequência (Hz)')

plt.tight_layout()
plt.show()
