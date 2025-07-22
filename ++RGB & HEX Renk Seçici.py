from tkinter import *
import tkinter.messagebox

def slider(value):
    r = int(red_Scale.get())
    g = int(green_Scale.get())
    b = int(blue_Scale.get())

    rgb = f'{r},{g},{b}'
    hex_code = "#%02x%02x%02x" % (r, g, b)

    colorLabel.config(bg=hex_code)
    rgb_entry.delete(0, END)
    rgb_entry.insert(0, rgb)
    hex_entry.delete(0, END)
    hex_entry.insert(0, hex_code)


def update_color_from_rgb(rgb_string):
    try:
        r, g, b = map(int, rgb_string.split(','))
        if not all(0 <= x <= 255 for x in [r, g, b]):
            raise ValueError
        red_Scale.set(r)
        green_Scale.set(g)
        blue_Scale.set(b)
        slider(0)  # Renk güncellemesi için slider'ı tetikle
    except ValueError:
        tkinter.messagebox.showerror("Hata", "Geçersiz RGB formatı. 0 ile 255 arasında 'r,g,b' formatında değerler girin.")

def update_color_from_hex(hex_string):
    try:
        hex_string = hex_string.lstrip('#')
        r, g, b = tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))
        red_Scale.set(r)
        green_Scale.set(g)
        blue_Scale.set(b)
        slider(0)  # Renk güncellemesi için slider'ı tetikle
    except ValueError:
        tkinter.messagebox.showerror("Hata", "Geçersiz HEX formatı. '#rrggbb' formatı kullanın.")

def onClick():
    #rgb_value = rgb_entry.get()
    hex_value = hex_entry.get()
    #tkinter.messagebox.showinfo("Renk Kodunu Kopyala", f"RGB kodu ({rgb_value}) ve HEX kodu ({hex_value}) kopyalandı.") # RGB ve HEX kodunu kopyala
    tkinter.messagebox.showinfo("Renk Kodunu Kopyala", f"HEX kodu ({hex_value}) kopyalandı.") # sadece HEX kodunu kopyala
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    #clip.clipboard_append(f"RGB: {rgb_value}\nHEX: {hex_value}") # RGB ve HEX kodunu kopyala
    clip.clipboard_append(hex_value) # sadece HEX kodunu kopyala
    clip.destroy()

root = Tk()

# Başlangıçta siyah renk için değerleri ayarlayalım
r, g, b = 0, 0, 0
rgb = f'{r},{g},{b}'
hex_code = "#%02x%02x%02x" % (r, g, b)
       
root.title("Basit RGB & HEX Renk Seçici")
root.geometry("360x420+100+100")

colorLabel = Label(root, bg="black", width=50, height=10, bd=1, relief=None)
colorLabel.pack(pady=5)

frame = Frame(root, bd=1, relief=None)
frame.pack(pady=5)

red_label = Label(frame, text="Kırmızı", fg="red", font=("Arial", 12, "bold"))
red_label.grid(row=0, column=0)

red_Scale = Scale(frame, from_=0, to=255, length=210, fg="red", orient=HORIZONTAL, command=slider)
red_Scale.grid(row=0, column=1)
red_Scale.set(0)

green_label = Label(frame, text="Yeşil", fg="green", font=("Arial", 12, "bold"))
green_label.grid(row=1, column=0)

green_Scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL, command=slider)
green_Scale.grid(row=1, column=1)
green_Scale.set(0)

blue_label = Label(frame, text="Mavi", fg="blue", font=("Arial", 12, "bold"))
blue_label.grid(row=2, column=0)

blue_Scale = Scale(frame, from_=0, to=255, length=210, fg="blue", orient=HORIZONTAL, command=slider)
blue_Scale.grid(row=2, column=1)
blue_Scale.set(0)

frame2 = Frame(root, bd=1, relief=None)
frame2.pack(pady=5)

rgb_label = Label(frame2, text="RGB RENK KODU :", font=("Arial", 12, "bold"))
rgb_label.grid(row=0, column=0)

rgb_entry = Entry(frame2, width=12, font=("Arial", 12))
rgb_entry.grid(row=0, column=1, padx=5)
rgb_entry.insert(END, rgb)
rgb_entry.bind('<Return>', lambda event: update_color_from_rgb(rgb_entry.get()))

hex_label = Label(frame2, text="HEX RENK KODU :", font=("Arial", 12, "bold"))
hex_label.grid(row=1, column=0)

hex_entry = Entry(frame2, width=12, font=("Arial", 12))
hex_entry.grid(row=1, column=1, padx=5)
hex_entry.insert(END, hex_code)
hex_entry.bind('<Return>', lambda event: update_color_from_hex(hex_entry.get()))

copy = Button(frame2, text="KOPYALA", font=("Arial", 12, "bold"),command = onClick)
copy.grid(row=2, columnspan=2, pady=7)


root.mainloop()