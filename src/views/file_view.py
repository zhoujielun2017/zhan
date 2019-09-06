import os
import os
import time

import shortuuid
from flasgger import swag_from
from flask import Blueprint, render_template, request, jsonify

from model.result import Result

file = Blueprint('file', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'bmp', 'BMP'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@file.route('/images', methods=['GET'], strict_slashes=False)
@swag_from("yml/file_view_images_upload.yml")
def upload_view():
    return render_template("product/upload.html")


@file.route('/images', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join("/data", "upload")
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']
    if f and allowed_file(f.filename):
        ext = f.filename.rsplit('.', 1)[1]
        if ext in ALLOWED_EXTENSIONS:
            new_filename = str(int(time.time())) + '_' + shortuuid.uuid()[:8] + ".jpg"
            print(new_filename)
            f.save(os.path.join(file_dir, new_filename))
            return jsonify(Result().success(new_filename))
    return jsonify(Result().fail())


