import time
from google.cloud import storage

def upload(file_name):
    bucket_name = "pgcc-audio-text"
    destination = time.strftime("%Y%m%d-%H%M%S") + file_name[file_name.find('/')+1:]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination)

    blob.upload_from_filename(file_name)

    return destination