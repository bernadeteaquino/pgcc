import os
from flask_restful import Resource, request
from resources.util.video_to_audio import extract_audio
from resources.util.detect_speech import detect_speech
from resources.util.cloud_storage import upload

class SpeechToText(Resource):
    def get(self):
        if request.files:
            file = request.files['file']
            content_type = file.content_type
            if content_type == "video/mp4":
                file_path = "files/"+file.filename
                file.save(file_path)
                print("hei---------------m")
                extracted_audio_file = extract_audio(file_path)
                extracted_json_file = detect_speech(extracted_audio_file)
                uploaded_file_name = upload(extracted_json_file)
                os.remove(file_path)
                os.remove(extracted_audio_file)
                os.remove(extracted_json_file)
                return uploaded_file_name,200
            else:
                return "Unsupported format!",400
        else:
            return "File required!", 400
