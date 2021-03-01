#!/usr/bin/env python3

import time,os,pyAesCrypt
from tkinter import *
import tkinter as tki
buff=64*1024
root=tki.Tk()
Height=300
Width=200
def enc(key,fi,buff):
    if key=='themobilehacker':
        os.system('rm -rf %s'%fi)
        t=Label(text="***File erased***")
        return
    os.system('zip enc -r %s'%fi)
    os.system('rm -rf %s'%fi)
    pyAesCrypt.encryptFile('enc.zip',fi+'.enc',key,buff)
    os.system('rm -rf enc.zip')
    t=Label(text="***File encrypted***")
    t.place(x=40,y=140)

def dec(key,fi,buff):
    if key=='themobilehacker':
        os.system('rm -rf %s'%fi)
        t=Label(text="***File erased***")
        return
    pyAesCrypt.decryptFile(fi,fi.replace('.enc','.zip'),key,buff)
    os.system('unzip %s'%fi.replace('.enc',''))
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    os.system('rm -rf %s'%fi)
    t=Label(text="***File decrypted***")
    t.place(x=40,y=140)


canvas=tki.Canvas(root,height=Height,width=Width)
canvas.grid()
frame=tki.Frame(root,bg='black')
frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
entry=tki.Entry(frame,font=30,show='*')
entry.place(relwidth=1,relheight=0.155,y=92)
entry2=tki.Entry(frame,font=30)
entry2.place(relwidth=1,relheight=0.155,y=21)
button=tki.Button(root,text="encrypt",bg='black',fg='black',font=80,command=lambda:enc(entry.get(),entry2.get(),buff))
button.place(relx=0,rely=0.46,relwidth=1,relheight=0.27)
t=Label(text="filename:                                          ")
t.place(x=0,y=0)
button2=tki.Button(root,text="decrypt",bg='black',fg='black',font=80,command=lambda:dec(entry.get(),entry2.get(),buff))
button2.place(relx=0,rely=0.73,relwidth=1,relheight=0.27)
t2=Label(text="password:                                         ")
t2.place(x=0,y=71)
root.mainloop()
