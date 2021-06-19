from m2_read_MIDI import *
#importing library
from collections import Counter
print('Counter : \n',Counter(notes_))
#computing frequency of each note
freq = dict(Counter(notes_))

print('Freq : \n',freq)

#library for visualiation
import matplotlib.pyplot as plt

#consider only the frequencies
no=[count for _,count in freq.items()]

#set the figure size
plt.figure(figsize=(5,5))
print(no)
#plot
plt.hist(no)

frequent_notes = [note_ for note_, count in freq.items() if count>=50]
print('>50 very frequent notes: ', len(frequent_notes))
