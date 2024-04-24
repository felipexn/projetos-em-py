#########################
###### FM_FMFE ##########
#########################
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
Fs = 500  # Frequência de amostragem
T = 1/Fs  # Período de amostragem
t = np.arange(0, 1, T)  # Vetor de tempo

# Sinal de mensagem m(t)
fm = 5  # Frequência da mensagem
mt = np.cos(2 * np.pi * fm * t)

# Parâmetros de FM
fc = 150  # Frequência da portadora
E0 = 1.0  # Amplitude da portadora
beta =5 # Índice de modulação em frequência

# Modulação em Frequência de Faixa Estreita (NFM)
e_t = E0 * np.cos(2 * np.pi * fc * t) - (beta * E0/2 ) * np.cos((2 * np.pi * fc - 2 * np.pi * fm) * t) + (beta * E0/2 ) * np.cos((2 * np.pi * fc + 2 * np.pi * fm) * t)

frequencies = np.fft.fftfreq(len(e_t), T)
freq = np.fft.fft(e_t)

# Plotagem no domínio do tempo
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, mt, label='Sinal de Mensagem')
plt.title('Sinal de Mensagem (m(t))')

plt.subplot(3, 1, 2)
plt.plot(t, e_t, label='Sinal Modulado (NFM)')
plt.title('Modulação em Frequência de Faixa Estreita (NFM) No Tempo')

plt.subplot(3, 1, 3)
plt.plot(frequencies,np.abs(freq))
plt.title('Modulaçao em Frequencia de Faixa Estreita (NFM) na Frequencia')

plt.tight_layout()
plt.show()