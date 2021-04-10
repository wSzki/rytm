import mido
from mido import Message
msg = Message('note_on', note=60)
print(msg)

name = mido.get_input_names()
print(name)

inport  = mido.open_input(name[0])
print(inport)
msg = inport.receive()
for msg in inport:
    print(msg)
print(msg)
