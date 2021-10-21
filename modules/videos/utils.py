import os
from . import VIDEOS_DIRECTORY
from flask.helpers import safe_join
from werkzeug.datastructures import FileStorage
from datetime import datetime, timezone
from werkzeug.utils import secure_filename


from datetime import datetime

def get_list_of_videos():
    _,_,filenames = list(os.walk(VIDEOS_DIRECTORY))[0]
    return filenames

def save_video(file :FileStorage):
    file_extension = file.filename.split('.')[-1]
    filename = secure_filename(str(datetime.now(timezone.utc))[:26])
    filename = f'{filename}.{file_extension}'
    path = safe_join(VIDEOS_DIRECTORY,filename)
    file.save(path)

    return filename

def get_path(filename :str):
    path = safe_join(VIDEOS_DIRECTORY,filename)
    return path 


def converter_video(filename:str, format:str):
    print(filename,format)
    path = get_path(filename)
    output_path = f'/tmp/{filename.split(".")[0]}.{format}'
    os.system(f'ffmpeg -i {path} {output_path}')
    return output_path

