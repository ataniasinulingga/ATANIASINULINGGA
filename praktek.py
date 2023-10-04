nama = input ("enter nama :")
nim = input ("enter nim :")
print(nama)
print(nim)

# masukkan input nilai dalam kilogram
berat_kg = (input("Masukkan berat dalam kilogrgram: "))

# menampilkan menu pilihan satuan massa 
print("pilih satuan massa yang akan di koversikan: ")
print("1. pound (lb)")
print("2. ounce (oz)")
print("3. gram (g)")

# meminta pengguna untuk memilih satuan massa 
pilihan = int(input("masukkan nomor pilihan (1,2,3): "))

# inisialisasi variabel hasil
hasil = 0

# lonversi yang dipilih 
if pilihan == 1: 
    # konversi ke pound (lb)
    hasil = berat_kg * 2.234
    satuan = "pound (lb)"
elif pilihan == 2:
    # konversi ke ounce (oz)
    hasil = berat_kg * 56.890
    satuan = "ounce (oz)"
elif pilihan == 3:
    # konversi ke gram (g)
    hasil = berat_kg * 3.000
    satuan = "gram (g)"
else:
    print("pilihan tidak valid. silahkan pilih nomor 1/2/3. ")

# menampilkan hasil konversi jika valid
if pilihan in [1,2,3]:
    print(f"{berat_kg} kilogram sama denga {hasil} {satuan}")