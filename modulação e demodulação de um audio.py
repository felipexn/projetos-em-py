import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.io import wavfile
from IPython.display import Audio, display
from scipy.fft import fft, fftshift

# Função para criar um filtro passa-baixa
def butter_lowpass(cutoff, fs, order=6):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=6):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Carregando o arquivo de áudio
fs, audio_data = wavfile.read('/content/drive/MyDrive/Colab Notebooks/surpresa.wav')
audio_data_left = audio_data[:, 0]

# Parâmetros
f_portadora = 10000000  # Frequência da portadora em Hz
f_cutoff = 20000  # Frequência de corte do filtro passa-baixa em Hz
order = 6  # Ordem do filtro

t = np.linspace(0, len(audio_data_left) / fs, len(audio_data_left))

# Modulação VSB-SC
dbs_signal = (1 + audio_data_left) * np.cos(2 * np.pi * f_portadora * t)
signal = butter_lowpass_filter(dbs_signal, f_cutoff, fs, order)

# Demodulação VSB-SC
demodulated_signal = signal * np.cos(2 * np.pi * f_portadora * t)

# Plotando os gráficos
plt.figure(figsize=(12, 8))

plt.subplot(6, 1, 1)
plt.plot(t, audio_data_left)
plt.title('Sinal de Áudio Original (Canal Esquerdo)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 2)
plt.plot(t, vsb_signal)
plt.title('Sinal VSB-SC Modulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 3)
plt.plot(t, demodulated_signal)
plt.title('Sinal VSB-SC Demodulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

frequenciesMttt = np.fft.fftfreq(len(dbs_signal), t)
mt_freqtt = fft(dbs_signal)

plt.subplot(6, 1, 4)
plt.plot(frequenciesMttt, np.abs(mt_freqtt))
plt.title(' Sinal modulado na Frequencia')

frequenciesMt = np.fft.fftfreq(len(signal), t)
mt_freq = fft(signal)

plt.subplot(6, 1, 5)
plt.plot(frequenciesMt, np.abs(mt_freq))
plt.title(' Sinal na Frequencia')

frequenciesMtt = np.fft.fftfreq(len(demodulated_signal), t)
mt_freqt = fft(demodulated_signal)

plt.subplot(6, 1, 6)
plt.plot(frequenciesMtt, np.abs(mt_freqt))
plt.title('Sinal demodulado na Frequencia')

plt.tight_layout()
plt.show()

# Reproduzindo os áudios
print("Reproduzindo o sinal modulado (VSB-SC)...")
display(Audio(signal, rate=fs))

print("Reproduzindo o sinal demodulado...")
