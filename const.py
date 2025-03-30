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