from model.daftar_nilai import *
from view.view_nilai import *

while True:
    print(71*"-")
    print(25*"-", "Program Input Nilai", 25*"-")
    print(71*"-")
    print("T)ambah, U)bah, C)ari, H)apus L)ihat, K)eluar")
    print(71*"-") 

    c = input("Pilih Menu: ")

    if c.lower() == 't' or c.lower() == 'T':
        tambah_data()

    elif c.lower() == 'u' or c.lower() == 'U':
        ubah_data()

    elif c.lower() == 'c' or c.lower() == 'C':
        cetak_hasil_pencarian()

    elif c.lower() == 'h' or c.lower() == 'H':
        hapus_data()

    elif c.lower() == 'l' or c.lower() == 'L':
        cetak_daftar_nilai()

    elif c.lower() == 'k' or c.lower() == 'K':
        break

    else:
        print("Silahkan pilih menu yang tersedia\n")