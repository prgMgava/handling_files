from flask import Flask, jsonify, request, send_file
from modules.videos import utils

app = Flask(__name__)

@app.get('/')
def videos_list():
    list_all_videos = utils.get_list_of_videos()
    return jsonify(list_all_videos)


@app.post('/')
def upload():
    list_file = []

    for file in request.files:
        filename = utils.save_video(request.files[file])
        list_file.append(filename)

    return jsonify(list_file)

@app.get('/download/<string:filename>')
def dowload(filename):
    path = utils.get_path(filename)
    if request.args.get('format'):
        path = utils.converter_video(filename, request.args.get('format'))
        send_file(path, as_attachment=True)
    return send_file(path, as_attachment=True)

@app.get('/play/<string:filename>')
def play_video(filename):
    path = utils.get_path(filename)
    return send_file(path) 

