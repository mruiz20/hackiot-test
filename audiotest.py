import pyaudio
import wave

print("1")
FORMAT = pyaudio.paInt16
print("1")
CHANNELS = 1           # Number of channels
print("1")
BITRATE = 44100        # Audio Bitrate
print("1")
CHUNK_SIZE = 512       # Chunk size to 
print("1")
RECORDING_LENGTH = 10  # Recording Length in seconds
print("1")
WAVE_OUTPUT_FILENAME = "myrecording.wav"
print("1")
audio = pyaudio.PyAudio()

info = audio.get_host_api_info_by_index(0)
print("1")
numdevices = info.get('deviceCount')
print("1")
for i in range(0, numdevices):
    if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

print("Which Input Device would you like to use?")
device_id = int(input()) # Choose a device
print("Recording using Input Device ID "+str(device_id))

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=BITRATE,
    input=True,
    input_device_index = device_id,
    frames_per_buffer=CHUNK_SIZE
)

recording_frames = []

for i in range(int(BITRATE / CHUNK_SIZE * RECORDING_LENGTH)):
    data = stream.read(CHUNK_SIZE)
    recording_frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(BITRATE)
waveFile.writeframes(b''.join(recording_frames))
waveFile.close()