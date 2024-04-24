######################
###### paremetros ########
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
fc = 150  # Frequência da portadora
ct = np.cos(2 * np.pi * fc * t )


# Plotagem
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, mt)
plt.title('Sinal de Mensagem m(t)')

plt.subplot(4, 1, 2)
plt.plot(t, ct)
plt.title('Portadora c(t)')

frequenciesMt = np.fft.fftfreq(len(mt), T)
mt_freq = fft(mt)

plt.subplot(4, 1, 3)
plt.plot(frequenciesMt, np.abs(mt_freq))
plt.title('m(t) na Frequencia')

frequenciesCt = np.fft.fftfreq(len(ct), T)
ct_freq = (fft(ct))

plt.subplot(4, 1, 4)
plt.plot(frequenciesCt, np.abs(ct_freq))
plt.title('Portadora na Frequencia')



plt.tight_layout()
plt.show()
