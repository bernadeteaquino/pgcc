import io
import json
from google.cloud import speech
from google.protobuf.json_format import MessageToDict

def detect_speech(file_name):
    client = speech.SpeechClient()
    json_file_name = file_name[:-3] + 'json'

    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="pt_BR",
    )

    response = client.recognize(config=config, audio=audio)
    result_json = type(response).to_json(response)

    with open(json_file_name, 'w') as json_file:
        json.dump(result_json, json_file)

    return json_file_name

