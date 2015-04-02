#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import Tkinter as tk

path = os.path.split(os.path.realpath(__file__))[0]
xiami_sh = path + '/xiami.sh'

def rotate(ori,root):
	os.system('xrandr -o '+ori)
	root.quit()

def keystrock(key):
	os.system('xdotool key '+key)

root = tk.Tk()
root.geometry('-10+50')
root.wm_attributes('-topmost',1)
root.wm_title('PaNeL')

btn_xiami_p=tk.Button(root,text='►/❚❚',command=lambda:os.system(xiami_sh+' &'))
btn_xiami_n=tk.Button(root,text='►►❚',command=lambda:os.system(xiami_sh+' -n &'))

btn_bri_u=tk.Button(root,text='☼',command=lambda:keystrock('XF86MonBrightnessUp'))
btn_bri_d=tk.Button(root,text='☀',command=lambda:keystrock('XF86MonBrightnessDown'))

btn_ori_l=tk.Button(root,text='⟲',command=lambda:rotate('left',root))
btn_ori_r=tk.Button(root,text='⟳',command=lambda:rotate('right',root))
btn_ori_n=tk.Button(root,text='⥀',command=lambda:rotate('normal',root))

btn_quit=tk.Button(root,text='Quit',command=root.quit,fg='red')

for x in range(4):
  tk.Grid.columnconfigure(root, x, weight=1)

for y in range(4):
  tk.Grid.rowconfigure(root, y, weight=1)

btn_ori_l.grid(row=0,column=0,rowspan=4,sticky='nsew')
btn_ori_r.grid(row=0,column=4,rowspan=4,sticky='nsew')
btn_ori_n.grid(row=0,column=1,columnspan=2,sticky='nsew')
btn_xiami_p.grid(row=1,column=1,sticky='nsew')
btn_xiami_n.grid(row=2,column=1,sticky='nsew')
btn_bri_u.grid(row=1,column=2,sticky='nsew')
btn_bri_d.grid(row=2,column=2,sticky='nsew')
btn_quit.grid(row=3,column=1,columnspan=2,sticky='nsew')

root.mainloop()
