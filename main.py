import os
import time
from tkinter import ttk
from PIL import ImageGrab, ImageTk, Image
from pathlib import Path
import tkinter as tk
import pyautogui as py
import keyboard
from tkinter import *
import win32con
import os
import time
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

def setClickthrough(hwnd):
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

def telao(off = 0):
    global tela
    global bg
    if off == 1:
        tela.destroy()
    else:
        tela = tk.Tk()
        tela.overrideredirect(True)
        tela_largura = tela.winfo_screenwidth()
        tela_altura = tela.winfo_screenheight()
        x_1 = (tela_largura / 2) - (240 / 2)
        y_1 = (tela_altura / 2) - (260 / 2)
        tela.geometry('%dx%d+%d+%d' % (240, 260, x_1, y_1))
        tela.attributes('-transparentcolor', 'white', '-topmost', 1)
        tela.config(bg='white')
        tela.wm_attributes("-topmost", 1)
        bg = Canvas(tela, width=x_1, height=y_1, bg='white')
        setClickthrough(bg.winfo_id())
        bg.pack()
        tela.update()

def update_tela(png):
    print_tela()
    frame = tk.PhotoImage(file=png)
    image = Label(bg, image=frame)
    image.pack()
    tela.update()
    image.destroy()

# hwnd = (None, NOME DA ABA)
def print_tela():
    hwnd = win32gui.FindWindow(None, 'Counter-Strike: Global Offensive - Direct3D 9')
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = 100
    h = 100
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap) #(150,150) = tmnho (633, 334) = meio da tela
    result = saveDC.BitBlt((0, 0), (150, 150), mfcDC, (633, 334), win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    if result == None:
        im = im.resize((240, 200), Image.ANTIALIAS)
        im.save("test.png")


while True:
    if keyboard.is_pressed('v'):
        telao(0)
        while True:
            if keyboard.is_pressed('c'):
                telao(1)
                break
            else:
                jpg_files = Path('C:/Users/kalil/PycharmProjects/pythonProject1').glob('*.png')
                for x in jpg_files:
                    update_tela(x)



