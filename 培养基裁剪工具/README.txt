名称：图像裁剪

作用：根据图片与背景色差，确定裁剪边界，批量裁剪图片
步骤：
1.编辑"cut_image.py"，根据图像分辨率调整x_left,x_right,y_left,y_right.
	均为可调参数，看色差，色差越明显值越小
	x_left：左顶点裁剪，越小越靠左
	x_right：右顶点裁剪，越小越靠右
	y_left：上顶点裁剪，越小越靠上
	y_right：下顶点裁剪，越小越靠下
	border:裁剪预留边框宽度
	threshold:色差阈值

2.把需要裁剪的培养基图片放入"pictures"文件夹，首先保证该文件夹之前是空的，否则“cd pictures”进入此目录，执行 “rm *” 清空文件夹；
3.设置完毕后运行命令 "python3 cut_image.py"；
4.待程序执行完毕后，生成"processed_images",处理后的图片就在此目录中。

温馨提示：
1.如果不确定参数调整是否准确，可先放置一张图片进行测试，根据处理后的图片在进行参数调整，直到适合为止；
2.如果背景色与培养基色差越大，图片分辨率较高，可适当调低threshold参数。


作者：钱富根
时间：2018-11-17 17:00
