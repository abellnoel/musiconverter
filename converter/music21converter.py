import music21 as m 
import pygame
import os

#get directory this file is in
dir_path = os.path.dirname(os.path.realpath(__file__))
MIDI_SAVE_PATH = dir_path
MIDI_SAVE_NAME = "/conversion.mid"

#find helper programs such as musescore
s = m.stream.Stream()
n = m.note.Note("C")
n.quarterLength = 0.5
s.repeatAppend(n,4)
mf = m.midi.translate.streamToMidiFile(s)

#saves music21 stream as midi file
midiExport = s.write('midi', fp=MIDI_SAVE_PATH + MIDI_SAVE_NAME)

#plays midifile location through pygame
def play_midi(midi):
    # mixer config
    freq = 44100  # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024   # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30) # check if playback has finished

#play saved midifile
play_midi(MIDI_SAVE_PATH + MIDI_SAVE_NAME)