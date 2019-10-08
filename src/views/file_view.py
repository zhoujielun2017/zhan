import datetime
import os
import time

import shortuuid
from PIL import Image
from flasgger import swag_from
from flask import Blueprint, render_template, request, jsonify, current_app, Response, session

from const import const
from model.result import Result
from views.util.captcha import Captcha

file = Blueprint('file', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'bmp', 'BMP'])
ALLOWED_WIDTH_HEIGHT = set(['600', '300x300', '100x100'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@file.route('/images', methods=['GET'], strict_slashes=False)
@swag_from("yml/file_view_images_upload.yml")
def upload_view():
    return render_template("product/upload.html")


@file.route('/captcha', methods=['GET'])
@swag_from("yml/file_view_images_captcha.yml")
def captcha():
    img = Captcha()
    data, valid_str = img.getValidCodeImg()
    session[const.SESSION_CAPTCHA] = valid_str
    return Response(data, mimetype="image/jpeg")


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
    if not os.path.exists(file_dir):
        ext = path.rsplit('.', 1)[1]
        orign_dir = os.path.join(upload, datepath.replace("-", "/"), "%s_%s.%s" % (arr[0], arr[1], ext))
        print(orign_dir)
        if len(arr) > 2:
            wh_str = arr[2].split(".")[0]
            if not wh_str in ALLOWED_WIDTH_HEIGHT:
                return jsonify(Result().fail(code="wh.not.allow", msg="wh not allow"))
            wh = wh_str.split("x")
            if len(wh) > 1:
                # widthxheight.png
                print(orign_dir)
                print(file_dir)
                print(wh)
                clip_resize(orign_dir, file_dir, wh)
            else:
                # width.png
                thumbnail(orign_dir, file_dir, wh)
    with open(file_dir, 'rb') as f:
        return Response(f.read(), mimetype="image/jpeg")


def thumbnail(orign_dir, dest_dir, wh):
    img = Image.open(orign_dir)
    width = img.size[0]
    height = img.size[1]
    scale = int(wh[0]) / width
    scale_w = int(wh[0])
    scale_h = height * scale
    img.thumbnail((int(scale_w), int(scale_h)))
    img.save(dest_dir)
    return img


# 裁剪压缩图片
def clip_resize(orign_dir, dest_dir, wh):
    '''
        先按照一个比例对图片剪裁，然后在压缩到指定尺寸
        一个图片 16:5 ，压缩为 2:1 并且宽为200，就要先把图片裁剪成 10:5,然后在等比压缩
    '''
    dst_w = float(wh[0])
    dst_h = float(wh[1])
    im = Image.open(orign_dir)
    ori_w, ori_h = im.size

    dst_scale = float(dst_w) / dst_h  # 目标高宽比
    ori_scale = float(ori_w) / ori_h  # 原高宽比

    if ori_scale <= dst_scale:
        # 过高
        width = ori_w
        height = int(width / dst_scale)

        x = 0
        y = (ori_h - height) / 2

    else:
        # 过宽
        height = ori_h
        width = int(height * dst_scale)

        x = (ori_w - width) / 2
        y = 0

    # 裁剪
    box = (x, y, width + x, height + y)
    # 这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
    # 所包围的图像，crop方法与php中的imagecopy方法大为不一样
    newIm = im.crop(box)
    im = None

    # 压缩
    ratio = float(dst_w) / width
    newWidth = int(width * ratio)
    newHeight = int(height * ratio)
    newIm.resize((newWidth, newHeight), Image.ANTIALIAS).save(dest_dir)
    return newIm
