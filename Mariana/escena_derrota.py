from music import *

# Melodía de Derrota
pitches_defeat_melody = [E4, D4, C4, REST, C4, D4, REST, C4, D4, E4, REST, E4, D4, C4]
durations_defeat_melody = [HN, QN, QN, QN, HN, QN, QN, HN, QN, QN, HN, QN, QN, HN]

# Armonía triste con acordes menores
pitches_defeat_harmony = [A3, C4, D4, E4, C4, D4, C4, A3, C4, D4, REST, A3, C4, D4]
durations_defeat_harmony = [QN, HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN]

# Tambores de selva en ritmo lento para derrota
defeat_drums_pitches = [C2, REST, REST, E2, REST, C2, REST, G2, REST, E2, C2, REST]
defeat_drums_durations = [QN, HN, HN, QN, HN, QN, HN, QN, HN, QN, QN, HN]

melody_defeat = Phrase()
melody_defeat.addNoteList(pitches_defeat_melody, durations_defeat_melody)

harmony_defeat = Phrase()
harmony_defeat.addNoteList(pitches_defeat_harmony, durations_defeat_harmony)

drums_defeat = Phrase()
drums_defeat.addNoteList(defeat_drums_pitches, defeat_drums_durations)

score_defeat = Score("Tema de Derrota", 80)
score_defeat.addPart(Part(melody_defeat))
score_defeat.addPart(Part(harmony_defeat))
score_defeat.addPart(Part(drums_defeat))

Write.midi(score_defeat, "tema_derrota.mid")
Play.midi(score_defeat)
