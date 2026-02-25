import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fft import fft

sample_rate = 44100
block_size = 1024

# Setup plot
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0.5)

x = np.arange(block_size)
line1, = ax1.plot(x, np.zeros(block_size))
ax1.set_title("Time Domain Waveform")
ax1.set_ylim(-1, 1)

freqs = np.fft.fftfreq(block_size, 1/sample_rate)
line2, = ax2.plot(freqs[:block_size//2], np.zeros(block_size//2))
ax2.set_title("Frequency Spectrum")

def audio_callback(indata, frames, time, status):
    if status:
        print(status)

    audio_data = indata[:, 0]

    line1.set_ydata(audio_data)

    spectrum = np.abs(fft(audio_data))
    line2.set_ydata(spectrum[:block_size//2])

    fig.canvas.draw_idle()

stream = sd.InputStream(callback=audio_callback,
                        channels=1,
                        samplerate=sample_rate,
                        blocksize=block_size)

stream.start()

print("Listening... Close window to stop.")
plt.show()