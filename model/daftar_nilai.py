from view.input_nilai import *

class data_mahasiswa():
    def __init__(self, nama, nim, uts, uas, tugas):
        self.nama = nama
        self.nim = nim
        self.uts = uts
        self.uas = uas
        self.tugas = tugas
        hasil_akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        self.akhir = hasil_akhir

mahasiswa = {}
def tambah_data():
    print("\nTambah Data")
    nama = input_nama()
    nim = input_nim()
    uts = input_uts()
    uas = input_uas()
    tugas = input_tugas()
    akhir = nilai_akhir()
    mahasiswa[nama] =  [nim, tugas, uts, uas, akhir]
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!\n")


def ubah_data():
    print("\nUbah Data Berdasarkan Nama")
    nama = input("Masukan Nama : ")
    if nama in mahasiswa.keys():
        print(f"Data ditemukan!")
        print(41*"=")
        print(f"Nama        : {nama}")
        print(f"NIM         : {mahasiswa[nama][0]}")
        print(f"Nilai Tugas : {mahasiswa[nama][1]}")
        print(f"Nilai UTS   : {mahasiswa[nama][2]}")
        print(f"Nilai UAS   : {mahasiswa[nama][3]}")
        print(41*"=")

        while True:
            print("1. Nama\n2. NIM\n3. Nilai\n4. Kembali")
            try:
                tanya = int(input("Apa yang ingin diubah? [1-4] : "))
                if tanya == 1:
                    _nama = input("Masukan Nama Baru : ")
                    mahasiswa[_nama] = mahasiswa.pop(nama)
                    print("Berhasil merubah Nama!\n")

                elif tanya == 2:
                    _nim = int(input("Masukan Nim Baru : "))
                    mahasiswa[nama][0] = _nim
                    print("Berhasil merubah NIM!\n")

                elif tanya == 3:
                    _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
                    _nilaiUTS = int(input("Masukan Nilai UTS Baru   : "))
                    _nilaiUAS = int(input("Masukan Nilai UAS Baru   : "))
                    _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
                    mahasiswa[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
                    print("Berhasil merubah data nilai!\n")

                elif tanya == 4:
                    pass
                    
            except ValueError:
                print("Pilihan tidak ada! Silahkan masukan [1-4]")
                print(41*"=")
                
            else:
                break

    else:
        print("Nama {0} tidak ditemukan".format(nama))


def hapus_data():
    nama = input("Masukkan Nama : ")
    if nama in mahasiswa.keys():
        del mahasiswa[nama]
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))


def cari_data():
    nama = input("Masukkan Nama : ")
    if nama in mahasiswa.keys():
        print("=" * 73)
        print("|                             Daftar Mahasiswa                          |")
        print("=" * 73)
        print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 73)
        print("| {0:15} | {1:15} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
            .format(nama, mahasiswa[nama][0], mahasiswa[nama][1], mahasiswa[nama][2], mahasiswa[nama][3], mahasiswa[nama][4]))
        print("=" * 73)