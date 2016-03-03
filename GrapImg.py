#!/usr/bin/env python
#coding=utf-8
#��ģ����Ҫ��������Ļ��ͼ�����������ַ�ʽ��
#1��ץȡȫ��
#2��ץȡ��ǰ����
#3��ץȡ��ѡ����

from PIL import ImageGrab
def capture_fullscreen():
    '''
    Function:ȫ��ץͼ
    Input��NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''  
    #ץͼ   
    img = ImageGrab.grab()
    return img
    
    
def capture_current_windows():
    '''
    Function:ץȡ��ǰ����
    Input��NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''  
    #���ڽṹ       
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]
        def __str__(self):
            return str((self.left, self.top, self.right, self.bottom))
    rect = RECT()
    #��ȡ��ǰ���ھ��
    HWND = win32gui.GetForegroundWindow()
    #ȡ��ǰ��������
    ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
    #��������
    rangle = (rect.left+2,rect.top+2,rect.right-2,rect.bottom-2)
    #ץͼ
    img = ImageGrab.grab(rangle)
    return img
    
def capture_choose_windows():
    '''
    Function:ץȡѡ�������û���Լ�д���������QQץͼ����
    Input��NONE
    Output: img
    author: yangkun
    blog:http://blog.csdn.net/xyyangkun
    date:206-03-03
    '''      
    try:
         #����QQץͼʹ�õ�dll
         dll_handle = ctypes.cdll.LoadLibrary('CameraDll.dll') 
    except Exception:
             try:
                 #���dll����ʧ�ܣ����ַ���ʹ�ã�ֱ�����У������ʧ�ܣ��˳�
                 os.system("Rundll32.exe CameraDll.dll, CameraSubArea")
             except Exception:
                 return    
    else:
         try:
             #����dll�ɹ��������ץͼ������ע:û�з����������������Ĳ�������
             #�����ͣ����Դ����ִ�к�ᱨ����ȱ��4���ֽڣ�����Ӱ��ץͼ���ܣ���
             #��ֱ�Ӻ�����Щ�쳣
             dll_handle.CameraSubArea(0)
         except Exception:
             return           
