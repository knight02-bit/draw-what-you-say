# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:09:41 2022

@author: Knight02
"""
import os
import PicAndCloud as pc
import SpyderForMaterial as spyder

def print_menu(menu):
    for i in range(0, len(menu)):
        if (i+1) % 8 == 0:
            print(menu[i])
        elif len(menu[i])<3:
            print(menu[i], end='\t\t')
        else:
            print(menu[i], end='\t')

def judge_kind(key, menu):
    kind_char = ''
    if cloudKind in menu[0:81]:
        kind_char = 't'
    elif cloudKind in menu[81:126]:
        kind_char = 'a'
    elif cloudKind in menu[126:138]:
        kind_char = 'c'
    else:
        kind_char = 'x'
        
    return kind_char

if __name__ == "__main__":
    menu = spyder.get_menu()
    while True:
        centerWord = input(">请输入你要形容的对象[quit:退出]:")
        if centerWord=="quit":
            break
        
        pc.create_pic(centerWord)
        print_menu(menu)
        cloudKind = input("\n>请从以上风格选择"+centerWord+"的\"云\"的风格:")
        if cloudKind in menu:
            # 不同大类的url属性不同,需要预判
            kind_char = judge_kind(cloudKind, menu)
            poemText = spyder.get_text(cloudKind, kind_char)
            if len(poemText) < 100:
                print("该风格数据不足")
            else:
                pc.make_cloud(centerWord, poemText)
            
        else:
            print("该风格不存在!")  
        t = os.system("cls")