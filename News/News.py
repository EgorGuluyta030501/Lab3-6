import requests
 
    
from bs4 import BeautifulSoup
import requests
from tkinter import *
from Frame_from_item import FrameFromItem as FFI
import urllib.request
import os
from tkinter import *
from PIL import ImageTk,  Image
listItem = []
listButton = []
itemMenu = []
def back_callback():
    i = load_main_news("https://news.tut.by/top5news/")
def destroy_main_news(i,listItem,listButton):
    for item in range(i):
        listItem[item].destroy()
        itemMenu[0].destroy()
        itemMenu[1].destroy()
        #itemMenu.clear()


def callback(col):
    destroy_main_news(i,listItem,listButton)
    download_iteam(listItem[col-1].url)
def parser_from_url(url):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup
def load_main_news(url):
    canvas = Canvas(root)
    scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = Frame(canvas)
    soup = parser_from_url(url)
    i = 0
    variable = soup.find_all(class_= 'news-entry big annoticed time ni')
    for tag in variable:
        i = i+1;
        title = tag.find('span', class_="entry-head _title")
        text = tag.find('span', class_="entry-note")
        url_item = tag.find('a', class_="entry__link")['href']
        image = tag.find( "img")['src']
        url =str( image)
        img = urllib.request.urlopen(url).read()
        out = open ("images/"+str(i) +".jpg" ,"wb")
        out.write(img)
        out.close()
        time =  tag.find('span', class_="entry-time")
        FrameItem = FFI(Frame(frame,bd = 1),title.get_text(),text.get_text(),i,time.get_text(),url_item)
        listItem.append(FrameItem)
        listItem[i-1].frame.pack()
        button = Button(listItem[i-1].TextFrame,command=lambda i=i :callback(i),text = "Узнать больше...")
        listButton.append(button)
        listButton[i-1].pack(side = "right")

    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
    for file in range(i):
        os.remove("images/"+str(file+1) +".jpg")
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)
    itemMenu.append(canvas)
    itemMenu.append(scroll_y)
    itemMenu[0].pack(fill='both', expand=True, side='left')
    itemMenu[1].pack(fill='y', side='right')
    return i
def download_iteam(url):
    canvas = Canvas(root)
    scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
    is_text = True
    TextFrame = Frame(canvas)
    Back_button = Button(canvas,command = back_callback,text = "Назад")
    Back_button.pack()
    soup = parser_from_url(url)
    soup = soup.find(class_="b-article")
    variable = soup.find_all(['img','h1','p'])

    for tag in variable:
        print(tag)
        print("\n\n\n\n\n\n\n\n\n\n\n")



        if  tag.find('img'):
            tag = tag.find('img')['src']
            image = tag
            is_text = False
            print("\n\n\n\n\nlol\n\n\n\n\n\n")
        else:
             try:
                 image = tag['src']
                 is_text = False
                 print(image)
             except Exception as e:
                  print ("LOL")
                  text_item = tag.get_text()
                  is_text = True
        if is_text:
            textLabel = Label(TextFrame,text = text_item,wraplength=700)
            textLabel.pack()
        else:
            url =str(image)
            img = urllib.request.urlopen(url).read()
            out = open("images/i.jpg" ,"wb")
            out.write(img)
            out.close()
            im = Image.open("images/i.jpg")
            ph = ImageTk.PhotoImage(im)
            label = Label(TextFrame, image=ph)
            label.image=ph
            label.pack()
            os.remove("images/i.jpg")

    TextFrame.pack(side = "left")
    canvas.create_window(0, 0, anchor='nw', window=TextFrame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)
    itemMenu.append(canvas)
    itemMenu.append(scroll_y)
    itemMenu[2].pack(fill='both', expand=True, side='left')
    itemMenu[3].pack(fill='y',side='right')


root=Tk()
root.geometry("800x900")

barframe = Frame(root,width=700,height=40)
barframe.pack(side = "top")


i = load_main_news("https://news.tut.by/top5news/")

root.mainloop()
