import csv
import os
from datetime import datetime

# Tempat disimpannya file CSV
csv_filename = 'Transaksi.csv'

# Check if file exist and create if file does not Exist
if os.path.exists('Transaksi.csv') :
    pass
else :
    csv_create = open("Transaksi.csv","w+")
    fields = ["No Transaksi", "Tanggal Transaksi", "Jenis Transaksi", "Kategori", "Jumlah Transaksi"]
    with open (csv_filename, mode='w', newline='') as csv_file :
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

# Untuk Membuat Efek Clear Screen pada program
def clear_screen() :
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan Menu Utama Program
def tampil_menu() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open(csv_filename,mode="r") as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum(1 for row in Transaksi)
    print("=== APLIKASI PENCATATAN KEUANGAN PERSONAL === \n")
    print("=================== MENU ====================")
    print("* Info Total Transaksi : ",row_count)
    print("============================================= \n")
    print("[1] Lihat Data Transaksi")
    print("[2] Tambah Data Transaksi")
    print("[3] Edit Data Transaksi")
    print("[4] Hapus Data Transaksi")
    print("[5] Cari Data Transaksi")
    print("[6] Cek Saldo")
    print("[0] Exit \n")
    print("=============================================")
    pilihan_menu = input("Pilih Menu > ")
    if (pilihan_menu == "1") :
        tampil_sub_menu_1()
    elif (pilihan_menu == "2") :
        tambah_data_transaksi()
    elif (pilihan_menu == "3") :
        edit_data_transaksi()
    elif (pilihan_menu == "4") :
        hapus_data_transaksi()
    elif (pilihan_menu == "5") :
        cari_data_transaksi()
    elif (pilihan_menu == "6") :
        cek_saldo()
    elif (pilihan_menu == "0") :
        exit()
    else :
        print("Anda memilih menu yang salah !")
        print("Silahkan memilih menu sesuai deskripsi !")
        kembali_ke_menu()


# Fungsi Kembali Ke Menu Utama
def kembali_ke_menu() :
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    tampil_menu()


# Fungsi Menampilkan Transaksi Dengan Urutan Nomor Transaksi
def tampil_data_transaksi() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r") as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum (1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\t\tDaftar Riwayat Transaksi")
    print("-" * 106)
    print("")
    print("Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    no_urut = sorted(Transaksi, key=lambda d: d['No Transaksi'])
    # Looping untuk mengeluarkan data list of dict
    for data in no_urut :
        print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    kembali_ke_sub_menu()


# Fungsi Menambah Data Transaksi
def tambah_data_transaksi() :
    clear_screen()
    # Buka file CSV dengan mode Writer / Tulis
    with open (csv_filename, mode='a', newline='') as csv_file :
        fieldnames = ['No Transaksi','Tanggal Transaksi', 'Jenis Transaksi', 'Kategori', 'Jumlah Transaksi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("==================================")
        print("======== Tambah Transaksi ========")
        print("==================================\n")
        print("Pilihan Jenis Transaksi : ")
        print("Jenis Transaksi [1] = Pemasukan")
        print("Jenis Transaksi [0] = Pengeluaran \n")
        print("==================================\n")
        no_transaksi = input ("Masukkan Nomor Transaksi : ")
        tanggal_transaksi = input("Tanggal Transaksi (DD-MM-YYYY) : ")
        jenis_transaksi = input("Jenis Transaksi : ")
        kategori = input("Kategori : ").lower()
        jumlah_transaksi = input("Jumlah Transaksi : ")
        # Menulis data baru ke dalam file csv dalam bentuk dict
        writer.writerow({'No Transaksi' : no_transaksi,'Tanggal Transaksi' : tanggal_transaksi, 'Jenis Transaksi' : jenis_transaksi, 'Kategori' : kategori, 'Jumlah Transaksi' : jumlah_transaksi})
        print("")
        print("=================================")
        print("Data Berhasil Ditambahkan")
        print("=================================")
        print("")
    kembali_ke_menu()


# Fungsi Edit/Update Data Transaksi
def edit_data_transaksi () :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r", newline='') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum(1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\tDaftar Riwayat Transaksi")
    print("-" * 106)
    print("")
    print("Pilihan Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    # Looping untuk mengeluarkan data list of dict
    no_urut = sorted(Transaksi, key=lambda d: d['No Transaksi'])
    for data in no_urut :
         print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    no_transaksi = input ("Masukkan Nomor Transaksi : ")
    tanggal_transaksi = input("Tanggal Transaksi (DD-MM-YYYY) : ")
    jenis_transaksi = input("Jenis Transaksi : ")
    kategori = input("Kategori : ").lower()
    jumlah_transaksi = input("Jumlah Transaksi : ")
    # Mencari Data Transaksi dan Mengubah Datanya dengan Data Baru
    indeks = 0
    for data in Transaksi :
        if(data['No Transaksi'] == no_transaksi) :
            Transaksi[indeks]['Tanggal Transaksi'] = tanggal_transaksi
            Transaksi[indeks]['Jenis Transaksi'] = jenis_transaksi
            Transaksi[indeks]['Kategori'] = kategori
            Transaksi[indeks]['Jumlah Transaksi'] = jumlah_transaksi
        indeks += 1
    # Menulis data baru ke file CSV dengan mode Writer/Tulis
    with open (csv_filename, mode="w") as csv_file :
        fieldnames = ['No Transaksi', 'Tanggal Transaksi', 'Jenis Transaksi', 'Kategori', 'Jumlah Transaksi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Transaksi :
            writer.writerow({'No Transaksi' : new_data['No Transaksi'], 'Tanggal Transaksi' : new_data['Tanggal Transaksi'], 'Jenis Transaksi' : new_data['Jenis Transaksi'], 'Kategori' : new_data['Kategori'], 'Jumlah Transaksi' : new_data['Jumlah Transaksi']})
    print("")
    print("=================================")
    print("Data Berhasil Di Update")
    print("=================================")
    print("")
    kembali_ke_menu()


# Fungsi Hapus Transaksi
def hapus_data_transaksi() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r") as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum(1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\tDaftar Riwayat Transaksi")
    print("-" * 106)
    print("")
    print("Pilihan Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    no_urut = sorted(Transaksi, key=lambda d: d['No Transaksi'])
    for data in no_urut :
        print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    no_transaksi = input("Hapus Transaksi dengan No : ")
    indeks = 0
    # Looping untuk mencari data (no transaksi) untuk dihapus
    for data in Transaksi :
        if (data['No Transaksi']== no_transaksi) :
            Transaksi.remove(Transaksi[indeks])
        indeks+=1
    # Menulis data baru untuk dihapus Ke dalam File CSV dengan mode write/tulis (tulis ulang)
    with open (csv_filename, mode="w") as csv_file :
        fieldnames = ['No Transaksi', 'Tanggal Transaksi', 'Jenis Transaksi', 'Kategori', 'Jumlah Transaksi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Transaksi :
            writer.writerow({'No Transaksi' : new_data['No Transaksi'], 'Tanggal Transaksi' : new_data['Tanggal Transaksi'], 'Jenis Transaksi' : new_data['Jenis Transaksi'], 'Kategori' : new_data['Kategori'], 'Jumlah Transaksi' : new_data['Jumlah Transaksi']})
    print("")
    print("=================================")
    print("Data Berhasil Dihapus")
    print("=================================")
    print("")
    kembali_ke_menu()


# Fungsi Cari Data Transaksi 
def cari_data_transaksi () :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode = "r") as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    no_transaksi = input("Cari berdasarkan No Transaksi > ")
    data_found = []
    # Mencari Data Transaksi dengan no transaksi
    indeks = 0
    for data in Transaksi :
        if (data['No Transaksi'] == no_transaksi) :
            data_found = Transaksi[indeks]
        indeks += 1
    if len(data_found) > 0 :
        print("")
        print("====================================")
        print("Data Berhasil Ditemukan :")
        print("====================================")
        print("")
        print(f"Tanggal Transaksi\t: {data_found['Tanggal Transaksi']}")
        print(f"Jenis Transaksi \t: {data_found['Jenis Transaksi']}")
        print(f"Kategori \t\t: {data_found['Kategori']}")
        print(f"Jumlah Transaksi\t: Rp.{data_found['Jumlah Transaksi']}")
        print("")
        print("====================================")
        print("")
    else :
        print("")
        print("===========================")
        print("Maaf Data Tidak Ditemukan")
        print("===========================")
        print("")
    kembali_ke_menu()


# Fungsi Cek Saldo
def cek_saldo () :
    clear_screen ()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r", newline='') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    print("-" * 40)
    print("\t\tInfo Saldo")
    print("-" * 40)
    jumlah_pemasukan = 0
    jumlah_pengeluaran = 0
    for data in Transaksi :
        jml_transaksi = {data['Jumlah Transaksi']}
        if (data['Jenis Transaksi'] == "1") :
            list_pemasukan = []
            for i in jml_transaksi :
                list_pemasukan.append(int(i))
                for j in list_pemasukan :
                    jumlah_pemasukan += j
        elif (data['Jenis Transaksi'] == "0") :
            list_pengeluaran = []
            for i in jml_transaksi :
                list_pengeluaran.append(int(i))
                for j in list_pengeluaran :
                    jumlah_pengeluaran += j
    print("Jumlah Pendapatan \t: Rp.",jumlah_pemasukan, sep="" )
    print("Jumlah Pengeluaran \t: Rp.",jumlah_pengeluaran, sep="" )
    print("Total Saldo \t\t: Rp.",(jumlah_pemasukan-jumlah_pengeluaran), sep="")
    print("-" * 40)
    kembali_ke_menu()


# Fungsi Mengurutkan Data Transaksi Berdasarkan Tanggal
def tampil_data_transaksi_tanggal() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r", newline='') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum (1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\tDaftar Riwayat Transaksi Urutan Tanggal")
    print("-" * 106)
    print("")
    print("Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    tanggal_urut = sorted(Transaksi, key=lambda x: datetime.strptime(x['Tanggal Transaksi'], '%d-%m-%Y'))
    # Looping untuk mengeluarkan data list of dict
    for data in tanggal_urut :
        print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    kembali_ke_sub_menu()


# Fungsi Mengurutkan Data Transaksi Berdasarkan Kategori 
def tampil_data_transaksi_kategori() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r", newline='') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum (1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\tDaftar Riwayat Transaksi Urutan Kategori")
    print("-" * 106)
    print("")
    print("Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    kategori_urut = sorted(Transaksi, key=lambda d: d['Kategori'])
    # Looping untuk mengeluarkan data list of dict
    for data in kategori_urut :
        print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    kembali_ke_sub_menu()

# Fungsi Mengurutkan Data Transaksi Berdasarkan Jenis Transaksi
def tampil_data_transaksi_jenis() :
    clear_screen()
    Transaksi = []
    # Buka file CSV dengan mode Read / Baca
    with open (csv_filename, mode="r", newline='') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum (1 for row in Transaksi)
    print("-" * 106)
    print("\t\t\t\tDaftar Riwayat Transaksi Urutan Jenis Transaksi")
    print("-" * 106)
    print("")
    print("Jenis Transaksi : ")
    print("Jenis Transaksi [1] = Pemasukan")
    print("Jenis Transaksi [0] = Pengeluaran")
    print("")
    print("-" * 106)
    print("No Transaksi \t Tanggal Transaksi \t Jenis Transaksi \t Kategori \t\t Jumlah Transaksi")
    print("-" * 106)
    jenis_urut = sorted(Transaksi, key=lambda d: d['Jenis Transaksi'])
    # Looping untuk mengeluarkan data list of dict
    for data in jenis_urut :
        print(f"{data['No Transaksi']} \t\t {data['Tanggal Transaksi']} \t\t {data['Jenis Transaksi']} \t\t\t {data['Kategori']} \t\t\t Rp.{data['Jumlah Transaksi']} \t |")
    print("-" * 106)
    print("Total Transaksi : ",row_count)
    print("-" * 106)
    kembali_ke_sub_menu()

# Fungsi Tampil Sub Menu Tampil Data Transaksi
def tampil_sub_menu_1 () :
    clear_screen()
    Transaksi = []
    with open(csv_filename,mode="r") as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Transaksi.append(row)
    # Row Count Untuk Hitung Jumlah Transaksi Yang Sudah Tersimpan di File CSV
    row_count = sum (1 for row in Transaksi)
    print("===================== Sub Menu [1] ===================")
    print("Total Transaksi : ",row_count)
    print("====================================================== \n")
    print("[1] Lihat Data Transaksi General")
    print("[2] Lihat Data Transaksi Dengan Urutan Tanggal")
    print("[3] Lihat Data Transaksi Dengan Urutan Jenis Transaksi")
    print("[4] Lihat Data Transaksi Dengan Urutan Kategori")
    print("[0] Kembali Ke Menu Awal \n")
    print("====================================================== \n")
    pilihan_sub_menu_1 = input("Pilih Menu Sub Menu [1] > ")
    if (pilihan_sub_menu_1 == "1") :
        tampil_data_transaksi()
    elif (pilihan_sub_menu_1 == "2") :
        tampil_data_transaksi_tanggal()
    elif (pilihan_sub_menu_1 == "3") :
        tampil_data_transaksi_jenis()
    elif (pilihan_sub_menu_1 == "4") :
        tampil_data_transaksi_kategori()
    elif (pilihan_sub_menu_1 == "0") :
        tampil_menu()
    else :
        print("Anda memilih menu yang salah !")
        print("Silahkan memilih menu sesuai deskripsi !")
        kembali_ke_sub_menu()


# Fungsi Untuk Kembali Sub Menu 1
def kembali_ke_sub_menu () :
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Sub Menu 1...")
    tampil_sub_menu_1()

# Looping Untuk Menjalankan Program 
if __name__ == "__main__" :
    while True:
        tampil_menu()