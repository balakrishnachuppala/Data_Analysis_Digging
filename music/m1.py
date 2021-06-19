#https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/#:~:text=WaveNet%20is%20a%20Deep%20Learning,original%20distribution%20of%20the%20data.&text=Similar%20to%20a%20language%20model,to%20predict%20the%20next%20sample.
from music21 import *
import os

#Array Processing
import numpy as np

# defining function to read MIDI files
def read_midi(file):
    print("Loading Music File:", file)

    notes = []
    notes_to_parse = None

    # parsing a midi file
    midi = converter.parse(file)

    # grouping based on different instruments
    s2 = instrument.partitionByInstrument(midi)

    # Looping over all the instruments
    for part in s2.parts:

        # select elements of only piano
        if 'Piano' in str(part):

            notes_to_parse = part.recurse()

            # finding whether a particular element is note or a chord
            for element in notes_to_parse:

                # note
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))

                # chord
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)

