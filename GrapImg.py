#!/usr/bin/env python
#coding=utf-8
#此模块主要功能是屏幕截图，分以下三种方式：
#1、抓取全屏
#2、抓取当前窗口
#3、抓取所选区域

from PIL import ImageGrab
def capture_fullscreen():
    '''
    Function:全屏抓图
    Input：NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''  
    #抓图   
    img = ImageGrab.grab()
    return img
    
    
def capture_current_windows():
    '''
    Function:抓取当前窗口
    Input：NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''  
    #窗口结构       
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]
        def __str__(self):
            return str((self.left, self.top, self.right, self.bottom))
    rect = RECT()
    #获取当前窗口句柄
    HWND = win32gui.GetForegroundWindow()
    #取当前窗口坐标
    ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
    #调整坐标
    rangle = (rect.left+2,rect.top+2,rect.right-2,rect.bottom-2)
    #抓图
    img = ImageGrab.grab(rangle)
    return img
    
def capture_choose_windows():
    '''
    Function:抓取选择的区域，没有自己写这个，借用QQ抓图功能
    Input：NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''      
    try:
         #加载QQ抓图使用的dll
         dll_handle = ctypes.cdll.LoadLibrary('CameraDll.dll') 
    except Exception:
             try:
                 #如果dll加载失败，则换种方法使用，直接运行，如果还失败，退出
                 os.system("Rundll32.exe CameraDll.dll, CameraSubArea")
             except Exception:
                 return    
    else:
         try:
             #加载dll成功，则调用抓图函数，注:没有分析清楚这个函数带的参数个数
             #及类型，所以此语句执行后会报参数缺少4个字节，但不影响抓图功能，所
             #以直接忽略了些异常
             dll_handle.CameraSubArea(0)
         except Exception:
             return           
