# 监控是否插入U盘，并把U盘上的内容复制到本地
# encoding=utf-8
from time import sleep
import os, shutil,re
usb_path = "/Volumes/"
content = os.listdir(usb_path) # os.listdir(路径)返回路径下所有文件以及文件夹的名称
while True:
    new_content = os.listdir(usb_path) #每隔三秒扫描一次/Volumes/
    if new_content != content: # 如果发现异常，即多出一个文件夹，则退出
        break;
    sleep(3)

x = [item for item in new_content if item not in content]
# 找到那个新文件夹，返回包括新文件夹string类型名称的列表，这个表达方法很pythonic
# shutil.copytree(os.path.join(usb_path, x[0]), '/Users/home/usb_copy')
# shutil.copytree 把目录下所有东西一股脑复制进/Users/home/usb_copy,
# 放进了自己的home目录下

target_folder = "../file/"
# 设置需要复制的文件格式
regex_filename = re.compile('(.*zip$)|(.*rar$)|(.*docx$)|(.*ppt$)|(.*xls$)')
for root, dirs, files in os.walk(os.path.join(usb_path, x[0])): #MyUSB location
    for name in files:
        file = os.path.join(root, name)
        if regex_filename.match(file) and os.path.getsize(file) < 1024*1024:
            shutil.copy2(file, target_folder)
