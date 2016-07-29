import math
import pyaudio
import random

_author_ = 'Gentz'

PyAudio = pyaudio.PyAudio

# See http://en.wikipedia.org/wiki/Bit_rate#Audio
sampleRate = 44100  # number of frames per second/frameset.
length = 0.25  # seconds to play sound

numberOfFrames = int(sampleRate * length)
restFrames = (numberOfFrames % sampleRate) * 0

p = PyAudio()
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=sampleRate,
                output=True)

note = random.randint(16, 39)
oldNote = note

note2 = random.randint(52, 75)
oldNote2 = note2

while 0 == 0:
    offset = 0
    if note > oldNote:
        offset = 1
    if note < oldNote:
        offset = -1

    oldNote = note
    note += random.randint(-3, 3) + offset

    if note > 40:
        note = 35
    if note < 1:
        note = 5

    offset2 = 0
    if note2 > oldNote2:
        offset2 = 1
    if note2 < oldNote2:
        offset2 = -1

    oldNote2 = note2
    note2 += random.randint(-3, 3) + offset2

    if note2 > 88:
        note2 = 83
    if note2 < 50:
        note2 = 55

    frequency = 440 * 2 ** ((note-49)/12)
    frequency2 = 440 * 2 ** ((note2-49)/12)

    waveData = ''

    for x in range(numberOfFrames):
        sound1 = math.sin(x / ((sampleRate / 100 * 16 / frequency) / math.pi)) * 127 + 128
        sound2 = math.sin(x / ((sampleRate / 100 * 16 / frequency2) / math.pi)) * 127 + 128
        waveData += chr(int(sound1 * 0.34 + sound2 * 0.66))

    for x in range(restFrames):
        waveData += chr(128)

    stream.write(waveData)

stream.stop_stream()
stream.close()
p.terminate()

