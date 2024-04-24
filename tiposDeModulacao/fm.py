#########################
###### FM ###############
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
ct=(2 * np.pi * fc * t)
CT=np.cos(ct)
kf = 1   # Índice de modulação em frequência

# Modulação em Frequência (FM)
x_fm = np.cos(ct +  kf * np.cumsum(mt) )

frequencies = np.fft.fftfreq(len(x_fm), T)
freq = np.fft.fft(x_fm)

# Plotagem no domínio do tempo
plt.figure(figsize=(12, 6))

plt.subplot(4, 1, 1)
plt.plot(t, mt, label='Sinal de Mensagem')
plt.title('Sinal de Mensagem (m(t))')

plt.subplot(4, 1, 2)
plt.plot(t, CT )
plt.title('Portadora no tempo')


plt.subplot(4, 1, 3)
plt.plot(t, x_fm, label='Sinal Modulado (FM)')
plt.title('Modulação em Frequência (FM)')

plt.subplot(4, 1, 4)
plt.plot(frequencies,np.abs(freq))
plt.title('Sinal Modulado em Frequencia no Dominio da Frequencia')

plt.tight_layout()
plt.show()
