import ffmpeg
from ffmpeg import Error

def extract_audio(file_name):
    extracted_file_name = file_name[:-3] + 'wav'
    try:

        out, err = (
            ffmpeg
            .input(file_name)
            .output(extracted_file_name, ac=1, ar='16k')
            .run(quiet=False,capture_stdout=True, capture_stderr=True)
        )
        return extracted_file_name
    except ffmpeg.Error as err:
        # TODO
        print(err.stderr)
        raise