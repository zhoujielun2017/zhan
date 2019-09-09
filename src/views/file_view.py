import datetime
import os
import os
import time
from PIL import Image
import shortuuid
from flasgger import swag_from
from flask import Blueprint, render_template, request, jsonify, current_app, Response

from model.result import Result

file = Blueprint('file', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'bmp', 'BMP'])
ALLOWED_WIDTH_HEIGHT = set(['600', '300x300', '100x100'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@file.route('/images', methods=['GET'], strict_slashes=False)
@swag_from("yml/file_view_images_upload.yml")
def upload_view():
    return render_template("product/upload.html")


@file.route('/images', methods=['POST'], strict_slashes=False)
def api_upload():
    upload = current_app.config.get("UPLOAD_IMAGE")
    now = datetime.date.today().isoformat()
    file_dir = os.path.join(upload, now.replace("-", "/"))
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']
    if f and allowed_file(f.filename):
        ext = f.filename.rsplit('.', 1)[1]
        if ext in ALLOWED_EXTENSIONS:
            new_filename = str(int(time.time())) + '_' + shortuuid.uuid()[:8] + "." + ext
            f.save(os.path.join(file_dir, new_filename))
            return jsonify(Result().success("/file/img/" + new_filename))
    return jsonify(Result().fail())


@file.route('/img/<path>', methods=['GET'])
def get_img(path):
    arr = path.split("_")
    time = arr[0]
    upload = current_app.config.get("UPLOAD_IMAGE")
    datepath = datetime.datetime.fromtimestamp(int(time)).date().isoformat()
    file_dir = os.path.join(upload, datepath.replace("-", "/"), path)
    if os.path.exists(file_dir):
        with open(file_dir, 'rb') as f:
            return Response(f.read(), mimetype="image/jpeg")
    else:
        ext = path.rsplit('.', 1)[1]
        orign_dir = os.path.join(upload, datepath.replace("-", "/"), "%s_%s.%s" % (arr[0], arr[1], ext))
        print(orign_dir)
        if len(arr) > 2:
            wh_str = arr[2].split(".")[0]
            if not wh_str in ALLOWED_WIDTH_HEIGHT:
                return jsonify(Result().fail(code="wh.not.allow",msg="wh not allow"))
            wh = wh_str.split("x")
            if len(wh) > 1:
                # widthxheight.png
                print(orign_dir)
                print(file_dir)
                print(wh)
                img4 = cut_img_center(orign_dir,file_dir,wh)
            else:
                # width.png
                img4 = scale_img_width(orign_dir, file_dir, wh)
        return Response(img4, mimetype="image/jpeg")
    return jsonify(Result().fail())


def cut_img_center(orign_dir,dest_dir,wh):
    img = Image.open(orign_dir)
    img4 = img.thumbnail(
        (
            int(wh[0]),
            int(wh[1])
       )
    )

    img4.save(dest_dir)
    return img4


def scale_img_width(orign_dir,dest_dir,wh):
    img = Image.open(orign_dir)
    width = img.size[0]
    height = img.size[1]
    scale=int(wh[0])/width
    scale_w=int(wh[0])
    scale_h=height*scale
    print("scale %s %s" % (scale_w,scale_h))
    img4 = img.resize((int(scale_w), int(scale_h)))
    img4.save(dest_dir)
    return img4