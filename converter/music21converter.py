import music21 as m 
import pygame
import os
import re

#get directory this file is in
dir_path = os.path.dirname(os.path.realpath(__file__))
MIDI_SAVE_PATH = dir_path
MIDI_SAVE_NAME = "/conversion.mid"

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
        
#run sheet music model conversion on selected file
def convert(file):
    os.chdir("../util")
    command = "python ctc_predict.py -image " + file + " -model Models/semantic_model.meta -vocabulary Data/vocabulary_semantic.txt"
    os.system(command)

def translate():  
    semantics = open(dir_path + "/semantics/semantics.txt", "r")
    #load created semantic text file into array
    stream = m.stream.Stream()
    semArray = []
    for l in semantics:
        sem = l.rstrip()
        #check if note or rest
        match = re.match(r"^note", sem)
        #NOTE
        if (match != None):
            end = match.span()[1]
            sem = match.string[end + 1:] #+1 to remove -
            #Get note and duration
            match = re.search("_", sem)
            _pos = match.span()[0]
            note = match.string[0:_pos]
            duration = match.string[_pos:]
            #Insert to semArray
            semArray.append([note, duration])
        #REST
        else:
            match = re.match(r"^rest", sem)
            if (match != None):
                end = match.span()[1]
                sem = match.string[end + 1:] #+1 to remove -
                #Get duration and insert to semArray
                semArray.append(["rest", sem])
    #semantic array has format [[note, duration], [note, duration]] where note = rest if rest
    #for p in semArray:






    semantics.close()


    return stream
    

#get semantic data
convert("../converter/sheets/sw.png")
stream = translate()

#translate semantic data into music21 streams
#stream = m.stream.Stream()



#saves music21 stream as midi file
#stream.write('midi', fp=MIDI_SAVE_PATH + MIDI_SAVE_NAME)

#play saved midifile
#play_midi(MIDI_SAVE_PATH + MIDI_SAVE_NAME)

