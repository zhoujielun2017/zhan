import random
import unittest

from PIL import Image, ImageFont, ImageDraw


class ImageTest(unittest.TestCase):

    def getRandomColor(self):
        '''获取一个随机颜色(r,g,b)格式的'''
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)
        return (c1, c2, c3)

    def test_image(self):
        # 获取一个Image对象，参数分别是RGB模式。宽150，高30，红色
        image = Image.new('RGB', (150, 30), 'red')
        # 保存到硬盘，名为test.png格式为png的图片
        # 获取一个画笔对象，将图片对象传过去
        draw = ImageDraw.Draw(image)
        # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
        font = ImageFont.truetype("tahoma.ttf", size=32)

        # 在图片上写东西,参数是：定位，字符串，颜色，字体
        draw.text((20, 0), 'fuyong', self.getRandomColor(), font=font)
        image.save(open('test.png', 'wb'), 'png')
