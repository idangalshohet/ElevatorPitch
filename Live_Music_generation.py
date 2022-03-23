import soundcard
import numpy as np


speaker = soundcard.default_speaker()
block_size = 1024
samplerate = 44100
frequency = 100


def generate_block(block_size, phase_offset, frequency, samplerate):
    time = np.arange(0, block_size) / samplerate
    output_buffer = np.sin(2*np.pi*frequency*time + phase_offset)
    next_phase_offset = 2*np.pi*frequency*block_size/samplerate + phase_offset
    return output_buffer, next_phase_offset


phase_offset = 0
with speaker.player(samplerate=samplerate, channels=1, blocksize=block_size) as player:
    while True:
        frequency += 1
        output_buffer, phase_offset = generate_block(block_size, phase_offset, frequency, samplerate)
        player.play(output_buffer)

