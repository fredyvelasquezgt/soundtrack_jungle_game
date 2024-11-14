# Melodía de Resolución
pitches_resolution_melody = [C5, E5, G5, C6, G5, E5, REST, C5, E5, G5, C6, G5, E5]
durations_resolution_melody = [QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, QN, QN, QN]

# Armonía de resolución
pitches_resolution_harmony = [G4, C5, E5, G5, REST, C5, E5, G5, REST, C5, E5, G5]
durations_resolution_harmony = [HN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, HN]

# Tambores de selva más alegres
resolution_drums_pitches = [C2, E2, G2, REST, C2, E2, G2, REST, G2, E2, REST, C2]
resolution_drums_durations = [QN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN]

melody_resolution = Phrase()
melody_resolution.addNoteList(pitches_resolution_melody, durations_resolution_melody)

harmony_resolution = Phrase()
harmony_resolution.addNoteList(pitches_resolution_harmony, durations_resolution_harmony)

drums_resolution = Phrase()
drums_resolution.addNoteList(resolution_drums_pitches, resolution_drums_durations)

score_resolution = Score("Tema de Resolución Parcial", 90)
score_resolution.addPart(Part(melody_resolution))
score_resolution.addPart(Part(harmony_resolution))
score_resolution.addPart(Part(drums_resolution))

Write.midi(score_resolution, "tema_resolucion.mid")
Play.midi(score_resolution)
