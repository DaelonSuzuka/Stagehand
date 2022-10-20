import mido

print('midi')

print(mido.get_input_names())
print(mido.get_output_names())

with mido.open_output('test 1') as outport:
    outport.send(mido.Message('note_on'))
    # for message in inport:
    #     print(message)