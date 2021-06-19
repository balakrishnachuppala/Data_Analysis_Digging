from m3_graph_notes import *

new_music = []

for notes in notes_array:
    temp = []
    for note_ in notes:
        if note_ in frequent_notes:
            temp.append(note_)
    new_music.append(temp)

new_music = np.array(new_music)

print('New music content: \n',new_music)