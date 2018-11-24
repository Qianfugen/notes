from PIL import Image

image = Image.open('test.png')
# 设置图片尺寸，使其适合我终端大小
image = image.resize((100, 40), Image.ANTIALIAS)

# 图像先转为灰度图像，在二值化处理

image = image.convert('L')
# image.show()
# 设置阈值
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()

list = []
for i in range(40):
    for j in range(100):
        x = image.load()[j, i]
        list.append(x)
# print(list)

with open('test.txt', 'w') as f:
    for i in range(4000):
        if i % 100 == 0:
            f.write('\n')
        else:
            # f.write(str(list[i]))
            if list[i] == 0:
                f.write('0')
            else:
                f.write(' ')
