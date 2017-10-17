#!bin/python 
#-*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import sys
import os
reload(sys)
from NanXiao import Him
sys.setdefaultencoding("utf-8")
def mergei(files, mid,output_file):
    tot = len(files)
    img = Image.open(files)
    w, h = img.size[0], img.size[1]
    img1 = Image.open(mid)
    w1, h1 = img1.size[0], img1.size[1]
    img2 = Image.open(u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/pass.png')
    w2,h2=img2.size[0],img2.size[1]
    merge_img = Image.new('RGB', (w1, h+h1+h2), 0xffffff)
    merge_img.paste(img, (0, 0))
    merge_img.paste(img1, (0, h))
    merge_img.paste(img2, (0, h+h1))
    merge_img.save(output_file)

url1="http://job.xidian.edu.cn/html/zpxx/nxqzph/"
url2="http://job.xidian.edu.cn/html/zpxx/bxqzph/"
input1=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/nan.png'
input2=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/bei.png'
header1=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/header_nan.png'
header2=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/header_bei.png'
out1=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/nan.png'
out2=u'H:/个人简历/pachong/Jobs-search/Zhaopin/im/bei.png'


Him(url1,input1)
Him(url2,input2)
mergei(header1,input1,out1)
mergei(header2,input2,out2)
