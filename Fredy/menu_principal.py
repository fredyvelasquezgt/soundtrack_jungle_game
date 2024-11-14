from music import *

# Melodía principal para un ambiente más alegre y aventurero
pitches_menu_melody = [G4, B4, C5, D5, REST, G4, C5, D5, E5, REST, G4, D5, C5, B4, A4, G4]
durations_menu_melody = [QN, QN, EN, EN, QN, QN, QN, QN, HN, QN, QN, QN, QN, EN, EN, HN]

# Acordes de acompañamiento que crean un fondo más alegre
pitches_menu_chords = [
    G3, B3, D4, REST, C4, E4, G4, REST, A3, C4, E4, REST, F3, A3, C4
]
durations_menu_chords = [
    HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN
]

# Acompañamiento de bajo con un ritmo de exploración dinámica
pitches_menu_bass = [G2, D3, E3, G2, C3, G3, F3, D3, E3, G3, A3, F3]
durations_menu_bass = [QN, QN, QN, QN, HN, QN, QN, QN, QN, QN, HN, QN]

# Crear frases para la melodía principal, acordes y acompañamiento de bajo
menu_melody = Phrase()
menu_melody.addNoteList(pitches_menu_melody, durations_menu_melody)

menu_chords = Phrase()
menu_chords.addNoteList(pitches_menu_chords, durations_menu_chords)

menu_bass = Phrase()
menu_bass.addNoteList(pitches_menu_bass, durations_menu_bass)

# Crear la partitura y agregar las frases
menu_score = Score("Música del Menú Inicial Alegre y Aventurera", 100)  # BPM ajustado a 100 para un ambiente más animado
menu_score.addPart(Part(menu_melody))
menu_score.addPart(Part(menu_chords))
menu_score.addPart(Part(menu_bass))

# Guardar la música del menú en un archivo MIDI
Write.midi(menu_score, "menu_inicial_alegre.mid")

# Reproducir la música del menú inicial
Play.midi(menu_score)

