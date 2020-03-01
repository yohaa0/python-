# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zfj'
__mtime__ = '2018/7/23'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os
import jieba
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#print('当前目录是%s' % (os.getcwd()))
text = open(path.join(os.getcwd(), 'Desktop\\ranfa.txt')).read()
# print(text)
text = ' '.join(jieba.cut(text))
# print(text)
backgroud_Image = plt.imread('Desktop\\12.jpg')
wordcloud = WordCloud(
                background_color = 'white',    # 设置背景颜色
                mode="RGBA",
                mask = backgroud_Image,        #设置背景图片样式
                max_words = 2000,            # 设置最大现实的字数
                stopwords = STOPWORDS,        # 设置停用词
                font_path='C:\Windows\Fonts\simhei.ttf',
                max_font_size=80,  # 设置字体最大值
                min_font_size=5,
                random_state=42,
                scale=20,
            ).generate(text)

image_colors = ImageColorGenerator(backgroud_Image)
plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()