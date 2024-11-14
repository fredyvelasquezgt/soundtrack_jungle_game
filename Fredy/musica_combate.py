from music import *

# Melodía principal tensa para el combate
pitches_combat_melody = [
    E5, D5, E5, G5, F5, REST, E5, D5, E5, C5, REST, E5, D5, G5, F5, E5
]
durations_combat_melody = [
    EN, EN, SN, SN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, EN, EN
]

# Cuerdas rápidas en fondo para intensificar la atmósfera
pitches_combat_strings = [
    C4, E4, G4, REST, D4, F4, A4, REST, E4, G4, B4, REST, F4, A4, C5
]
durations_combat_strings = [
    SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN
]

# Bajo de percusión constante y dramático
pitches_combat_bass = [E2, G2, E2, G2, F2, E2, G2, F2, E2, G2, F2, E2]
durations_combat_bass = [QN, QN, QN, QN, EN, EN, QN, QN, QN, QN, EN, EN]

# Tambores de ritmo rápido para crear tensión
pitches_combat_drums = [
    C2, REST, C2, C2, REST, C2, C2, REST, C2, C2, REST, C2, C2, C2, C2, REST
]
durations_combat_drums = [
    SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, SN
]

# Melodía de cuerdas adicionales para acentuar el drama
pitches_combat_strings_high = [
    A4, E5, G5, F5, E5, G5, A5, G5, E5, D5, E5, G5, F5, D5, E5
]
durations_combat_strings_high = [
    SN, SN, SN, SN, EN, EN, SN, SN, EN, EN, SN, SN, EN, EN, QN
]

# Crear frases para cada parte
combat_melody = Phrase()
combat_melody.addNoteList(pitches_combat_melody, durations_combat_melody)

combat_strings = Phrase()
combat_strings.addNoteList(pitches_combat_strings, durations_combat_strings)

combat_bass = Phrase()
combat_bass.addNoteList(pitches_combat_bass, durations_combat_bass)

combat_drums = Phrase()
combat_drums.addNoteList(pitches_combat_drums, durations_combat_drums)

combat_strings_high = Phrase()
combat_strings_high.addNoteList(pitches_combat_strings_high, durations_combat_strings_high)

# Crear la partitura y agregar las frases
combat_score = Score("Música de Combate Tensa y Dramática", 130)  # BPM elevado para mayor intensidad
combat_score.addPart(Part(combat_melody))
combat_score.addPart(Part(combat_strings))
combat_score.addPart(Part(combat_bass))
combat_score.addPart(Part(combat_drums))
combat_score.addPart(Part(combat_strings_high))

# Guardar la música de combate en un archivo MIDI
Write.midi(combat_score, "musica_combate_rapida_tensa.mid")

# Reproducir la música de combate
Play.midi(combat_score)
