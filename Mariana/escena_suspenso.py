# Melodía de Suspenso
pitches_suspense_melody = [C5, REST, C5, D5, REST, E5, D5, C5, D5, REST, C5, REST, E5, D5]
durations_suspense_melody = [QN, SN, QN, SN, QN, QN, SN, QN, SN, QN, QN, SN, QN, SN]

# Armonía de suspenso
pitches_suspense_harmony = [G3, REST, A3, C4, REST, G3, REST, A3, C4, REST, G3, REST, A3]
durations_suspense_harmony = [HN, SN, QN, HN, QN, QN, SN, QN, QN, HN, QN, QN, SN]

# Tambores para escenas de tensión
suspense_drums_pitches = [C2, E2, REST, C2, REST, E2, G2, REST, C2, REST, G2, REST, E2]
suspense_drums_durations = [QN, SN, QN, QN, HN, QN, QN, HN, QN, HN, QN, SN, QN]

melody_suspense = Phrase()
melody_suspense.addNoteList(pitches_suspense_melody, durations_suspense_melody)

harmony_suspense = Phrase()
harmony_suspense.addNoteList(pitches_suspense_harmony, durations_suspense_harmony)

drums_suspense = Phrase()
drums_suspense.addNoteList(suspense_drums_pitches, suspense_drums_durations)

score_suspense = Score("Tema de Suspenso", 100)
score_suspense.addPart(Part(melody_suspense))
score_suspense.addPart(Part(harmony_suspense))
score_suspense.addPart(Part(drums_suspense))

Write.midi(score_suspense, "tema_suspenso.mid")
Play.midi(score_suspense)
