from makanan import Makanan
import os
import random

os.system("cls")
#variable lain
energi = 3
hari = 0


#makanan
hp_gehu = [2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000]
makanan1 = Makanan("Gehu",hp_gehu,0,"Belum Terjual")

hp_balabala = [2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,8000]
makanan2 = Makanan("Bala Bala",hp_balabala,20000000,"Belum Terjual")


def header():
    print(f"{'Game Sederhana': ^40}")
    print(f"{'Silahkan kelola warung ini dengan baik': ^40}")
    print(f"{'='*40: ^40}")
    
def display_pil():
    print(f"Hari ke-{hari}")
    print("anda ingin melakukan apa? :")
    print("1. Buka Toko")
    print("2. Buat Makanan")
    print("3. Beli bahan")
    print("4. Beli resep")
    print("5. Info")
    print("6. Ganti Hari")

def bukaToko():
    global energi
    if energi > 0:
        print("Anda ingin menjual makanan apa? :")
        print(f"1. {makanan1.nama}")
        print(f"2. {makanan2.nama}")
        opsi = input("pilihanmu?")
        if opsi == "1":
            makanan1.jual()
            energi -= 1
        elif opsi == "2":
            if makanan2.kode_b == "Terjual":
                makanan2.jual()
                energi -= 1
            else:
                print("Anda belum membeli resep ini!")
    else:
        print("Energi Anda Habis!")

def info():
    print(f"Jumlah produk makanan : {Makanan.jumlah_resep}\nUang : {Makanan.pendapatan}\n")
    if Makanan.jumlah_resep < 2:
        print(f"Produk {makanan1.nama}\nHarga jual : {makanan1.harga}\nStock : {makanan1.jumlah}\nBahan : {makanan1.jumlah_bahan}\nRating : {makanan1.rating}\n")
    else:
        print(f"Produk {makanan1.nama}\nHarga jual : {makanan1.harga}\nStock : {makanan1.jumlah}\nBahan : {makanan1.jumlah_bahan}\nRating : {makanan1.rating}\n")
        print(f"Produk {makanan2.nama}\nHarga jual : {makanan2.harga}\nStock : {makanan2.jumlah}\nBahan : {makanan2.jumlah_bahan}\nRating : {makanan2.rating}")

def resetEnergi():
    global energi
    global hari
    if energi == 0:
        print("Hari berganti")
        energi += 3
        hari += 1
    else:
        print("Hari Berganti")
        energi = 3
        hari += 1

def main_opsi():
    opsi = input("pilihan anda? :")
    if opsi == "1":
        os.system("cls")
        bukaToko()
    elif opsi == "2":
        os.system("cls")
        b_makanan = int(input("Ingin buat seberapa banyak? :"))
        makanan1.restock(b_makanan)
    elif opsi == "3":
        os.system("cls")
        b_bahan = int(input("Ingin beli bahan seberapa banyak? :"))
        makanan1.beliBahan(b_bahan)
        print(f"Bahan sebanyak {b_bahan} telah dibeli")
    elif opsi == "4":
        os.system("cls")
        print("Mau beli Resep apa? :")
        print(f"1. {makanan2.nama} seharga Rp.{makanan2.harga_resep}")
        pil = input("pilihanmu? :")
        if pil == "1":
            makanan2.beliResep1()
    elif opsi == "5":
        os.system("cls")
        info()
    elif opsi == "6":
        os.system("cls")
        resetEnergi()

def main():
    nama_r = input("Masukan nama warung anda : ")
    print(f"Warung {nama_r}")
    while True:
        display_pil()
        main_opsi()
       

header()
main()




