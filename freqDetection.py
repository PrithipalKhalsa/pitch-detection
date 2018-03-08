import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('440_sine.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'

print spf.getframerate()
print spf.getnframes()
print spf.readframes(2000)
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()
