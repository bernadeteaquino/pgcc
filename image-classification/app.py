from flask import Flask
from flask_restful import Api
from resources.image_classification import ImageClassification

app = Flask(__name__)
api = Api(app)

api.add_resource(ImageClassification, "/image-classification")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)