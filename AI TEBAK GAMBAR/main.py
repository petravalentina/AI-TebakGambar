import tkinter as tk                                                #Mengimport Library tkinter
import AI                                                           #Mengimport File Coding AI.py
import numpy as np                                                  #Mengimport Library numpy
from PIL import Image, ImageTk, ImageDraw                           #Mengimport Library pillow

model = AI.load_ai()                                                #Memodelkan file AI.py

window = tk.Tk()                                                    #Membuat tampilan background polos dari library tkinter

img = Image.new(mode="1", size=(500, 500),color=0)                  #Membuat background 1 bit dengan ukuran 500x500 pixel dengan background hitam
tkimage = ImageTk. PhotoImage(img)                                  #Mengconvert objek gambar agar bisa dibaca oleh tkinter
canvas = tk.Label(window, image=tkimage)                            #Membuat canvas sebagai media menggambar 
canvas.pack()                                                       #Mengupdate canvas yang sudah dibuat

draw = ImageDraw.Draw(img)                                          #Membuat kuas untuk menggambar objek

last_point = (0, 0)                                                 #Membuat label last_point dengan default(0,0)
prediction = tk.StringVar()                                         #Menginputkan StringVar pada tkinter untuk prediksi
label = tk.Label(window, textvariable=prediction)                   #Membuat label bahwa textvariabel adalah prediksi

def draw_image(event):                                              #Callback dari B1-Motion
    global last_point, tkimage                                      #Keyword dari last_point,tkimage
    current_point = (event.x, event.y)                              #Mengistilahkan current_point sebagai titik saat menggambar dengan potongan koordinat
    draw.line([last_point, current_point], fill=255, width=30)      #Membuat garis dengan parameter warna putih dan ketebalan 30 pixel
    last_point = current_point                                      #Titik sebelum menggambar = Titik saat menggambar
    tkimage = ImageTk.PhotoImage(img)                               #Mengconvert objek gambar agar bisa dibaca oleh tkinter
    canvas['image'] = tkimage                                       #Menampilkan garis atau gambar yang sudah dibuat
    canvas.pack()                                                   #Mengupdate canvas agar garis atau gambar yang sudah dibuat dapat ditampilkan
    img_temp = img.resize((28, 28))                                 #Meresize ukuran canvas menjadi 28x28 pixel                        
    img_temp = np.array(img_temp)                                   #Melakukan proses array
    img_temp = img_temp.flatten()                                   #Melakukan proses flatten
    output = model.predict([img_temp])                              #Menghitung hasilnya
    if(output[0] == 0):                                             #Label dari persegi 0
        prediction.set("persegi")                                   #Saat label menyatakan 0 maka diganti dengan kata persegi
    elif(output[0] == 1):                                           #Label dari lingkaran 1
        prediction.set("lingkaran")                                 #Saat label menyatakan 1 maka diganti dengan kata lingkaran
    else:                                                           #Segitiga tidak mempunyai label
        prediction.set("segitiga")                                  #Saat label tidak menyatakan 0 atau 1 maka diganti dengan kata segitiga
    label.pack()                                                    #Mengupdate label yang sudah dibuat

def start_draw(event):                                              #Callback dari ButtonPress-1
    global last_point                                               #Keyword dari last_point
    last_point = (event.x, event.y)                                 #Mengistilahkan last_point sebagai titik sebelum menggambar dengan potongan koordinat

def reset_canvas(event):                                            #Callback dari ButtonPress-3
    global tkimage, img, draw                                       #Keyword dari tkimage, img, draw
    img = Image.new(mode="1", size=(500, 500),color=0)              #Membuat background 1 bit dengan ukuran 500x500 pixel dengan background hitam setelah gambar direset
    draw = ImageDraw.Draw(img)                                      #Membuat kuas baru untuk menggambar objek setelah gambar sebelumnya direset
    tkimage = ImageTk.PhotoImage(img)                               #Mengconvert objek gambar agar bisa dibaca oleh tkinter
    canvas['image'] = tkimage                                       #Menampilkan garis atau gambar yang sudah dibuat
    canvas.pack()                                                   #Mengupdate canvas agar garis atau gambar yang sudah dibuat dapat ditampilkan

persegi = 0                                                         #counter dari folder persegi
lingkaran = 0                                                       #counter dari folder lingkaran
segitiga = 0                                                        #counter dari folder segitiga

def save_image(event):                                              #Callback dari Key
    global persegi, lingkaran, segitiga                             #Keyword dari persegi, lingkaran, segitiga
    img_temp = img.resize((28, 28))                                 #Memperkecil ukuran canvas saat save gambar untuk memudahkan AI
    if(event.char == "p"):                                          #Menjadikan tombol keyboard 'p' sebagai save gambar persegi
        img_temp.save(f"persegi/{persegi}.png")                     #Menyimpan gambar pada folder persegi dengan format png
        persegi += 1                                                #Save 1 gambar saat mengklick tombol 'p' 1 kali
    elif(event.char == "l"):                                        #Menjadikan tombol keyboard 'l' sebagai save gambar lingkaran
        img_temp.save(f"lingkaran/{lingkaran}.png")                 #Menyimpan gambar pada folder lingkaran dengan format png
        lingkaran += 1                                              #Save 1 gambar saat mengklick tombol 'l' 1 kali
    elif(event.char == "s"):                                        #Menjadikan tombol keyboard 's' sebagai save gambar segitiga
        img_temp.save(f"segitiga/{segitiga}.png")                   #Menyimpan gambar pada folder segitiga dengan format png
        segitiga += 1                                               #Save 1 gambar saat mengklick tombol 's' 1 kali

window.bind("<B1-Motion>", draw_image)                              #Menjadikan gerakan dari cursor sebagai gambar
window.bind("<ButtonPress-1>", start_draw)                          #Menjadikan klick kiri dari mouse sebagai start gambar
window.bind("<ButtonPress-3>", reset_canvas)                        #Menjadikan klick kanan dari mouse sebagai reset gambar
window.bind("<Key>", save_image)                                    #Menjadikan keyboard sebagai tombol save gambar yang sudah dibuat

label.pack()                                                        #Mengupdate label yang sudah dibuat

window.mainloop()                                                   #Menampilkan latar background yang sudah dibuat sebelumnya