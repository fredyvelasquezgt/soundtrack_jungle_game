from music import *

pitches_exploration_melody = [
    C5, E5, G5, REST, D5, F5, A5, REST, E5, G5, C6, REST, G5, F5, D5,
    C5, REST, E5, G5, C6, E5, D5, REST, C5
]
durations_exploration_melody = [
    QN, EN, QN, EN, QN, EN, QN, EN, QN, EN, HN, EN, QN, EN, HN,
    QN, EN, QN, QN, HN, QN, QN, EN, HN
]

pitches_exploration_chords = [
    C4, G4, E4, REST, F4, A4, C5, REST, D4, G4, B4, REST, G4, F4, E4,
    A3, C4, F4, REST, G3, C4, E4, REST, F4, A4, C5
]
durations_exploration_chords = [
    HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN,
    HN, QN, HN, EN, HN, QN, HN, EN, HN, QN, HN
]

pitches_exploration_bass = [
    C3, G3, C4, REST, F3, C4, F4, REST, G3, D4, G4,
    E3, REST, C3, A2, G2, REST, F3, D3, E3, REST, G3, C4
]
durations_exploration_bass = [
    QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN,
    HN, EN, QN, QN, QN, QN, QN, QN, QN, QN, HN, HN
]

pitches_exploration_arpeggio = [
    E4, G4, C5, REST, F4, A4, C5, REST, D4, F4, A4, REST, G4, B4, D5,
    E4, REST, G4, C5, E5, G5, C6, REST, E4, D5
]
durations_exploration_arpeggio = [
    EN, EN, QN, EN, EN, EN, QN, EN, EN, EN, QN, EN, EN, EN, HN,
    QN, EN, QN, QN, HN, EN, QN, EN, HN, EN
]

pitches_ambient_wind = [
    G2, REST, E2, REST, C2, REST, D2, REST, G2
]
durations_ambient_wind = [
    WN, HN, WN, HN, WN, HN, WN, HN, WN
]

pitches_ambient_birds = [
    C6, REST, E6, G6, REST, A6, E6, REST, C6, G5, REST, D6
]
durations_ambient_birds = [
    SN, EN, SN, EN, QN, QN, EN, EN, QN, SN, EN, HN
]

exploration_melody = Phrase()
exploration_melody.addNoteList(pitches_exploration_melody, durations_exploration_melody)

exploration_chords = Phrase()
exploration_chords.addNoteList(pitches_exploration_chords, durations_exploration_chords)

exploration_bass = Phrase()
exploration_bass.addNoteList(pitches_exploration_bass, durations_exploration_bass)

exploration_arpeggio = Phrase()
exploration_arpeggio.addNoteList(pitches_exploration_arpeggio, durations_exploration_arpeggio)

ambient_wind = Phrase()
ambient_wind.addNoteList(pitches_ambient_wind, durations_ambient_wind)

ambient_birds = Phrase()
ambient_birds.addNoteList(pitches_ambient_birds, durations_ambient_birds)

exploration_valley_score = Score("Exploración", 70)  
exploration_valley_score.addPart(Part(exploration_melody))
exploration_valley_score.addPart(Part(exploration_chords))
exploration_valley_score.addPart(Part(exploration_bass))
exploration_valley_score.addPart(Part(exploration_arpeggio))
exploration_valley_score.addPart(Part(ambient_wind))   
exploration_valley_score.addPart(Part(ambient_birds)) 

Write.midi(exploration_valley_score, "tema_exploracion.mid")

Play.midi(exploration_valley_score)
