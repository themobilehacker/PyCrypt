#!/usr/bin/env python3

import base64,time,hashlib,os
from cryptography.fernet import Fernet as f
from tkinter import *
import tkinter as tki
root = tki.Tk()
Height = 300
Width = 200
def key(key):
    keyc=len(key)
    key=hashlib.md5(str(key).encode())
    key=key.hexdigest()
    key=base64.urlsafe_b64encode(bytes(str(key),'utf-8'))
    return(key)
def enc(key,fi):
    os.system('zip enc -r %s'%str(fi))
    fd=open('enc.zip','rb').read()
    os.system('rm -rf %s'%fi)
    en=f(key).encrypt(fd)
    open(fi+'.enc','wb').write(en)
    t=Label(text="***File encrypted***")
    t.place(x=40,y=140)
    os.system('rm -rf enc.zip')
def dec(key,fi):
    if key=='themobilehacker':
        os.system('rm -rf %s'%fi)
        t=Label(text="***File erased***")
        return
    fd=open(fi,'rb').read()
    de=f(key).decrypt(fd)
    open(fi.replace('.enc','.zip'),'wb').write(de)
    os.system('unzip %s'%fi.replace('.enc',''))
    
    t.place(x=39,y=140)
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    os.system('rm -rf %s'%fi)

canvas = tki.Canvas(root, height =Height, width = Width)
canvas.grid()
frame = tki.Frame(root, bg = 'black')
frame.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.98)
entry = tki.Entry(frame, font = 30)
entry.place(relwidth = 1, relheight = 0.155,y=92)
entry2 = tki.Entry(frame, font = 30)
entry2.place(relwidth = 1, relheight = 0.155,y=21)
button = tki.Button(root, text = "encrypt", bg='black', fg = 'black', font = 80, command =lambda:enc(key(entry.get()),entry2.get()))
button.place(relx = 0, rely = 0.46, relwidth = 1, relheight = 0.27)
t=Label(text="filename:                                          ")
t.place(x=0,y=0)
button2 = tki.Button(root, text = "decrypt", bg='black', fg = 'black', font = 80, command =lambda:dec(key(entry.get()),entry2.get()))
button2.place(relx = 0, rely = 0.73, relwidth = 1, relheight = 0.27)
t2=Label(text="password:                                          ")
t2.place(x=0,y=71)
root.mainloop()
