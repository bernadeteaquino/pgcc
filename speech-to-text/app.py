from flask import Flask
from flask_restful import Api
from resources.speech_to_text import SpeechToText

app = Flask(__name__)
api = Api(app)

api.add_resource(SpeechToText, "/speech-to-text")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
