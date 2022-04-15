# -*- coding: utf-8 -*-
import jieba
import os
import math
import random
import matplotlib.pyplot as plt
from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image, ImageFont, ImageDraw, ImageOps

# def getText(file):
#     materialTest = ""
#     try:
#        f = open(file, encoding="utf-8")
#        lines = f.readlines()
       
#        for i in range(len(lines)):
#           isSelect = random.randint(0,1)
#           if isSelect==1 :
#               materialTest += '.'.join(lines)
#     except:
#        print("文件读取错误！")

#     return materialTest

# 根据生成的字体图
def make_cloud(fileName, poemText):
    print("云图生成中...")

    # 读取生成的背景
    bg_img = imread('.\\output\\'+fileName+'.jpg')
    # materialTest = getText(materialFile)   
    
    # 切分文本
    seg_list = jieba.cut(poemText)
    segs = [s for s in seg_list if len(s)>=2 ]
    seg_space = ' '.join(segs)
    
    # 随机选一款字体
    randomFont = str(random.randint(1, 29)) + '.ttf'

    wc = WordCloud(font_path='.\\font\\'+randomFont, 
                   max_words=200, random_state=42,
                   background_color='white', mask=bg_img,
                   max_font_size=100, scale=10, collocations=False).generate(seg_space)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    
    # 保存结果
    wc.to_file('.\\output\\'+fileName+'之云.jpg')

def create_pic(text, size=[1920,1080],margin=5,
              bgRGB=[255,255,255],fontRGB=[0,0,0]):

    size = tuple(size)
    bgRGB = tuple(bgRGB)
    fontRGB = tuple(fontRGB)
    # 随机选一款字体
    randomFont = str(random.randint(1, 29)) + '.ttf'
    fontType = '.\\font\\'+randomFont
    
    iW, iH = size # 画布高宽
    imageTmp = Image.new('RGB', size, bgRGB) # 设置画布大小及背景色

    # 计算字节数,GBK编码下汉字双字,英文单字,都看作双字
    byteNum = len(text.encode('gbk'))/2
    # 计算字体大小, 做一个最小值处理
    fontSize = min(int((iW-(margin*2))/byteNum),
                    int(iH-(margin*2)))
    font = ImageFont.truetype(fontType, fontSize) # 设置字体及字号
    draw = ImageDraw.Draw(imageTmp)
    fW, fH = draw.textsize(text, font) # 获取文字宽高
    # 偏移量
    oW, oH = font.getoffset(text)

    # 绘制最终图片
    imageRes = Image.new('RGB', (fW, fH), bgRGB)
    drawRes = ImageDraw.Draw(imageRes)
    # print(fW, fH, iW, iH)
    # 绘制文字
    fontx = (iW - fW - oW*10) / 100
    fonty = (iH - fH - oH*10) / 50
    drawRes.text((fontx, fonty), text, fontRGB, font)
    imageRes.save('.\\output\\'+text+'.jpg') # 保存最终图片
