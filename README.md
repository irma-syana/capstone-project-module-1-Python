### capstone project module 1 Python
# Sistem Manajemen Data Pasien Rumah Sakit

## Gambaran Umum
Proyek ini adalah aplikasi berbasis Python yang dirancang untuk mengelola informasi/data pasien rumah sakit secara efisien dan digunakan oleh administrasi RS. Aplikasi ini menggunakan operasi CRUD (Create, Read, Update, Delete) dan dua fitur tambahan (filter, sorting, dan pemulihan data terhapus) untuk menyediakan sistem yang komprehensif dalam mengelola catatan pasien.

## Fitur
1. Rekap Data Pasien (Read): Menampilkan semua data pasien yang terdaftar.
2. Registrasi Pasien (Create): Menambah data pasien baru.
3. Perbaharui Data Pasien (Update): Memperbaharui informasi pasien yang sudah terdaftar.
4. Hapus Data Pasien (Delete): Menghapus data pasien dari daftar.
5. Pemulihan Data Pasien (Restore): Mengembalikan data pasien yang telah dihapus.
6. Urutkan Data Pasien: Mengurutkan data pasien berdasarkan nama, umur, atau tanggal sakit.
7. Filter Data Pasien: Memfilter data pasien berdasarkan nama, diagnosis, atau domisili.
   
## Instalasi
Pastikan Anda memiliki Python terinstal di sistem Anda. Kemudian, instal paket yang diperlukan dengan menjalankan perintah berikut:

     pip install regex tabulate

## Penggunaan
1. Unduh file kode.
2. Jalankan skrip menggunakan perintah: python nama_file.py
3. Ikuti instruksi yang muncul di layar untuk menggunakan fitur-fitur yang tersedia.

## Struktur Tabel Data Pasien
Aplikasi ini menggunakan tabel untuk menyimpan dan menampilkan data pasien. Berikut adalah struktur tabel yang digunakan:

      Kolom                Deskripsi 
    -------               ------------------------------------------------------------------------------------
        ID                 ID unik untuk setiap pasien yang terdiri dari tiga huruf pertama nama dan nomor urut 
        Nama               Pasien	Nama lengkap pasien
        Umur               Umur pasien dalam format "tahun bulan"
        Jenis Kelamin      Jenis kelamin pasien, 'L' untuk laki-laki, 'P' untuk perempuan
        Domisili	       Tempat tinggal pasien.
        Nomor HP Wali      Nomor telepon wali pasien.
        Tanggal Sakit      Tanggal mulai sakit pasien dalam format "dd Month yyyy".
        Tanggal Kunjungan   Tanggal kunjungan ke rumah sakit dalam format "dd Month yyyy".
        Diagnosis	         Diagnosis medis pasien.
    

## Struktur Kode
1. Fungsi Input: Berbagai fungsi input untuk validasi data pengguna seperti angka, huruf, nama, tanggal, jenis kelamin, dan nomor HP.
2. CRUD:
   - 'rekap_data_pasien()' : Menampilkan semua data pasien.
   - 'registrasi()' : Menambah data pasien baru.
   - 'perbaharui_data()': Memperbaharui data pasien yang ada.
   - hapus_data(): Menghapus data pasien dan memindahkannya ke tempat sampah sementara.
   - pemulihan_data(): Memulihkan data pasien yang dihapus.
3. Fitur Tambahan:
   - 'urutkan_data(): Mengurutkan data pasien berdasarkan kriteria tertentu.
   - filter_data(): Memfilter data pasien berdasarkan kriteria tertentu.
4. Menu Utama: Fungsi menu_utama() yang menampilkan menu interaktif bagi pengguna untuk memilih fitur yang ingin digunakan.

