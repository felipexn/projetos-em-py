#########################
###### AM_VSB_SC ########
#########################
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
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

# AM-VSB-SC
am_vsb_sc = mt * ct

# Aplicar filtro passa-banda para pegar apenas a banda lateral vestigial
cutoff_frequency = fc-fm  # Ajuste conforme necessário
nyquist = 0.5 * Fs
normal_cutoff = cutoff_frequency / nyquist
b, a = butter(8, normal_cutoff, btype='low', analog=False)
filtered_signal = lfilter(b, a, am_ssb_sc)

# Transformada de Fourier para obter a representação em frequência
frequencies_vsb_sc = np.fft.fftfreq(len(filtered_signal), T)
am_vsb_sc_freq = (fft(filtered_signal))

# Plotagem no domínio do tempo
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, am_vsb_sc)
plt.title('AM-VSB-SC')

frequencies = np.fft.fftfreq(len(am_vsb_sc), T)
freq = (fft(am_vsb_sc))
plt.subplot(4, 1, 2)
plt.plot(frequencies, freq)
plt.title('AM-VSB-SC')

# Plotagem no domínio da frequência do sinal original
plt.subplot(4, 1, 3)
plt.plot(frequencies_vsb_sc, np.abs(am_vsb_sc_freq))
plt.title('AM-VSB-SC no Domínio da Frequência após Filtro ')
plt.xlabel('Frequência (Hz)')

plt.subplot(4, 1, 4)
plt.plot(t,filtered_signal)
plt.title('AM-VSB-SC no Domínio do tempo após o Filtro')
plt.xlabel('Tempo')

plt.tight_layout()
plt.show()
