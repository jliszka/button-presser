import time
import array
import math
import audioio
import audiocore
import audiomixer
import board
import ulab

_audio = audioio.AudioOut(board.A0)
_mixer = audiomixer.Mixer(voice_count=5, channel_count=1, samples_signed=False)
#_audio.play(_mixer)
_playing = {}


def play(frequency):
    waveform = wf(frequency*2)
#    waveform = add_harmonic(waveform, frequency, 3, 0.3)
#    waveform = add_harmonic(waveform, frequency, 5, 0.1)
    samples = ulab.array((waveform + 1) * (2 ** 15 - 1), dtype=ulab.uint16)
    sample = audiocore.RawSample(samples)
    voice = None
    for v in range(5):
        if v not in _playing:
            voice = v
            break
    print("using voice %d" % voice)
    if voice is None:
        return
    _mixer.voices[voice].play(sample, loop=True)
    _playing[voice] = True
    return voice
    #_audio.play(sample, loop=True)

def stop(voice):
    del _playing[voice]
    _mixer.stop_voice(voice)

def wf(frequency):
    samples_per_cycle = 8000 // frequency
    waveform = ulab.arange(2520, dtype=ulab.float)
    waveform = waveform * 2 * math.pi / samples_per_cycle
    return ulab.vector.sin(waveform)
    
def add_harmonic(base, frequency, harmonic, amplitude):
    return base * (1-amplitude) + wf(frequency * harmonic) * amplitude
    
