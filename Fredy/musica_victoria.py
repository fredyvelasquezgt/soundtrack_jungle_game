from music import *

# Melodía triunfal principal
pitches_victory_melody = [
    C5, E5, G5, C6, G5, E5, C5, REST, E5, G5, C6, E5, G5, C6, REST
]
durations_victory_melody = [
    QN, QN, QN, HN, QN, QN, QN, EN, QN, QN, QN, QN, QN, HN, EN
]

# Acordes de fondo para dar sensación de plenitud y celebración
pitches_victory_chords = [
    C4, E4, G4, C5, G4, C4, E4, G4, C5, F4, A4, C5, G4, C4, E4, G4
]
durations_victory_chords = [
    HN, QN, QN, HN, QN, QN, HN, QN, HN, QN, QN, HN, QN, QN, HN, QN
]

# Bajo para agregar más cuerpo a la música de victoria
pitches_victory_bass = [
    C3, G3, C4, F3, C3, G3, C4, E3, F3, C3, G3, C3, F3, C3, G3, C4
]
durations_victory_bass = [
    QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, HN, QN
]

# Percusión rítmica y animada
pitches_victory_drums = [
    C2, REST, C2, REST, C2, G2, C2, C2, REST, G2, REST, C2, C2, G2, C2, C2
]
durations_victory_drums = [
    SN, SN, SN, SN, QN, QN, SN, SN, QN, QN, SN, QN, QN, QN, SN, QN
]

# Trompetas para resaltar el momento de victoria
pitches_victory_trumpets = [
    C5, E5, G5, C6, REST, G5, C6, E5, G5, REST, C6, G5, C5, E5, G5
]
durations_victory_trumpets = [
    QN, QN, QN, HN, EN, QN, QN, QN, QN, EN, HN, QN, QN, QN, HN
]

# Crear frases para cada parte de la música de victoria
victory_melody = Phrase()
victory_melody.addNoteList(pitches_victory_melody, durations_victory_melody)

victory_chords = Phrase()
victory_chords.addNoteList(pitches_victory_chords, durations_victory_chords)

victory_bass = Phrase()
victory_bass.addNoteList(pitches_victory_bass, durations_victory_bass)

victory_drums = Phrase()
victory_drums.addNoteList(pitches_victory_drums, durations_victory_drums)

victory_trumpets = Phrase()
victory_trumpets.addNoteList(pitches_victory_trumpets, durations_victory_trumpets)

# Crear la partitura y asignar los instrumentos
victory_score = Score("Música de Victoria", 140)  # BPM rápido para dar energía

# Asignar instrumentos MIDI
part_melody = Part(victory_melody)
part_melody.setInstrument(0)  # Piano

part_chords = Part(victory_chords)
part_chords.setInstrument(48)  # String Ensemble

part_bass = Part(victory_bass)
part_bass.setInstrument(32)  # Acoustic Bass

part_drums = Part(victory_drums)
part_drums.setInstrument(115)  # Woodblock for drums (alternative percussion)

part_trumpets = Part(victory_trumpets)
part_trumpets.setInstrument(56)  # Trumpet for triumphant sound

# Agregar cada parte al score
victory_score.addPart(part_melody)
victory_score.addPart(part_chords)
victory_score.addPart(part_bass)
victory_score.addPart(part_drums)
victory_score.addPart(part_trumpets)

# Guardar la música de victoria en un archivo MIDI
Write.midi(victory_score, "musica_victoria.mid")

# Reproducir la música de victoria
Play.midi(victory_score)

