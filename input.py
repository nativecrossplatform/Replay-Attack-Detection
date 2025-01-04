import sounddevice as sd
import numpy as np
import io
def record_audio_to_bytes(duration=5, samplerate=44100, channels=1): 
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()  # Ensure the recording is complete
    # Convert the raw audio data to bytes for database storage
    # the given line below ensures that a binary stream is created, a binary stream is allows user to write binary like they would write in a file, but the difference is this is completly in the memory
    byte_buffer = io.BytesIO()
    # write the raw audio data which is in numpy array form into the stream in binary format
    byte_buffer.write(audio.tobytes())
    # retrieves the in-memory byte buffer as byte object
    audio_bytes = byte_buffer.getvalue()
    # we could have used file for storage but the long term plan for database integration made it seem reasonable to go for byte object so as to have complete ease while storing it to db
    return audio_bytes, samplerate