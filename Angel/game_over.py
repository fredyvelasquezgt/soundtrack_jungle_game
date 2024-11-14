from music import *

pitches_game_over_melody = [E4, REST, D4, C4, REST, A3, B3, REST, E4, D4, C4, REST, G3]
durations_game_over_melody = [QN, EN, QN, EN, QN, HN, EN, EN, QN, EN, QN, EN, HN]

pitches_game_over_chords = [
    C3, G3, E4, REST, B3, F3, D4, REST, G3, E4, C4, REST, A3
]
durations_game_over_chords = [
    HN, QN, QN, EN, HN, QN, QN, EN, HN, QN, QN, EN, HN
]

pitches_game_over_bass = [C2, REST, B2, A2, G2, REST, F2, E2, D2, REST, C2]
durations_game_over_bass = [HN, QN, HN, QN, HN, QN, HN, QN, HN, QN, HN]

pitches_game_over_strings = [
    E4, D4, REST, C4, REST, B3, C4, REST, A3, G3, REST, F3, E3
]
durations_game_over_strings = [
    EN, QN, EN, QN, QN, EN, QN, EN, QN, EN, QN, QN, HN
]

game_over_melody = Phrase()
game_over_melody.addNoteList(pitches_game_over_melody, durations_game_over_melody)

game_over_chords = Phrase()
game_over_chords.addNoteList(pitches_game_over_chords, durations_game_over_chords)

game_over_bass = Phrase()
game_over_bass.addNoteList(pitches_game_over_bass, durations_game_over_bass)

game_over_strings = Phrase()
game_over_strings.addNoteList(pitches_game_over_strings, durations_game_over_strings)

game_over_score = Score("Game Over", 55) 
game_over_score.addPart(Part(game_over_melody))
game_over_score.addPart(Part(game_over_chords))
game_over_score.addPart(Part(game_over_bass))
game_over_score.addPart(Part(game_over_strings))

Write.midi(game_over_score, "tema_game_over_melancolico.mid")

Play.midi(game_over_score)
