#qpy:quiet
#-*-coding:utf8;-*-
"""
@Author:yohaa0
@Date:2020-02-16
This is a sample project which use SL4A UI Framework,
There is another Sample project: https://github.com/qpython-android/qpy-calcount
"""
import qpy
import androidhelper
import urllib.request as ur
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#ff0E4200"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
	<ImageView
		android:id="@+id/logo"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="10"
	/>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:text="Hello, QPython"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
		 </LinearLayout>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">
		<TextView
	 	android:id="@+id/text1"
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:textColor="#ffffffff"
			android:layout_weight="60"
			android:gravity="left"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"
		/>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Load"
			android:id="@+id/but_load"
			android:textSize="8dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Exit"
			android:id="@+id/but_exit"
			android:textSize="8dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
</LinearLayout>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_load.add_event(click_EventHandler(self.views.but_load, self.load))

        pass

    def on_close(self):
        pass

    def load(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Load")
        
        saved_logo = qpy.tmp+"/qpy.logo"
        ur.urlretrieve("https://www.qpython.org/static/img_logo.png", saved_logo)
        self.views.logo.src = "file://"+saved_logo
	
        #以下为框架下新加
	file_name = "/storage/emulated/0/text/ceshi.txt" # （1）创建读文件对象 
        file_read = open(file_name, mode="r", encoding="utf-8") # （2）一行一行读取文件内容 
        txtlist = [l.strip() for l in file_read.readlines()] # 去行结束符      
        txtlistlen=len(txtlist)
        #print(txtlistlen)
        file_read.close()
        message = droid.dialogGetInput('总共'+str(txtlistlen)+'行', '从哪一段开始阅读?').result
        startnum=int(message)#开始行数
        message2 = droid.dialogGetInput('还有'+str(txtlistlen-starnum)+"行", '您需要阅读多少行?').result
        endnum=int(message2)#设定阅读行数
        readnum=0  #要阅读行数计数置零
        if startnum>txtlistlen:
           droid.makeToast('输入错误段数，请重新输入')   
        else:
           for p in range(startnum,txtlistlen):    
               Rtext=txtlist[p]
               readnum=readnum+1
               #print(readnum,p,Rtext)
               dayintxt="阅读第"+str(readnum)+"行，总第"+str(p)+"行_"+Rtext
               self.views.text1.text=dayintxt
               #droid.makeToast(str(readnum)+str(p)+Rtext)
               if not Rtext: 
                  break
               else:         
                  droid.ttsSpeak(Rtext)
                  time.sleep(1)
                  if endnum<readnum:#到设定次数停止
                     break
                  else:
                     time.sleep(5)
        
    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Exit")
        FullScreenWrapper2App.close_layout()

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
