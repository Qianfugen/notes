#!/usr/bin/python3
from PIL import Image
import numpy as np
import os
'''可调参数，看色差，色差越明显值越小
x_left：左顶点裁剪，越小越靠左
x_right：右顶点裁剪，越小越靠右
y_left：上顶点裁剪，越小越靠上
y_right：下顶点裁剪，越小越靠下
'''
x_left = 10
x_right = 10
y_left = 5
y_right = 5
# 色差值域，色差越大，值域越大（0-255之间),图片分辨率高，可适当调低（建议30-80之间）
threshold = 40
#预留的边框宽度
border_width=8


def image_process(image, width, height):
    list = []
    n = width / 3
    m = 2 * width / 3
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            a = image.load()[i, j]
            b = image.load()[i + 1, j]
            if abs(a[0] - b[0]) > threshold and abs(a[1] - b[1]) > threshold and abs(a[2] - b[2]) > threshold:
                if i < n or i > m:
                    list.append(i)
    return list


def image_cut(image, list, height, left, right):
    cut_left = np.bincount(list[:left])
    cut_right = np.bincount(list[-right:-1])
    left_point = np.argmax(cut_left)
    right_point = np.argmax(cut_right)
    image = image.crop((left_point-border_width, 0, right_point+border_width, height))
    return image


if __name__ == '__main__':
    if not os.path.exists('processed_pictures'):
        os.mkdir('processed_pictures')
    for pic in os.listdir('./pictures'):
        image = Image.open('./pictures/'+pic)
        w, h = image.size
        print(w, h)
        list = image_process(image, w, h)
        #image = image_cut(image, list, h, x_left, x_right)
        image = image_cut(image, list, h, x_left, x_right).rotate(90)
        w, h = image.size
        list = image_process(image, w, h)
        #print(list[-10:])
        image = image_cut(image, list, h, y_left, y_right).rotate(270)
        image.save('./processed_pictures/'+pic)
