#!/usr/bin/env python3
import tkinter as tk
import pyscreenshot
from PIL import ImageTk, Image

class FullScreenApp(object):
  def __init__(self, master, **kwargs):
    self.master = master


    self.frame = tk.Frame(master, bg="black") #green for testing
    self.frame.pack(fill=tk.BOTH, expand=tk.YES)

    self.canvas = tk.Canvas(self.frame, bg="black")
    self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

    self.im      = pyscreenshot.grab().convert('LA')
    self.imobj   = ImageTk.PhotoImage(self.im)
    self.canvimg = self.canvas.create_image(0,0, image=self.imobj, anchor=tk.NW)

    #master.overrideredirect(True)
    master.attributes('-fullscreen', True)
    master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    master.bind_all('<Key>', self.key)
    master.focus_set()

  def key(self, event):
    event.widget.quit()
    #print "pressed", repr(event.char)
    root.destroy()

root = tk.Tk()
app  = FullScreenApp(root)
root.mainloop()