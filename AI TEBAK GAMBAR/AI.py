import os                                                           #Mengimport Library os
import numpy as np                                                  #Mengimport Library numpy
from sklearn.neighbors import KNeighborsClassifier                  #Mengimport Library scikit-learn
from PIL import Image                                               #Mengimport Library pillow

def load_dataset():                                                 #Membuat fungsi dari dataset
    persegi = []                                                    #List folder persegi
    lingkaran = []                                                  #List folder lingkaran
    segitiga = []                                                   #List folder segitiga

    for file in os.listdir("persegi"):                              #Membuat fungsi pengulangan pada folder persegi
        img = Image.open("persegi/" + file)                         #Membuka gambar yang ada di folder persegi
        img = np.array(img)                                         #Melakukan proses array
        img = img.flatten()                                         #Melakukan proses flatten
        persegi.append(img)                                         #Menambahkan gambar dari folder persegi

    for file in os.listdir("lingkaran"):                            #Membuat fungsi pengulangan pada folder lingkaran
        img = Image.open("lingkaran/" + file)                       #Membuka gambar yang ada di folder lingkaran
        img = np.array(img)                                         #Melakukan proses array
        img = img.flatten()                                         #Melakukan proses flatten
        lingkaran.append(img)                                       #Menambahkan gambar dari folder lingkaran

    for file in os.listdir("segitiga"):                             #Membuat fungsi pengulangan pada folder segitiga
        img = Image.open("segitiga/" + file)                        #Membuka gambar yang ada di folder segitiga
        img = np.array(img)                                         #Melakukan proses array
        img = img.flatten()                                         #Melakukan proses flatten
        segitiga.append(img)                                        #Menambahkan gambar dari folder segitiga
    
    return persegi, lingkaran, segitiga                             #mereturn persegi, lingkaran, segitiga

def load_ai():                                                      #membuat fungsi baru ai
    model = KNeighborsClassifier(n_neighbors=5)                     #Model dataset dari library KNeighborsClassifier                                
    persegi, lingkaran, segitiga = load_dataset()                   #Load dataset dari persegi, lingkaran, segitiga
    y_persegi = np.zeros(len(persegi))                              #Melabelkan persegi dengan angka 0
    y_lingkaran = np.ones(len(lingkaran))                           #Melabelkan persegi dengan angka 1
    y_segitiga = np.ones(len(segitiga)) * 2                         #Melabelkan persegi dengan angka 2
    X = persegi + lingkaran + segitiga                              #Menjumlahkan X
    y = np.concatenate([y_persegi, y_lingkaran, y_segitiga])        #Menjumlahkan y
    model.fit(X, y)                                                 #Memodelkan X dan y
    return model                                                    #Mereturn model