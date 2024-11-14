from music import *

pitches_romance_melody = [
    G4, REST, A4, B4, REST, C5, B4, A4, G4, REST, F4, G4, REST, E4, D4,
    C5, D5, E5, REST, F5, E5, D5, C5, REST, B4, C5, REST, A4, G4, F4
]
durations_romance_melody = [
    QN, EN, QN, EN, QN, QN, EN, EN, QN, EN, QN, EN, QN, QN, HN,
    QN, QN, HN, EN, QN, EN, QN, EN, QN, EN, QN, QN, QN, QN, HN
]

pitches_romance_chords = [
    C4, E4, G4, REST, D4, F4, A4, REST, E4, G4, B4, REST, C4, E4, G4,
    F4, A4, C5, REST, G4, B4, D5, REST, C4, E4, G4, REST, D4, F4, A4
]
durations_romance_chords = [
    HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN,
    QN, QN, HN, EN, QN, EN, HN, EN, HN, QN, EN, EN, HN, QN, HN
]

pitches_romance_bass = [
    C3, E3, G3, REST, F3, A3, C4, REST, G3, B3, C4, REST, D3, E3, F3,
    A3, C4, E4, REST, G3, B3, D4, REST, F3, A3, C4, REST, E3, G3, C3
]
durations_romance_bass = [
    HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN,
    QN, QN, HN, QN, QN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN
]

pitches_romance_arpeggio = [
    E4, G4, C5, REST, F4, A4, C5, REST, D4, F4, A4, REST, G4, B4, D5,
    C5, E5, G5, REST, A4, C5, E5, REST, F4, A4, C5, REST, E4, G4, C5
]
durations_romance_arpeggio = [
    EN, EN, QN, EN, EN, EN, QN, EN, EN, EN, QN, EN, EN, EN, HN,
    QN, EN, QN, EN, EN, QN, EN, QN, EN, EN, QN, EN, EN, QN, HN
]

romance_melody = Phrase()
romance_melody.addNoteList(pitches_romance_melody, durations_romance_melody)

romance_chords = Phrase()
romance_chords.addNoteList(pitches_romance_chords, durations_romance_chords)

romance_bass = Phrase()
romance_bass.addNoteList(pitches_romance_bass, durations_romance_bass)

romance_arpeggio = Phrase()
romance_arpeggio.addNoteList(pitches_romance_arpeggio, durations_romance_arpeggio)

romance_score = Score("Romance o Interacción", 60)
romance_score.addPart(Part(romance_melody))
romance_score.addPart(Part(romance_chords))
romance_score.addPart(Part(romance_bass))
romance_score.addPart(Part(romance_arpeggio))

Write.midi(romance_score, "RomanceInteraccion.mid")
Play.midi(romance_score)
