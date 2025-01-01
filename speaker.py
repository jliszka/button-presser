import time
import array
import math
import audioio
import audiocore
import board
import ulab

_audio = audioio.AudioOut(board.A0)

_frequencies = [ 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88 ]
_note_names = { 'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11 }

def note(name, octave=4):
    return _frequencies[_note_names[name]] * math.pow(2, octave-4)

def play(frequency):
    waveform = wf(frequency)
    samples = ulab.array((waveform + 1) * (2 ** 15 - 1), dtype=ulab.uint16)
    sample = audiocore.RawSample(samples)
    _audio.play(sample, loop=True)

def stop():
    _audio.stop()

def wf(frequency):
    samples = 60 * 8000 // frequency
    adj_freq = 60 * 8000 / samples
    samples_per_cycle = 8000 / adj_freq
    waveform = ulab.arange(samples, dtype=ulab.float)
    waveform = waveform * 2 * math.pi / samples_per_cycle
    return ulab.vector.sin(waveform)

def play2(frequency1, frequency2):
    waveform = wf2(frequency1, frequency2)
    samples = ulab.array((waveform + 1) * (2 ** 15 - 1), dtype=ulab.uint16)
    sample = audiocore.RawSample(samples)
    _audio.play(sample, loop=True)

def wf2(frequency1, frequency2):
    samples1 = 8000 // frequency1
    adj_freq1 = 8000 / samples1
    samples_per_cycle1 = 8000 / adj_freq1

    samples2 = 8000 // frequency2
    adj_freq2 = 8000 / samples2
    samples_per_cycle2 = 8000 / adj_freq2

    waveform1 = ulab.arange(samples1, dtype=ulab.float)
    waveform1 = waveform1 * 2 * math.pi / samples_per_cycle1
    waveform1 = ulab.vector.sin(waveform1)

    waveform2 = ulab.arange(samples2, dtype=ulab.float)
    waveform2 = waveform2 * 2 * math.pi / samples_per_cycle2
    waveform2 = ulab.vector.sin(waveform2)

    wf = ulab.concatenate((waveform1, waveform2))

    return wf
