from music import *

# Melodía principal, extendida para aumentar la emoción y expectativa
pitches_tension_melody = [
    D4, REST, E4, F4, REST, G4, E4, REST, D4, REST, C4, D4, REST, F4,
    G4, F4, E4, REST, D4, E4, F4, REST, G4, A4, G4, F4, E4, REST, D4
]
durations_tension_melody = [
    QN, EN, QN, EN, QN, QN, EN, EN, QN, EN, QN, EN, QN, HN,
    QN, EN, QN, EN, QN, QN, EN, EN, QN, EN, QN, EN, QN, QN, HN
]

# Acordes extendidos y dinámicos para añadir profundidad y emoción
pitches_tension_chords = [
    D3, F3, A3, REST, E3, G3, B3, REST, C3, E3, G3, REST, D3, F3, A3,
    G3, B3, D4, REST, A3, C4, F3, REST, G3, D4, C4
]
durations_tension_chords = [
    HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN,
    QN, QN, HN, EN, QN, QN, HN, EN, QN, QN, HN
]

pitches_tension_bass = [
    D2, E2, F2, G2, A2, REST, G2, F2, E2, D2, C2, REST, D2, G2, E2, D2
]
durations_tension_bass = [
    QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, HN, QN, EN, HN
]

pitches_tension_drums = [
    C2, REST, C2, REST, C2, C2, REST, C2, REST, C2, REST, C2,
    C2, REST, C2, C2, REST, C2, C2, C2, REST, C2, REST, C2
]
durations_tension_drums = [
    SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN,
    QN, EN, QN, QN, EN, QN, SN, SN, QN, SN, EN, HN
]

pitches_tension_strings = [
    F4, E4, D4, REST, C4, E4, REST, G4, REST, F4, E4, D4, REST, C4, E4,
    G4, REST, F4, E4, G4, A4, REST, F4, E4, G4, REST, D4, E4, C4
]
durations_tension_strings = [
    EN, QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, EN, QN,
    QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, QN, HN
]

tension_melody = Phrase()
tension_melody.addNoteList(pitches_tension_melody, durations_tension_melody)

tension_chords = Phrase()
tension_chords.addNoteList(pitches_tension_chords, durations_tension_chords)

tension_bass = Phrase()
tension_bass.addNoteList(pitches_tension_bass, durations_tension_bass)

tension_drums = Phrase()
tension_drums.addNoteList(pitches_tension_drums, durations_tension_drums)

tension_strings = Phrase()
tension_strings.addNoteList(pitches_tension_strings, durations_tension_strings)

tension_score = Score("Preparación", 125)  
tension_score.addPart(Part(tension_melody))
tension_score.addPart(Part(tension_chords))
tension_score.addPart(Part(tension_bass))
tension_score.addPart(Part(tension_drums))
tension_score.addPart(Part(tension_strings))

Write.midi(tension_score, "tema_tension_preparacion_extendido.mid")

Play.midi(tension_score)
