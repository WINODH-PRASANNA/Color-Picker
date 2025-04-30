import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os


root = tk.Tk()
root.title("Color Picker from Image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

filename = None


def showimage():
   global filename
   filename = filedialog.askopenfilename(
      initialdir=os.getcwd(),
      title='Select Image File',
      filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ("All files", '*.*')]
   )
   if filename:
      img = Image.open(filename)
      img.thumbnail((310, 270))
      img = ImageTk.PhotoImage(img)
      lbl.configure(image=img, width=310, height=270)
      lbl.image = img


def findcolor():
   if not filename:
      return

   ct = ColorThief(filename)
   palette = ct.get_palette(color_count=10)
   hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette]

   canvas_items = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10]
   text_labels = [hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hex10]

   for i in range(10):
      if i < len(hex_colors):
         color = hex_colors[i]
      else:
         color = "#ffffff"

      if i < 5:
         colors.itemconfig(canvas_items[i], fill=color)
      else:
         colors2.itemconfig(canvas_items[i], fill=color)

      text_labels[i].config(text=color)


try:
   image_icon = tk.PhotoImage(file="icon.png")
   root.iconphoto(False, image_icon)
except Exception:
   pass

tk.Label(root, width=120, height=10, bg="#4272f9").pack()


frame = tk.Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)


try:
   logo = tk.PhotoImage(file="logo.png")
   tk.Label(frame, image=logo, bg="#fff").place(x=10, y=10)
except Exception:
   pass

tk.Label(frame, text="Color Finder", font="Merriweather 25 bold", bg="white").place(x=100, y=20)


colors = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20, y=90)

id1 = colors.create_rectangle(10, 10, 50, 50, fill="#000")
id2 = colors.create_rectangle(10, 60, 50, 100, fill="#000")
id3 = colors.create_rectangle(10, 110, 50, 150, fill="#000")
id4 = colors.create_rectangle(10, 160, 50, 200, fill="#000")
id5 = colors.create_rectangle(10, 210, 50, 250, fill="#000")

hex1 = tk.Label(colors, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex1.place(x=60, y=15)
hex2 = tk.Label(colors, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex2.place(x=60, y=65)
hex3 = tk.Label(colors, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex3.place(x=60, y=115)
hex4 = tk.Label(colors, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex4.place(x=60, y=165)
hex5 = tk.Label(colors, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex5.place(x=60, y=215)


colors2 = tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180, y=90)

id6 = colors2.create_rectangle(10, 10, 50, 50, fill="#000")
id7 = colors2.create_rectangle(10, 60, 50, 100, fill="#000")
id8 = colors2.create_rectangle(10, 110, 50, 150, fill="#000")
id9 = colors2.create_rectangle(10, 160, 50, 200, fill="#000")
id10 = colors2.create_rectangle(10, 210, 50, 250, fill="#000")

hex6 = tk.Label(colors2, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex6.place(x=60, y=15)
hex7 = tk.Label(colors2, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex7.place(x=60, y=65)
hex8 = tk.Label(colors2, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex8.place(x=60, y=115)
hex9 = tk.Label(colors2, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex9.place(x=60, y=165)
hex10 = tk.Label(colors2, text="#000000", fg="#000", font="Merriweather 12 bold", bg="white")
hex10.place(x=60, y=215)


selectimage = tk.Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = tk.Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=tk.GROOVE)
f.place(x=10, y=10)

lbl = tk.Label(f, bg="black")
lbl.place(x=0, y=0)

tk.Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
tk.Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=findcolor).place(x=176, y=300)


root.mainloop()
