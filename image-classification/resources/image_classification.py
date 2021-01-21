import os
import json
import time
from google.cloud import storage
from flask_restful import Resource, request
from imageai.Detection import VideoObjectDetection

# https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/VIDEO.md

classification = {} 
def for_seconds(second_number, output_arrays, count_arrays, average_output_count):
    data = json.loads(json.dumps(average_output_count))
    for key, value in data.items():
        if not key in classification:
            classification[key] = {}

        dict_interno = classification[key]
        if not value in dict_interno:
            dict_interno[value] = []

        dict_interno[value].append(second_number)

def extract_interval(list): 
    list = sorted(set(list)) 
    range_start = previous_number = list[0] 

    for number in list[1:]: 
        if number == previous_number + 1: 
            previous_number = number 
        else: 
            yield [range_start, previous_number] 
            range_start = previous_number = number 
    yield [range_start, previous_number] 

def update_seconds(classification):
	for key, value in classification.items():
		for key_interno, value_interno in classification[key].items():
			interval = list(interval_extract(value_interno))
			classification[key][key_interno] = interval

def get_image_classification(file_path):
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(os.path.join("files/yolo.h5"))
    video_detector.loadModel()
    
    custom_objects = video_detector.CustomObjects(person=True, book=True, chair=True, tv=True, laptop=True, 
        mouse=True, remote=True, keyboard=True, dining_table= True)

    video_detector.detectCustomObjectsFromVideo(
        custom_objects=custom_objects,
        input_file_path=os.path.join(file_path),
        frames_per_second=20, 
        per_second_function=for_seconds,
        save_detected_video = False,
        minimum_percentage_probability=50)

    update_seconds(classification)
    return classification

def save_classification(file_name, classification):
    json_file_name = time.strftime("%Y%m%d-%H%M%S") + file_name[:file_name.find('.')+1] + "json"
    with open("files/" + json_file_name, 'w') as json_file:
        json.dump(classification, json_file)
    return json_file_name

def upload(json_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket("pgcc-image-classification")
    blob = bucket.blob(json_file_name)
    blob.upload_from_filename(file_name)

class ImageClassification(Resource):
    def get(self):
        if request.files:
            file = request.files['file']
            content_type = file.content_type
            forSeconds
            if content_type == "video/mp4":
                file_path = "files/"+file.filename
                file.save(file_path)

                classification = get_image_classification(file_path)
                json_file = save_classification(file.filename, classification)
                upload(json_file)

                os.remove(file_path)
                os.remove(json_file)
                return json_file, 200
            else:
                return "Unsupported format!",400
        else:
            return "File required!", 400
