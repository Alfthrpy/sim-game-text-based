
import random


class Makanan():
    jumlah_resep = 0
    pendapatan = 0
    def __init__(self,nama,harga_pool,harga_resep,kode_beli):
        self.nama = nama
        self.harga_pool = harga_pool
        self.harga_resep = harga_resep
        self.kode_b = kode_beli
        self.harga = 0
        self.jumlah = 0
        self.poin = 0
        self.rating = 0
        self.jumlah_bahan = 0
        Makanan.pendapatan = 20000000
        Makanan.jumlah_resep += 1

        
    

    def restock(self,input_user):
        if self.jumlah_bahan > 0:
            self.jumlah += input_user
            self.jumlah_bahan -= input_user
            print(f"Makanan sebanyak {input_user} telah dibuat")
        else:
            print("Bahan anda kurang!")
    
    def gainRating(self):
        self.poin += 10
        if self.poin >= 1000:
            self.rating = round(self.poin // 1000)
            self.rating %= 1000
            if self.rating >= len(self.harga_pool):
                self.rating = 10
    
    def gainBonus(self):
        if self.rating == 10:
            self.harga = self.harga_pool[10]
        else:
            self.harga = self.harga_pool[self.rating]

    def jual(self):
        if self.jumlah > 0:
            for jual in range(1,random.randrange(50,70)):
                if self.jumlah > 0:
                    print("Makanan Terjual!")
                    Makanan.pendapatan += self.harga
                    self.gainRating()
                    self.gainBonus()
                    self.jumlah -= 1
                    if self.jumlah < 0:
                        break
                else:
                    print("Stock habis!") 
                    break
        else:
            print("Stock habis!")


    def beliBahan(self,nilai):
        if self.pendapatan > 0:
            self.jumlah_bahan += nilai
            Makanan.pendapatan -= (nilai*1000)
        else:
            print("Uang anda tidak cukup!")

    def beliResep1(self):
        if self.pendapatan >= self.harga_resep:
            Makanan.pendapatan -= self.harga_resep
            self.kode_b = "Terjual"
            
            print(f"Anda telah membeli Resep {self.nama}")
            print(f"Sisa uang anda Rp.{self.pendapatan}")
        else:
            print("Uang anda tidak cukup!")



    
    def info(self):
        print(f"Produk {self.nama}\nHarga jual : {self.harga}\nStock : {self.jumlah}\nBahan : {self.jumlah_bahan}\nRating : {self.rating}")








    
