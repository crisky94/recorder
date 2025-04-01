
from scipy.io.wavfile import write
import sounddevice as sd

# Sampling frequency
device = 2

freq = 44100


# Recording duration
duration = 5

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                samplerate=freq, channels=1 , device=device)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("grabacion3.wav", freq, recording)
print("Grabación guardada como 'grabacion.wav'.")
# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)

# Listar dispositivos de entrada y salida

# import sounddevice as sd

# # Listar dispositivos de entrada y salida
# print(sd.query_devices())
