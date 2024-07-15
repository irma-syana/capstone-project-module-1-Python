# pip install regex
# pip install tabulate

import regex as re
from tabulate import tabulate
from datetime import datetime

import regex as re
from tabulate import tabulate
from datetime import datetime

data_sampah = []
data_pasienRS = [
    {'ID': 'BUT001',
     'Nama Pasien': 'Butet Tambunan',
     'Umur': '21 tahun 0 bulan',
     'Jenis Kelamin': 'P',
     'Domisili': 'Balige',
     'Nomor HP Wali':'085227777728',
     'Tanggal Sakit': '27 January 2024',
     'Tanggal Kunjungan': '27 January 2024',
     'Diagnosis': 'Asam Lambung'},

    {'ID': 'JOJ002',
     'Nama Pasien': 'Jojo Sinaga',
     'Umur': '17 tahun 0 bulan',
     'Jenis Kelamin': 'L',
     'Domisili': 'Solo',
     'Nomor HP Wali':'081227777728',
     'Tanggal Sakit': '26 January 2024',
     'Tanggal Kunjungan': '27 January 2024',
     'Diagnosis': 'Flu'},

    {'ID': 'SUK003',
     'Nama Pasien': 'Sukjojo',
     'Umur': '17 tahun 0 bulan',
     'Jenis Kelamin': 'L',
     'Domisili': 'Surabaya',
     'Nomor HP Wali':'+6282313123212',
     'Tanggal Sakit': '27 May 2024',
     'Tanggal Kunjungan': '27 May 2024',
     'Diagnosis': 'influenza'},

]
def input_angka(prompt='Input angka: '):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Input harus angka')

def input_huruf(prompt='Input huruf: '):
    while True:
        try:
            return str(input(prompt).title())
        except ValueError:
            print('Input harus huruf')

def input_nama(prompt='Masukkan Nama Pasien (Minimal 3 huruf):'):
    while True:
        nama = input(prompt).title()
        if len(nama.strip().replace(' ','')) >= 3 and nama.replace(' ', '').isalpha():
            return nama
        else:
            print('Nama harus terdiri dari 3 karakter dan hanya mengandung huruf')

def input_tanggal(prompt='Masukkan tanggal (dd-mm-yyyy): ', min_date=None, max_date=None):
    while True:
        try:
            tanggal = datetime.strptime(input(prompt), '%d-%m-%Y').date()
            if max_date and tanggal > max_date:
                print(f'Tanggal tidak boleh lebih dari {max_date.strftime("%d-%m-%Y")}.')
            elif min_date and tanggal < min_date:
                print(f'Tanggal tidak boleh kurang dari {min_date.strftime("%d-%m-%Y")}.')
            else:
                return tanggal
        except ValueError:
            print('Format tanggal tidak valid. Pastikan formatnya dd-mm-yyyy.')

def input_jenis_kelamin(prompt='Masukkan jenis kelamin (L/P): '):
    while True:
        jenis_kelamin = input(prompt).strip().upper()
        if jenis_kelamin in ['L', 'P']:
            return jenis_kelamin
        else:
            print("Masukkan tidak valid, silakan masukkan 'L' atau 'P'.")

def input_nohp (prompt='Nomor HP Wali:' ):
    while True: #no HP 10-13 digit
        no_hp = input(prompt).strip()
        if re.fullmatch(r'08\d{8,11}', no_hp) or re.fullmatch(r'\+62\d{8,11}', no_hp):
            return no_hp
        else:
            print('Nomor HP tidak valid, harus terdiri dari 10 hingga 12 digit angka.')

def id_pasien(nama):
    kodeid = nama.replace(' ', '')[:3].upper()
    noUrut = len(data_pasienRS) + 1
    id_pasien = f'{kodeid}{noUrut:03d}'
    return id_pasien

def hitung_umur(tanggal_lahir, tanggal_hari_ini):
    tahun = tanggal_hari_ini.year - tanggal_lahir.year
    bulan = tanggal_hari_ini.month - tanggal_lahir.month
    if bulan < 0:
        tahun -= 1
        bulan += 12
    return tahun, bulan

def validasi (prompt = 'Pilih ya/tidak'):
    while True:
        validasi = input(prompt).lower().strip()
        if validasi == 'ya':
            return True
        elif validasi == 'tidak':
            return False
        else:
            print("Masukkan pilihan yang valid: 'ya' atau 'tidak'.")

def cari_data_nama(prompt = 'Cari nama pasien:'):
    while True:
        cari_data = input_nama(prompt)
        if cari_data.lower().strip() == 'exit':
            break
        hasil_pencarian = [pasien for pasien in data_pasienRS if cari_data.lower().strip() in pasien['Nama Pasien'].lower()]
        if hasil_pencarian:
            print('Hasil pencarian:')
            print(tabulate(hasil_pencarian, headers='keys', tablefmt='pretty'))
            return hasil_pencarian
        else:
            print(f'Pasien dengan nama {cari_data} tidak ditemukan.')
            continue

def cari_id_pasienRS(prompt='Masukkan ID Pasien: '):
    while True:
        id_pasien = input(prompt).upper().strip()
        for idx, pasien in enumerate(data_pasienRS):
            if pasien['ID'] == id_pasien:
                return idx, pasien
        print(f'Pasien dengan ID {id_pasien} tidak ditemukan. Silakan coba lagi.')

def cari_data_sampah(prompt = 'Cari nama pasien:'):
    while True:
        cari_data = input_nama(prompt)
        if cari_data.lower().strip() == 'exit':
            break
        hasil_pencarian = [pasien for pasien in data_sampah if cari_data.lower().strip() in pasien['Nama Pasien'].lower()]
        if hasil_pencarian:
            print('Hasil pencarian:')
            print(tabulate(hasil_pencarian, headers='keys', tablefmt='pretty'))
            return hasil_pencarian
        else:
            print(f'Pasien dengan nama {cari_data} tidak ditemukan.')
            continue

def cari_id_sampah(prompt='Masukkan ID Pasien: '):
    while True:
        id_pasien = input(prompt).upper().strip()
        for idx, pasien in enumerate(data_sampah):
            if pasien['ID'] == id_pasien:
                return idx, pasien
        print(f'Pasien dengan ID {id_pasien} tidak ditemukan. Silakan coba lagi.')

# 1. Rekap data pasien (Read)
def rekap_data_pasien(data_pasienRS):
    print('Rekap data pasien:')
    print(tabulate(data_pasienRS, headers='keys', tablefmt='pretty'))

# 2. Registrasi pasien (Create)
def registrasi():
    nama = input_nama('Nama Pasien\t: ')
    tanggal_lahir = input_tanggal('Tanggal lahir (dd-mm-yyyy): ', max_date=tanggal_hari_ini)
    tanggal_sakit = input_tanggal('Tanggal mulai sakit (dd-mm-yyyy): ',min_date=tanggal_lahir, max_date=tanggal_hari_ini)
    tanggal_kunjungan = tanggal_hari_ini.strftime('%d %B %Y')
    jkelamin = input_jenis_kelamin('Jenis Kelamin (L/P)\t: ')
    domisili = input_nama('Domisili\t: ')
    diagnosis = input_nama('Diagnosis: ')
    nohp = input_nohp('Nomor HP Wali: ')

    tahun, bulan = hitung_umur(tanggal_lahir, tanggal_hari_ini)

    id_pasien_baru = id_pasien(nama)
    dataregistrasi = {
        'ID': id_pasien_baru,
        'Nama Pasien': nama,
        'Umur': f'{tahun} tahun {bulan} bulan',
        'Nomor HP Wali': nohp,
        'Jenis Kelamin': jkelamin,
        'Domisili': domisili,
        'Tanggal Sakit': tanggal_sakit.strftime('%d %B %Y'),
        'Tanggal Kunjungan': tanggal_kunjungan,
        'Diagnosis': diagnosis
        }

    data_pasienRS.append(dataregistrasi)
    print(f'\nPasien {nama} telah terdaftar dengan ID: {id_pasien_baru}\n')

# 3. Perbaharui data pasien (Update)
def perbaharui_data():
    hasil_pencarian = cari_data_nama('Nama Pasien yang ingin diperbaharui (Ketik "exit" untuk keluar): ')
    if not hasil_pencarian:
        return
    konfirmasi = validasi('Apakah Anda ingin diperbaharui data ini? (ya/tidak): ')
    if not konfirmasi:
        return

    idx, pasien = cari_id_pasienRS('Masukkan ID Pasien: ')
    print('Data Pasien yang akan diperbaharui:')
    print(tabulate([pasien], headers='keys', tablefmt='pretty'))

    while True:
        print('''\nPilih data yang ingin diperbaharui:
            1. Nama Pasien
            2. Tanggal lahir (dd-mm-yyyy)
            3. Jenis Kelamin
            4. Domisili
            5. Nomor HP Wali
            6. Tanggal Sakit (dd-mm-yyyy)
            7. Diagnosis
            8. Keluar
        ''')
        pilihan = input_angka('Masukkan pilihan (1-8): ')

        if pilihan == 1:
            data_pasienRS[idx]['Nama Pasien'] = input_nama('Nama Pasien: ')
        elif pilihan == 2:
            tanggal_lahir = input_tanggal('Tanggal lahir (dd-mm-yyyy): ', max_date=datetime.today())
            tahun, bulan = hitung_umur(tanggal_lahir, datetime.today())
            data_pasienRS[idx]['Umur'] = f'{tahun} tahun {bulan} bulan'
        elif pilihan == 3:
            data_pasienRS[idx]['Jenis Kelamin'] = input_jenis_kelamin('Jenis Kelamin (L/P): ')
        elif pilihan == 4:
            data_pasienRS[idx]['Domisili'] = input_huruf('Domisili: ')
        elif pilihan == 5:
            data_pasienRS[idx]['Nomor HP Wali'] = input_nohp('Nomor HP Wali: ')
        elif pilihan == 6:
            data_pasienRS[idx]['Tanggal Sakit'] = input_tanggal('Tanggal Sakit (dd-mm-yyyy): ', max_date=datetime.today()).strftime('%d %B %Y')
        elif pilihan == 7:
            data_pasienRS[idx]['Diagnosis'] = input_huruf('Diagnosis: ')
        elif pilihan == 8:
            break
        else:
            print('Pilihan tidak valid.')
            continue
        print(f'\nData pasien dengan ID {data_pasienRS[idx]["ID"]} berhasil diperbaharui.')
        ulangi = input('Apakah Anda ingin mengulangi pembaruan data? (ya/tidak): ').lower()
        if ulangi != 'ya':
            break

# 4. Hapus data pasien (Delete)
def hapus_data():
    while True:
        hasil_pencarian = cari_data_nama('Nama Pasien yang ingin dihapus (Ketik "exit" untuk keluar): ')
        if not hasil_pencarian:
            return
        idx, pasien = cari_id_pasienRS('Masukkan ID Pasien yang akan dihapus: ')
        if not pasien:
            return

        print('Data Pasien yang akan dihapus:')
        print(tabulate([pasien], headers='keys', tablefmt='pretty'))

        konfirmasi = validasi('Apakah Anda yakin ingin menghapus data ini? (ya/tidak): ')
        if konfirmasi:
            data_sampah.append(data_pasienRS.pop(idx))
            print(f'\nData pasien dengan ID {pasien["ID"]} berhasil dihapus.')
        else:
            print('Penghapusan data dibatalkan.')

        print('\nData pasien terupdate:')
        print(tabulate(data_pasienRS, headers='keys', tablefmt='pretty'))

        ulangi = validasi('\nApakah Anda ingin menghapus data lagi? (ya/tidak): ')
        if not ulangi:
            break

# 5. Pemulihan/restore data pasien
def pemulihan_data():
    print('Data Sampah:')
    if not data_sampah:
        print('Data sampah kosong.')
        return
    else:
        print(tabulate(data_sampah, headers='keys', tablefmt='pretty'))

    while True:
        hasil_pencarian = cari_data_sampah('Nama Pasien yang ingin di-restore (Ketik "exit" untuk keluar): ')
        if not hasil_pencarian:
            return
        idx, pasien = cari_id_sampah('Masukkan ID Pasien yang akan direstore: ')
        if not pasien:
            return

        konfirmasi = validasi('Apakah Anda yakin ingin me-restore data ini? (ya/tidak): ')
        if konfirmasi:
            data_pasienRS.append(data_sampah.pop(idx))
            print(f'\nData pasien dengan ID {pasien["ID"]} berhasil di-restore.')
        else:
            print('Penghapusan data dibatalkan.')

        print('\nData sampah terupdate:')
        if not data_sampah:
            print('Data sampah kosong.')
        else:
            print(tabulate(data_sampah, headers='keys', tablefmt='pretty'))

        ulangi = validasi('\nApakah Anda ingin me-restore data lagi? (ya/tidak): ')
        if not ulangi:
            break

# 6. Urutkan data pasien
def urutkan_data():
    print('Data pasien sebelum diurutkan:')
    print(tabulate(data_pasienRS, headers='keys', tablefmt='pretty'))

    while True:
        print('''Pilih kriteria untuk mengurutkan data:
                1. Berdasarkan Nama Pasien
                2. Berdasarkan Umur
                3. Berdasarkan Tanggal Sakit
            ''')
        pilihan = input("Masukkan pilihan (1/2/3) atau ketik 'exit' untuk keluar:" )
        if pilihan.lower().strip() == 'exit':
            break

        if pilihan == '1':
            sorted_data = sorted(data_pasienRS, key=lambda x: x['Nama Pasien'])
        elif pilihan == '2':
            sorted_data = sorted(data_pasienRS, key=lambda x: int(x['Umur'].split()[0]))  # Mengambil tahun dari string umur
        elif pilihan == '3':
            sorted_data = sorted(data_pasienRS, key=lambda x: datetime.strptime(x['Tanggal Sakit'], '%d %B %Y'))
        else:
            print('Pilihan tidak valid.')
            continue

        print('Data pasien setelah diurutkan:')
        print(tabulate(sorted_data, headers='keys', tablefmt='pretty'))

# 7. Filter data pasien
def filter_data():
    while True:
        filter_by = input('''Filter data pasien (ketik: Nama/diagnosis/domisili) atau 'exit' untuk keluar: ''').lower().strip()
        if filter_by.strip().lower() == 'exit':
            break
        if filter_by == 'diagnosis':
            keyword = input_huruf('Masukkan diagnosis untuk mencari (cth:demam): ')
            filtered_data = [pasien for pasien in data_pasienRS if keyword.lower() in pasien['Diagnosis'].lower()]
            if not filtered_data:
                print(f'Pasien dengan diagnosis {keyword} tidak ditemukan.')
        elif filter_by == 'domisili':
            keyword = input_huruf('Masukkan domisili untuk mencari (cth:solo): ')
            filtered_data = [pasien for pasien in data_pasienRS if keyword.lower() in pasien['Domisili'].lower()]
            if not filtered_data:
                print(f'Pasien dengan domisili {keyword} tidak ditemukan.')
        elif filter_by == 'nama':
            keyword = input_huruf('Masukkan Nama Pasien untuk mencari (cth: jojo): ')
            filtered_data = [pasien for pasien in data_pasienRS if keyword.lower() in pasien['Nama Pasien'].lower()]
            if not filtered_data:
                print(f'Pasien dengan nama {keyword} tidak ditemukan.')
        else:
            print('Pilihan filter tidak valid.')
            continue

        print('Hasil filter:')
        print(tabulate(filtered_data, headers='keys', tablefmt='pretty'))

# Fungsi untuk menampilkan menu utama
def menu_utama():
    global tanggal_hari_ini
    tanggal_hari_ini = datetime.today().date()

    while True:
        print(''' \n**Sistem Manajemen Data Pasien RS Purwadhika**
            1. Rekap data pasien (Read)
            2. Registrasi pasien (Create)
            3. Perbaharui data pasien (Update)
            4. Hapus data pasien (Delete)
            5. Pemulihan/re-store data pasien
            6. Urutkan data pasien
            7. Filter data pasien
            8. Keluar
            ''')
        pilih_menu = input_angka('Pilih menu: ')
        if pilih_menu == 1:
            rekap_data_pasien(data_pasienRS)
        elif pilih_menu == 2:
            registrasi()
        elif pilih_menu == 3:
            perbaharui_data()
        elif pilih_menu == 4:
            hapus_data()
        elif pilih_menu == 5:
            pemulihan_data()
        elif pilih_menu == 6:
            urutkan_data()
        elif pilih_menu == 7:
            filter_data()
        elif pilih_menu == 8:
            break
        else:
            print('Menu yang tersedia hanya 1-8')


menu_utama()

