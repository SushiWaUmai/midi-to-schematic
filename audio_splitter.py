import pretty_midi
import copy
import sys

pitch_cutoff_list = [6, 30, 54, 78, 102, 126]
# pitch_cutoff_list = [for i in range(12) i * 12 + 6]

def split_midi(path):
	mid = pretty_midi.PrettyMIDI(path)
	result = copy.deepcopy(mid)
	result.instruments = []

	for i in range(len(pitch_cutoff_list) - 1):
		notes = copy.deepcopy(mid)
		add = 54 - pitch_cutoff_list[i]
		pitch_instrument = pretty_midi.Instrument(program=0)
				
		for instrument in notes.instruments:
			for note in instrument.notes:
				if pitch_cutoff_list[i] < note.pitch < pitch_cutoff_list[i+1]:
					note.pitch += add
					pitch_instrument.notes.append(note)

		result.instruments.append(pitch_instrument)

	return result

if __name__ == '__main__':
	split_midi(sys.argv[1])