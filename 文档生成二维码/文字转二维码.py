#coding:utf-8
import qrcode
from PIL import Image
import os

#生成二维码图片
def make_qr(str,save):
    qr=qrcode.QRCode(
        #version=4,  #生成二维码尺寸的大小 1-40  1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M, #L:7% M:15% Q:25% H:30%
        box_size=10, #每个格子的像素大小
        border=2, #边框的格子宽度大小
    )
    qr.add_data(str)
    qr.make(fit=True)

    img=qr.make_image()
    img.save(save)
#生成带logo的二维码图片
def make_logo_qr(str,logo,save):
    #参数配置
    qr=qrcode.QRCode(
        #version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )
    #添加转换内容
    qr.add_data(str)
    qr.make(fit=True)
    img=qr.make_image()
    img=img.convert("RGBA")
    if logo and os.path.exists(logo):
        icon=Image.open(logo)
        img_w,img_h=img.size
        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
    #保存处理后图片
    img.save(save)

if __name__=='__main__':
    save_path='base__runmethod_02.png'
    logo='logo.jpg'  #logo图片
    path = os.getcwd() + r'\ceshi.log'
    print(path)
    f = open(path,'r+',encoding='UTF-8' )
    i = f.read()
    str=i
    make_logo_qr(str,logo,save_path)