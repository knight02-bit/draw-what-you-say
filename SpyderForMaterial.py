# -*- coding: utf-8 -*-
import requests
import lxml
import re
import urllib3
from bs4 import BeautifulSoup

# 素材目录
def get_menu():
    menuList = []
    
    try:
        with open(r'.\material\kinds.txt', encoding='utf-8') as rf:
            tStr = rf.read()
            menuList.append(tStr.splitlines())
            
    except:
        print("目录读取失败!")
        
    menu = menuList[0]
    return menu
    

# 爬取对应类型诗句的前两页(需不超过本身页数)
# 在爬取前需判断素材是否存在
def get_text(kindName, kind_char='a'):
    print("素材爬取中...")
    basic_url = "https://so.gushiwen.cn/mingjus/default.aspx?{kc}str="+kindName
    
    urllib3.disable_warnings()
    res1 = requests.get(basic_url, verify=False)
    
    res1.encoding = res1.apparent_encoding
    sp = BeautifulSoup(res1.text, "lxml")
    
    # pageNum = int(sp.select("label#sumPage")[0].text)
    # endPage = min(pageNum, 2)
    endPage = 2
    
    poemList = []
    for i in range(1, endPage+1):
        url_1 = basic_url.format(kc=kind_char)+"&page="+str(i)
        res2 = requests.get(url_1, verify=False)
        
        res2.encoding = res2.apparent_encoding
        
        # 正则匹配含有href="/mingju/juv...形式的a标签内容
        # 注意:不能用select选择"cont", 因为会有其他东西混进来
        poemList += re.findall(r'<a.*?href="/mingju/juv.*?">(.*?)</a>',res2.text)
        
    poemText = ''
    for i in poemList:
        poemText += i
        
    return poemText
