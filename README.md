## <b>Music Converter</b>

A tool that facilitates easier music learning by converting sheet music into playable sound using computer vision. Uses a pre-trained optical music recognition model by Jorge Zaragoza and David Rizo. Utilizes the PrIMuS dataset for testing examples.


## <b>Project Goal</b>

The problem is that for many novice musicians it may be challenging to understand what phrases of music are supposed to sound like. Our project goal was to take a sample of sheet music and process that image into playable music. This can benefit any musician who wants an idea of what a piece of sheet music sounds like. Auditory learning is very important for learning how to play an instrument.


## <b>Approach</b>

We devised an algorithm that utilizes optical music recognition to read sheet music and extract the key features from the music like key signature, note length, and pitch. The algorithm takes these features to read the notes on the sheet music and creates a MIDI file that produces an audio file that can be played by the user. Our algorithm was implemented in Python using Py 3.6.7, TensorFlow, Numpy, Matplotlib, OpenCV, and music21.


## <b>Model Testing</b>
<b>Using a data sample from the PrIMuS dataset the model yielded 97% accuracy. Let's look at a comparison between the actual and predicted assignments.</b>

![image](https://user-images.githubusercontent.com/37620953/117707732-e7fc0580-b19c-11eb-8e2e-0aa0bbeb0ca1.png)

<sub><sup>Predicted: ['clef-G2', 'keySignature-DbM', 'timeSignature-4/4', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-Db5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-G5_eighth', 'note-F5_eighth', 'barline']</sub></sup>

<sub><sup>Actual:    ['clef-G2', 'keySignature-DbM', 'timeSignature-4/4', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'barline', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Eb5_eighth', 'note-Db5_eighth', 'note-Eb5_eighth', 'note-F5_eighth', 'note-Gb5_eighth', 'note-F5_eighth', 'barline']</sub></sup>

<b>Accuracy: 38/39,  97.43589743589743%</b>


## <b>Improvement</b>


<b>To contribute to this model, our group devised a semantic data to MIDI file converter that takes the semantic data that's extracted from the input image and converts it to a MIDI file. This was accomplished using the music21 python library. By specifying the sheet music's file path in the music21convertor.py script and running it a MIDI file will be outputted according to the information the model collected.</b>

![image](https://user-images.githubusercontent.com/37620953/117709788-5641c780-b19f-11eb-8602-72dfad095396.png)


## <b>References</b>

<b>
[1]  Ashrafh, Ahmed, et al. “Aashrafh/Mozart.” GitHub, GitHub, 14 Dec. 2020, Retrieved from https://github.com/aashrafh/Mozart.

[2]  Calvo-Zaragoza J, Rizo D. End-to-End Neural Optical Music Recognition of Monophonic Scores. Applied Sciences. 2018; 8(4):606. https://doi.org/10.3390/app8040606

GitHub Repo: https://github.com/OMR-Research/tf-end-to-end

[3]  Ebonko, Israel. “Play Sheet Music with Python, OpenCV, and an Optical Music Recognition Model.” Hearbeat, Fritz AI, 26 Aug. 2020, https://heartbeat.fritz.ai/play-sheet-music-with-python-opencv-and-an-optical-music-recognition-model-a55a3bea8fe.

[4]  Nyati, A. (2017). CadenCV: An Optical Music Recognition System With Audible Playback. Massachusetts Institute of Technology. Retrieved from https://firebasestorage.googleapis.com/v0/b/afika-nyati-website.appspot.com/o/design%2Fcadencv%2Fcadencv_afika_nyati.pdf?alt=media&token=a5aa2413-32c0-4bc7-8222-06342b822096

GitHub Repo: https://github.com/afikanyati/cadenCV. 

[5]  Rebelo, A., Fujinaga, I., Paszkiewicz, F., Marcal, A., Guedes, C., & Cardoso, J. (2012). Optical music recognition: state-of-the-art and open issues. International Journal of Multimedia Information Retrieval, 1(3), 173–190. https://doi.org/10.1007/s13735-012-0004-6

Hyperlink: https://uncc.primo.exlibrisgroup.com/permalink/01UNCC_INST/1rqb8fi/cdi_crossref_primary_10_1007_s13735_012_0004_6

[6]  Vo, Q., Vo, Q., Lee, G., Lee, G., Kim, S., Kim, S., Yang, H., & Yang, H. (2018). Recognition of Music Scores with Non-Linear Distortions in Mobile Devices. Multimedia Tools and Applications, 77(12), 15951–15969. https://doi.org/10.1007/s11042-017-5169-9

Hyperlink: https://uncc.primo.exlibrisgroup.com/permalink/01UNCC_INST/1rqb8fi/cdi_springer_primary_2017_11042_77_12_5169

[7]  https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

[8]  https://grfia.dlsi.ua.es/primus/

</b>

