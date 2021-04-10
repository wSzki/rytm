

import midi
from midi import MidiConnector


conn = MidiConnector('/dev/dmmidi1')
msg = conn.read()
msg
Message(ProgramChange(35), 2)
msg.channel
msg.type
msg.program_number
