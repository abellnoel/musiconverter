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

#translate semantic data into music21 streams
def translate():  
    semantics = open(dir_path + "/semantics/semantics.txt", "r")
    #load created semantic text file into array
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
            #turn b into - to match music21 notation
            note = re.sub("b", "-", note)
            #check for dotted notes
            duration = match.string[_pos + 1:]
            dot = re.search("\.", duration)
            if (dot != None):
                duration = duration[0:dot.span()[0] + 1] #remove anything after dot
                print(duration)
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
    stream = m.stream.Stream()
    for p in semArray:
        print("Attempting to stream using: " + p[0] + " and " + p[1])
        #Set note/rest 
        if (p[0] == "rest"):
            primitive = m.note.Rest()
        else:
            primitive = m.note.Note(p[0])
        #Define duration
        duration = p[1]
        if (p[1] in ["whole", "half", "quarter", "eighth", "sixteenth", "whole.", "half.", "quarter.", "eighth.", "sixteenth."]):
            finalDuration = 0
            hasDot = False
            dot = re.search("\.", duration)
            if (dot != None):
                duration = duration[0:dot.span()[0]] #remove dot
                hasDot = True
            #set base value
            if (duration == "whole"):
                finalDuration = 4.0
            elif (duration == "half"):
                finalDuration = 2.0
            elif (duration == "quarter"):
                finalDuration = 1.0
            elif (duration == "eighth"):
                finalDuration = 0.5
            elif (duration == "sixteenth"):
                finalDuration = 0.25
            else:
                print("Duration not supported")
                finalDuration = 1.0
            #add dot duration
            if (hasDot):
                finalDuration += finalDuration / 2
        primitive.quarterLength = finalDuration
        stream.append(primitive)
    semantics.close()

    return stream
    
#get semantic data
convert("../converter/sheets/tt.png")
stream = translate()

#saves music21 stream as midi file
stream.write('midi', fp=MIDI_SAVE_PATH + MIDI_SAVE_NAME)

#play saved midifile
play_midi(MIDI_SAVE_PATH + MIDI_SAVE_NAME)

