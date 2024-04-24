#########################
###### AM_SSB_SC ########
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

# AM-SSB-SC
am_ssb_sc_upper=mt*ct
am_ssb_sc_lower=-mt*ct

am_ssb_sc = mt * ct


# Aplicar filtro passa-baixas para pegar apenas o LSB
cutoff_frequency = fc-fm  # Ajuste conforme necessário
nyquist = 0.5065 * Fs
normal_cutoff = cutoff_frequency / nyquist
b, a = butter(22, normal_cutoff, btype='low', analog=False)
filtered_signal = lfilter(b, a, am_ssb_sc)

# Transformada de Fourier para obter a representação em frequência
frequencies_ssb_sc = np.fft.fftfreq(len(filtered_signal), T)
am_ssb_sc_freq = (fft(filtered_signal))


frequencies = np.fft.fftfreq(len(am_ssb_sc), T)
freq = (fft(am_ssb_sc))
# Plotagem no domínio do tempo
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(t, am_ssb_sc_upper, label='Superior')
plt.plot(t, am_ssb_sc_lower, label='Inferior')
plt.title('AM-SSB-SC')
plt.legend()

# Plotagem no domínio da frequência
plt.subplot(4, 1, 2)
plt.plot(frequencies, np.abs(freq))
plt.title('Sinal modulado na Frequencia')


# Plotagem no domínio da frequência
plt.subplot(4, 1, 3)
plt.plot(frequencies_ssb_sc, np.abs(am_ssb_sc_freq))
plt.title('AM-SSB-SC no Domínio da Frequência após o  Filtro')
plt.xlabel('Frequência (Hz)')

plt.subplot(4, 1, 4)
plt.plot(t,filtered_signal)
plt.title('AM-SSB-SC no Domínio do tempo após o Filtro')
plt.xlabel('Tempo')

plt.tight_layout()
plt.show()
