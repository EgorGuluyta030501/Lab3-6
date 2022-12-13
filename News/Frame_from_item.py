from tkinter import *
from PIL import ImageTk, Image
class FrameFromItem(object):
     def __init__(self,frame,titleItem,textItem,nomber,date,url):
         self.frame = frame
         self.url = url
         self.nomber = nomber
         self.titleItem = titleItem
         self.textItem = textItem
         self.date = date
         self.TextFrame = Frame(frame)
         textLabel = Label(self.TextFrame,text=textItem,wraplength=300)
         titleLabel = Label(self.TextFrame,text=titleItem,wraplength=400)
         dateLabel = Label(self.TextFrame,text=date,wraplength=300)
         titleLabel.pack(side = "top")
         dateLabel.pack()
         textLabel.pack()

         try:
             im = Image.open("images/"+str((nomber)) +".jpg")

         except Exception as e:
              im = Image.open("img.jpg")

         ph = ImageTk.PhotoImage(im)

         self.label = Label(frame, image=ph)
         self.label.image=ph
         self.label.pack(side = "left")
         self.TextFrame.pack(side = "right")
     def destroy(self):
         self.frame.destroy()
         self.TextFrame.destroy()
         self.label.destroy()
