名称：ssh终端图像欢迎界面

作用:设置远程终端的图像欢迎界面。

步骤：
1.下载一张喜欢的图片，把它更名为“test.png”（替换狗头）;

2.运行命令执行脚本      ：   “ python3 pictonum.py ”；
（若无pillow库，下载安装：   “ pip3 install pillow ” ）

3.运行脚本后得到"test.txt"文本，已经把图片转为字符;
  编辑此文本            ：   “ vim test.txt ”
  在每行首添加 'echo "' ：   “ :%s/^/echo " ” 
  在每行尾添加 '"'      ：   “ :%s/$/" ”
  另存为“test2.txt”文本 ：   “ :w test2.txt ”
  退出编辑              ：   “ :q! ”

4.先获取权限            ：   “ sudo su”;
  写入配置文本          ：   “ cat test2.txt >> /etc/profile ”

温馨提示：可参考我的模板进行比对验证

作者：钱富根
时间：2018-11-24 12:00
