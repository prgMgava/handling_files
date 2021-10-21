import os
import dotenv

dotenv.load_dotenv()

VIDEOS_DIRECTORY = os.environ.get('VIDEOS_DIRECTORY')

if not os.path.isdir(VIDEOS_DIRECTORY):
    os.mkdir(VIDEOS_DIRECTORY)