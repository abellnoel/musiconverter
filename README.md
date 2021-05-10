## <b>Music Convertor</b>

A tool that facilitates easier music learning by converting sheet music into playable sound using computer vision. Uses a pre-trained optical music recognition model by Jorge Zaragoza and David Rizo. Utilizes the PrIMuS dataset for testing examples.


## <b>Project Goal</b>

The problem is that for many novice musicians it may be challenging to understand what phrases of music are supposed to sound like. Our project goal was to take a sample of sheet music and process that image into playable music. This can benefit any musician who wants an idea of what a piece of sheet music sounds like. Auditory learning is very important for learning how to play an instrument.


## <b>Approach</b>

We devised an algorithm that utilizes optical music recognition to read sheet music and extract the key features from the music like key signature, note length, and pitch. The algorithm takes these features to read the notes on the sheet music and creates a MIDI file that produces an audio file that can be played by the user. Our algorithm was implemented in Python using Py 3.6.7, TensorFlow, Numpy, Matplotlib, OpenCV, and music21.


## <b>Model Testing</b>
Using a data sample from the PrIMuS dataset the model yielded 97% accuracy. Let's look at a comparison between the actual and predicted assignments.
![image](https://user-images.githubusercontent.com/37620953/117707732-e7fc0580-b19c-11eb-8e2e-0aa0bbeb0ca1.png)

<b>Predicted: ['clef-G2', 'keySignature-DbM', 'timeSignature-4/4', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-Db5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-G5_eighth', 'note-F5_eighth', 'barline']</b>
<b>Actual:    ['clef-G2', 'keySignature-DbM', 'timeSignature-4/4', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-Db5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Gb5_eighth', 'note-F5_eighth', 'barline']</b>
<b>Accuracy: 38/39,  97.43589743589743%</b>


## <b>Improvement</b>
To contribute to this model, our group devised a semantic data to MIDI file converter that takes the semantic data that's extracted from the input image and converts it to a MIDI file. This was accomplished using the music21 python library. By specifying the sheet music's file path in the music21convertor.py script and running it a MIDI file will be outputted according to the information the model collected.
