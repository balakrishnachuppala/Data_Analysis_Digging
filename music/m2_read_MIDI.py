#for listing down the file names
from m1 import *
import os

#Array Processing
import numpy as np
#specify the path
path='schubert/'

#read all the filenames
files=[i for i in os.listdir(path) if i.endswith(".mid")]
print(files)
#reading each midi file
notes_array = np.array([read_midi(path+i) for i in files])
#converting 2D array into 1D array
notes_ = [element for note_ in notes_array for element in note_]
print('Total Notes: \n',notes_)
#No. of unique notes
unique_notes = list(set(notes_))
print('unique Notes: ',len(unique_notes))


