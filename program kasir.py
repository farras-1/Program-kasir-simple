user = "123"
password = "123"


username = input("please insert username :")
password = input("please insert password :")

if username == user and password == password:
    print("login success")

    def menu():
        print("menu:")
        print("1. tambahkan barang")
        print("2. lihat keranjang")
        print("3. hitung total")
        print("4. hapus barang")
        print("5. pembayaran")
        print("6. simpan nota")
        print("7. keluar")
    def fungsi1Keranjang():
        while True:
            namaBarang = input("Masukkan nama barang(q untuk keluar): ").strip()

            if namaBarang == "q":
                break

            if not all(part.isalpha() for part in namaBarang.split()):
                print("Tolong masukkan nama")
                return

            hargaBarang = input("Masukkan harga barang(q untuk keluar): ")
            if not hargaBarang.isdigit(): 
                print("Tolong masukkan angka")
                return  
        
            hargaBarang = int(hargaBarang) 
            keranjang.append({"nama": namaBarang, "harga": hargaBarang})
            print("Barang belanjaan berhasil ditambahkan")

    def fungsi2LihatKeranjang():
        if keranjang == []:
            print("keranjang kosong")
        else:
            print("isi keranjang:")
            x = 1
            for barang in keranjang:
                print(f"{x}. {barang['nama']} - {barang['harga']}")
                x += 1

    def fungsi3HitungTotal():
        total = 0
        for barang in keranjang:
            total = total + barang["harga"]

        if total > 100000:
            diskon = total * 0.1
            totalAkhir = total - diskon
            print(f"total belanja: {total}")
            print("anda mendapatkan diskon 10%")
            print(f"total yang harus dibayar: {totalAkhir}")
        else:
            print(f"total belanja: {total}")
            print("anda tidak mendapatkan diskon, untuk mendapatkan diskon minimal total belanja harus diatas RP 100.000")

    def fungsi4HapusBarang():
        try:

            HapusBarang = int(input("Masukkan nomor barang yang ingin dihapus: "))
        
            if 1 <= HapusBarang <= len(keranjang):
                barang_dihapus = keranjang.pop(HapusBarang - 1)
                print("barang berhasil dihapus, sisa barang anda : ")
            x = 1
            for barang in keranjang:
                print(f"{x}. {barang['nama']} - {barang['harga']}")
                x += 1
    
        except ValueError:
            print("Input tidak valid. Harap masukkan angka sesuai dengan belanjaan anda.")

    def fungsi5Pembayaran():
        try :
            total = 0
            for barang in keranjang:
                total = total + barang["harga"]

            if total > 100000:
                diskon = total * 0.1
                totalAkhir = total - diskon
                harga.append(totalAkhir)
                print(f"anda mendapat diskon sebesar 10%, tagihan anda :{totalAkhir} rupiah")
            else :
                totalAkhir = total
                harga.append(total)
                print(f"tagihan anda :{total} rupiah")

            bayar = int(input("masukkan nominal uang anda : "))
            pembayaran.append(bayar)
            if bayar > totalAkhir:
                kembali = bayar - totalAkhir
                kembalian.append(kembali)
                print(f"kembalian anda : {kembali}")
            elif bayar == totalAkhir:
                print("pembayaran anda pas")

            elif bayar < totalAkhir:
                kurang = totalAkhir - bayar
                kurangan.append(kurang)
                print(f"uang anda kurang sebesar : {kurang} rupiah")
        
            elif bayar == totalAkhir:
                print("uang anda pas")
        except:
            print("harap masukkan nominal dengan benar(tanpa titik)")

    def fungsi6nota():
        try:
            with open("nota belanja.txt", "w") as file:
                file.write("=== NOTA BELANJA ===\n")
                for idx, barang in enumerate(keranjang, 1):
                    file.write(f"{idx}. {barang['nama']} - Rp{barang['harga']}\n")
                file.write(f"\nTotal Belanja       : Rp{(harga)}")
                file.write(f"\nUang anda           : Rp{(pembayaran)}")
                file.write(f"\nKembalian anda      : Rp{(kembalian)}")
                file.write(f"\nKekurangan anda     : Rp{(kurangan)}")


                file.write("\n=====================")

            print("Nota berhasil disimpan ke dalam file 'nota_belanja.txt'")

        except Exception as e:
            print("Terjadi kesalahan:", e)


        
    keranjang = []
    harga= []
    pembayaran = []
    kurangan = []
    kembalian = []
    while True:
        menu()
        pilihan = input("pilih menunya: ")
        if pilihan == "1":
            fungsi1Keranjang()
        elif pilihan == "2":
            fungsi2LihatKeranjang()
        elif pilihan == "3":
            fungsi3HitungTotal()
        elif pilihan == "4":
            fungsi4HapusBarang()  
        elif pilihan == "5":
            fungsi5Pembayaran()
        elif pilihan == "6":
            fungsi6nota()
        elif pilihan == "7":
            print("terimakasih sudah berbelanja")
            break
        else:
            print("pilihan tidak falid, pilih nomor antara 1 - 7")
else:
    print("password atau username tidak valid")
    