import sounddevice as sd
import numpy as np
import io

def record_audio_to_bytes(duration=5, samplerate=44100, channels=1): 
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()  # Ensure the recording is complete
    # Convert the raw audio data to bytes for database storage
    byte_buffer = io.BytesIO()
    byte_buffer.write(audio.tobytes())
    audio_bytes = byte_buffer.getvalue()
    return audio_bytes, samplerate