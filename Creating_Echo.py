import soundcard
import numpy as np
speaker = soundcard.default_speaker()
block_size = 1024
samplerate = 44100
frequency = 440


def generate_block(block_size, phase_offset, frequency, samplerate):
    time = np.arange(0, block_size) / samplerate
    output_buffer = np.sin(2*np.pi*frequency*time + phase_offset)
    next_phase_offset = 2*np.pi*frequency*block_size/samplerate + phase_offset
    return output_buffer, next_phase_offset



delay_buffer = list(np.zeros(40))
phase_offset = 0
with speaker.player(samplerate=samplerate, channels=1, blocksize=block_size) as player:
    while True:
        
        sensor_value = 40
        delay_buffer.pop(0)
        frequency += 0.5
        output_buffer, phase_offset = generate_block(block_size, phase_offset, frequency, samplerate)
        delay_buffer.append(output_buffer)    #append the new buffer to our delay buffer 
        #player.play(output_buffer)
        print(delay_buffer[0]) #this is a block
        
        volume = 0.25
        #echo is the superimposed signal with the older buffers
        echo = volume*(delay_buffer[-sensor_value] + delay_buffer[-int(sensor_value/2)] + delay_buffer[-int(sensor_value/4)] + delay_buffer[-int(sensor_value/8)])
            

        new_output = 0.5*(delay_buffer[-1] + echo)
        
        print(new_output)
        #player.play(output_buffer)
        player.play(new_output)

        
