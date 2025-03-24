import csv
import sys

#Check csv file input
def is_not_csv(file):
    return not file.lower().endswith('.csv')

if len(sys.argv) != 2 or is_not_csv(sys.argv[1]):
    print("Usage: python script.py file.csv")
    sys.exit(1)
file = sys.argv[1]  

# Constants
note_to_midi = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5,
    "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11
}

intervals = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
## intervals_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

scales = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "Am": ["A", "B", "C", "D", "E", "F", "G"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "Em": ["E", "F#", "G", "A", "B", "C", "D"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "Bm": ["B", "C#", "D", "E", "F#", "G", "A"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "F#m": ["F#", "G#", "A", "B", "C#", "D", "E"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "C#m": ["C#", "D#", "E", "F#", "G#", "A", "B"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "G#m": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    "D#m": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "A#m": ["A#", "B#", "C#", "D#", "E#", "F#", "G#"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E"],
    "Dm": ["D", "E", "F", "G", "A", "Bb", "C"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "Gm": ["G", "A", "Bb", "C", "D", "Eb", "F"],
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Cm": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Fm": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "Bbm": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
    "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "Ebm": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"],
    "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
    "Abm": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"]
}

equinotes = {
    "C#": "Db", "Db": "C#",
    "D#": "Eb", "Eb": "D#",
    "F#": "Gb", "Gb": "F#",
    "G#": "Ab", "Ab": "G#",
    "A#": "Bb", "Bb": "A#",
    "B#": "C", "C": "B#",
    "E#": "F", "F": "E#",
    "Cb": "B", "B": "Cb",
    "Fb": "E", "E": "Fb"
}

# Parse my file
def parse(row):
    s_key = scales[row['source']]
    d_key = scales[row['dest']]
    ls_notes = row['l_notes'].split(" ")
    rs_notes = row['r_notes'].split(" ")
    return s_key, d_key, ls_notes, rs_notes

#Main Logic
def transpose(s_key, d_key, s_notes):
    d_notes = []
    #print(s_key)
    for note in s_notes:
        # if note in scale, just get the note at same index in other scale
        if note in s_key:
            tmp_idx = s_key.index(note)
            add = d_key[tmp_idx]
        # if note is not in scale, check if the other name for the note is in scale
        elif note in equinotes and equinotes[note] in s_key:
            alt = equinotes[note]
            tmp_idx = s_key.index(alt)
            add = d_key[tmp_idx]
        # if note is definitely not in scale
        else:
            # get the closest note in the source scale
            closest_note = find_closest_note(note, s_key)
            # calculate the distance between the closest note and the actual note
            distance = index_distance(note, closest_note)
            # get the position of the closest note in the source scale
            tmp_idx_s = s_key.index(closest_note)
            # get the note at the same index for the destination scale
            tmp_idx_d = d_key[tmp_idx_s]
            # make sure that it is not a flat, otherwise convert to # to match our interval list
            tmp_idx_d = standardise_for_interval(tmp_idx_d)
            # get the index of the target in the intervals scale
            tmp_idx_i = intervals.index(tmp_idx_d)
            # get the note, in the intervals list, which is at the index of the converted closest note + distance between original closest note and actual note
            add = (intervals[(tmp_idx_i + distance) % len(intervals)])
        d_notes.append(add)
    return d_notes

# find closest note to another note
def find_closest_note(target, scale):
    target_midi = note_to_midi[target]
    closest_note = min(scale, key=lambda n: abs(note_to_midi[n] - target_midi))
    return closest_note

# returns a value negative or positive depending on which direction the distance is
def index_distance(note, closest_note):
    note = standardise_for_interval(note)
    closest_note = standardise_for_interval(closest_note)
    idx1 = intervals.index(note)
    idx2 = intervals.index(closest_note)
    distance = idx1 - idx2 
    return distance 

# Be able to find a note in intervals constant
def standardise_for_interval(note):
    if 'b' in note:
        note = equinotes[note]
    return note

# open file
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['source'] not in note_to_midi:
            print(row['source'], row['dest'] if row.get('dest') else "")
            continue
        s_key, d_key, ls_notes, rs_notes = parse(row)
        ld_notes = transpose(s_key, d_key, ls_notes)
        rd_notes = transpose(s_key, d_key, rs_notes)
        print("\033[34m" + " ".join(ld_notes) + "\033[0m")
        print("\t\033[31m" + " ".join(rd_notes) + "\033[0m")

