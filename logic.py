import const

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
        elif note in const.equinotes and const.equinotes[note] in s_key:
            alt = const.equinotes[note]
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
            tmp_idx_i = const.intervals.index(tmp_idx_d)
            # get the note, in the intervals list, which is at the index of the converted closest note + distance between original closest note and actual note
            add = (const.intervals[(tmp_idx_i + distance) % len(const.intervals)])
        d_notes.append(add)
    return d_notes

# find closest note to another note
def find_closest_note(target, scale):
    target_midi = const.note_to_midi[target]
    closest_note = min(scale, key=lambda n: abs(const.note_to_midi[n] - target_midi))
    return closest_note

# returns a value negative or positive depending on which direction the distance is
def index_distance(note, closest_note):
    note = standardise_for_interval(note)
    closest_note = standardise_for_interval(closest_note)
    idx1 = const.intervals.index(note)
    idx2 = const.intervals.index(closest_note)
    distance = idx1 - idx2 
    return distance 

# Be able to find a note in intervals constant
def standardise_for_interval(note):
    if 'b' in note:
        note = const.equinotes[note]
    return note