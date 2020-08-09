
#%%
from muallef.io import AudioLoader
from muallef.pitch import MultiPitch
from muallef.util.units import Hz_to_MIDI

import numpy as np
import matplotlib.pyplot as plt

# matplotlib options
from matplotlib import rcParams
rcParams['savefig.transparent'] = True
rcParams['text.usetex'] = False


# load audio
audio_file = "/Users/thomash/Documents/Code/bakery/momo/media/test_files/chaos/8s_stereo_magnifique_hang.wav"
audio = AudioLoader(audio_file)
audio.cut(stop=10)
fs = audio.sampleRate
x = audio.signal
frameSize = 2048

print("starting multipitch")
klapuri = MultiPitch(x, fs, method='klapuri', frameSize=frameSize, max_polyphony=10)
freq = klapuri()
#%%
pitch = Hz_to_MIDI(freq)

print("done multipitch")
time = np.arange(pitch.shape[1]) * (frameSize / fs)


fig, ax = plt.subplots(figsize=(10,10))
fig.suptitle("Multi-pitch estimation using Klapuri's iterative method")
ax.set_title("Magnifique Hang 8s")
for m in range(pitch.shape[0]):
    ax.scatter(time, freq[m],#s=5
    )
ax.set_xlabel('Time (s)')
ax.set_ylabel('Freq (MIDI)')
#ax.set_ylim(33, 72)
ax.set_facecolor((0, 0, 0))
plt.show()

# %%
