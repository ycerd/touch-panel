#!/usr/bin/python
import os
import Tkinter as tk

path = os.path.split(os.path.realpath(__file__))[0]
xiami_sh = path + '/xiami.sh'

def rotate(orr,root):
	os.system('xrandr -o '+orr)
	root.quit()

def keystrock(key):
	os.system('xdotool key '+key)

root = tk.Tk()
root.geometry('-10+50')
root.wm_attributes('-topmost',1)

tk.Button(root,text='Xiami',command=lambda:os.system(xiami_sh)).pack(fill='x',side='left')
tk.Button(root,text='Next',command=lambda:os.system(xiami_sh+' -n')).pack(fill='x',side='right')


tk.Button(root,text='+',command=lambda:keystrock('XF86MonBrightnessUp')).pack(fill='x')
tk.Button(root,text='-',command=lambda:keystrock('XF86MonBrightnessDown')).pack(fill='x')
tk.Button(root,text='left',command=lambda:rotate('left',root)).pack(side = 'left', fill='x')
tk.Button(root,text='right',command=lambda:rotate('right',root)).pack(side = 'right',fill='x')
tk.Button(root,text='normal',command=lambda:rotate('normal',root)).pack(fill='x')
tk.Button(root,text='Quit',command=root.quit,fg='red').pack(fill='x')

root.mainloop()
