# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:09:41 2022

@author: Knight
"""

import jieba
import os
import math
import random
import matplotlib.pyplot as plt
from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image, ImageFont, ImageDraw, ImageOps


def getText(file):
    news_text=""
    try:
       f = open(file,encoding="utf-8")
       lines = f.readlines()
       
       for i in range(len(lines)):
          news_text+='.'.join(lines)
    except:
       print("文件读取错误！")

    return news_text

# 根据生成的字体图
def make_cloud(fileName):
# 设置新闻文本根目录、图像路径
    newsfile = r'.\美.txt'
    img_path = '.\\'+fileName+'.jpg'
    stop_word_path = r'.\stopword.txt'
    my_word_path = r'.\myword.txt'
    
    
    # 读取文件
    stopword_list = open(stop_word_path, encoding='utf-8').readlines()
    stopword_list=[s.strip("\n") for s in stopword_list]
    bg_img = imread(img_path)
    news_text = getText(newsfile)
    
    # 设置停用词
    stop_words = set(stopword_list)
    #print('停用词:', stop_words)
    
    # 加载自定义词库
    jieba.load_userdict(my_word_path)
    
    # 切分文本
    seg_list = jieba.cut(news_text)
    segs=[s for s in seg_list if len(s)>=2 ]
    seg_space = ' '.join(segs)
    
    # 随机选一款字体
    randomFont = str(random.randint(1, 29)) + '.ttf'
    # 生成词云，font_path需指向中文字体以避免中文变成方框，若出现非方框的乱码则为txt读取时的编码选择错误
    wc = WordCloud(font_path='.\\font\\'+randomFont, max_words=800, \
                   random_state=42,background_color='white', stopwords=stop_words,  #可以在这里指定停用词
                   mask=bg_img,max_font_size=100, scale=5, collocations=False).generate(seg_space)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    
    # 保存结果
    wc.to_file('.\\'+fileName+'之云.jpg')

def CreatePic(text, size=[1920,1080],margin=5,
              bgRGB=[255,255,255],fontRGB=[0,0,0]):

    size = tuple(size)
    bgRGB = tuple(bgRGB)
    fontRGB = tuple(fontRGB)
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
    print(fW, fH, iW, iH)
    # 绘制文字
    fontx = (iW - fW - oW*10) / 100
    fonty = (iH - fH - oH*10) / 50
    drawRes.text((fontx, fonty), text, fontRGB, font)
    imageRes.save(text+'.jpg') # 保存最终图片

if __name__ == "__main__":
    # centerWord = input("请输入你要夸的对象:")  
    for i in ["哈","哈哈","哈哈哈hhhhhhhh","a","ab","abc","abcd"]:
        CreatePic(i)
        make_cloud(i)
    
    # make_cloud(centerWord+".jpg")
    # image = Image.open("2.jpg") # open colour image
    # image_file = ImageOps.invert(image) # convert image to black and white
    # image_file.save('3.jpg')