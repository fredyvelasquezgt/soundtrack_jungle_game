from music import *

# Melodía principal extendida
pitches_main_melody = [C5, E5, G5, C6, G5, E5, C5, G5, E5, C5, E5, G5, C6, G5, E5, C5]
durations_main_melody = [QN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN, HN]

# Variación en la armonía
pitches_harmony = [C4, E4, G4, C5, G4, E4, C4, C4, G4, C4, E4, G4, C5, G4, E4, C4]
durations_harmony = [HN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN, HN]

# Ritmo de tambores de selva, con patrón variado
jungle_drums_pitches = [
    C2, REST, C2, REST, E2, G2, C2, REST, G2, E2, REST, C2, C2, E2, REST, G2,
    C2, REST, C2, E2, REST, G2, E2, REST, G2, C2, REST, C2, G2, E2, C2, G2
]
jungle_drums_durations = [
    SN, SN, SN, SN, QN, QN, SN, SN, QN, QN, SN, QN, QN, QN, SN, QN,
    SN, SN, SN, QN, SN, QN, QN, SN, QN, SN, SN, QN, QN, SN, QN, HN
]

# Acompañamiento adicional con más variaciones
accompaniment_pitches = [A4, E5, D5, REST, F5, C5, A4, A4, E5, D5, REST, F5, C5, A4]
accompaniment_durations = [QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, QN, QN, QN, HN]

# Crear frases extendidas para la melodía principal, armonía, tambores y acompañamiento
melody = Phrase()
melody.addNoteList(pitches_main_melody, durations_main_melody)
melody.addNoteList(pitches_main_melody, durations_main_melody)  # Repetimos la melodía para extenderla

harmony = Phrase()
harmony.addNoteList(pitches_harmony, durations_harmony)
harmony.addNoteList(pitches_harmony, durations_harmony)  # Repetimos la armonía también

# Crear frase para los tambores de selva
jungle_drums = Phrase()
jungle_drums.addNoteList(jungle_drums_pitches, jungle_drums_durations)
jungle_drums.addNoteList(jungle_drums_pitches, jungle_drums_durations)  # Repetimos el patrón de tambores

accompaniment = Phrase()
accompaniment.addNoteList(accompaniment_pitches, accompaniment_durations)
accompaniment.addNoteList(accompaniment_pitches, accompaniment_durations)  # Repetimos el acompañamiento

# Crear la partitura y agregar las frases
score = Score("Música de Aventura en la Selva Extendida", 120)  # BPM ajustado a 120 para el ritmo de aventura
score.addPart(Part(melody))
score.addPart(Part(harmony))
score.addPart(Part(jungle_drums))
score.addPart(Part(accompaniment))

# Guardar la partitura en un archivo MIDI
Write.midi(score, "tema_principal.mid")

# Reproducir la música extendida con ambiente de selva
Play.midi(score)
