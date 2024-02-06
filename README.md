# ReChefy

ReChefy merupakan aplikasi berbasis desktop yang hadir sebagai teman memasak Anda. Bersama ReChefy, Anda dapat memasak dengan lebih mudah dengan adanya fitur untuk melihat resep masakan. Anda juga dapat menambahkan resep pada aplikasi, serta menyunting dan menghapus resep buatan Anda. ReChefy juga dapat meningkatkan pengalaman memasak Anda dengan adanya fitur komentar pada setiap resep, sehingga Anda dapat memberikan catatan mengenai resep-resep pada aplikasi. Selain itu, ReChefy juga dilengkapi dengan kumpulan artikel memasak yang dapat Anda baca.

## Daftar Isi
* [Cara Menjalankan Aplikasi](#cara-menjalankan-aplikasi)
* [Struktur Program](#struktur-program)
* [Daftar Modul yang Diimplementasikan](#daftar-modul-yang-diimplementasikan)
* [Daftar Tabel Basis Data yang Diimplementasikan](#daftar-tabel-basis-data-yang-diimplementasikan)
* [Anggota Kelompok dan Pembagian Tugas](#anggota-kelompok-dan-pembagian-tugas)
* [Notes](#notes)

## Cara Menjalankan Aplikasi
1. Clone repository dengan menjalankan perintah ```git clone git@gitlab.informatika.org:Raylouis/if2250-2023-k01-11-rechify.git``` pada terminal.
2. Install requirements.txt pada repository dengan menjalankan perintah ```pip install -r requirements.txt``` pada terminal.
3. Pada directory repository, jalankan perintah ```./run.bat``` pada terminal.
4. Aplikasi ReChefy sudah dapat Anda gunakan.

## Struktur Program
``` bash
.
│   .gitignore
│   .gitlab-ci.yml
│   .pylintrc
│   README.md
│   requirements.txt
│   run.bat
│
└───src
    │   application.py
    │   addResep.py
    │   controller.py
    │   daftarArtikel.py
    │   daftarResep.py
    │   editResep.py
    │   fontLoader.py
    │   lihatArtikel.py
    │   lihatResep.py
    │   main.py
    │   menu.py
    │   warning.py
    │   welcomePage.py
    │   
    ├───database
    │       databaseFunc.py
    │       rechefy.db
    │       
    └───tests
            test.db
            testAddResep.py
            testDaftarArtikel.py
            testDaftarResep.py
            testEditResep.py
            testLihatArtikel.py
            testLihatResep.py
            testDatabaseFunc.py
```        

## Daftar Modul yang Diimplementasikan
### Welcome Page
Berikut adalah tampilan dari Welcome Page
![welcomePage](/uploads/c64220576df99c50c08640f13327a747/welcomePage.jpg)

### Menu
Berikut adalah tampilan dari Menu
![menu](/uploads/36c8033d575dd91d4ddc96132830d43a/menu.jpg)

### Daftar Artikel
Berikut adalah tampilan dari Daftar Artikel
![daftarArtikel](/uploads/52e1ae436769bba26da49801857a24d3/daftarArtikel.jpg)

### Lihat Artikel
Berikut adalah tampilan dari Lihat Artikel
![lihatArtikel](/uploads/e1660302d7b4c8490013a3205398cd09/lihatArtikel.jpg)

### Daftar Resep
Berikut adalah tampilan dari Daftar Resep
![daftarResep](/uploads/0e488a43d6e7178d525a380fe23dedf2/daftarResep.jpg)
![cariResepFound](/uploads/ce4b623a7ccc39949353738a57f1801f/cariResepFound.jpg)
![cariResepNotFound](/uploads/b6efb6c98d81987a71d6649fd80444c5/cariResepNotFound.jpg)

### Lihat Resep
Berikut adalah tampilan dari Lihat Resep
![lihatResepDefault](/uploads/692f2a537d17ca6c21c58aba3a4c59e4/lihatResepDefault.jpg)
![lihatResepResepku](/uploads/d4c16919f004e21e6f3462327ec60f63/lihatResepResepku.jpg)

### Tambah Resep
Berikut adalah tampilan dari Tambah Resep
![tambahResep](/uploads/4512269cc4ea6459309164bba8bc6fe5/tambahResep.jpg)

### Sunting Resep
Berikut adalah tampilan dari Sunting Resep
![suntingResep](/uploads/3036615c2c66234458b0d9474340b367/suntingResep.jpg)


## Daftar Tabel Basis Data yang Diimplementasikan
### Resep
| Atribut | Tipe | Key | Constraint |
|---------|------| ----|------------|
| idResep | integer | primary key | autoincrement, not null |
| gambarMasakan| blob | | not null |
| namaMasakan | text | | not null|
| deskripsiMasakan| text|| not null|
| langkahMemasak|text||not null|
| isDefault|integer||not null, default 0, isDefault = 0 or isDefault = 1|

### Bahan
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idBahan|integer|primary key|autoincrement, not null|
|namaBahan|text||not null|

### Alat
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idAlat|integer|primary key|autoincrement, not null|
|namaAlat|text||not null|

### AlatResep
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idResep|integer|primary key, foreign key references Resep(idResep)|not null|
|idAlat|integer|primary key, foreign key references Alat(idAlat)|not null|

### BahanResep
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idResep|integer|primary key, foreign key references Resep(idResep)|not null|
|idBahan|integer|primary key, foreign key references Bahan(idBahan)|not null|
|kuantitasBahan|real||not null|
|satuanKuantitasBahan|text||not null|

### Komentar
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idKomentar|integer|primary key|autoincrement, not null|
|komentarFoto|blob||not null|
|komentarTeks|text||not null|
|tanggalKomentar|text||not null|
|idResep|integer|foreign key references Resep(idResep)|not null|

### Artikel
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idArtikel|integer|primary key|autoincrement, not null|
|fotoArtikel|blob||not null|
|judulArtikel|text||not null|
|isiArtikel|text||not null|
|tanggalPublikasi|text||not null|

## Anggota Kelompok dan Pembagian Tugas
|NIM|Nama|Tugas|
|-|-|-|
|13521059|Arleen Chrysantha Gunardi|Daftar Artikel, Daftar Resep|
|13521127|Marcel Ryan Antony|database, ci cd, query|
|13521143|Raynard Tanadi|Lihat Resep, Lihat Artikel|
|13521145|Kenneth Dave Bahana|Welcome Page, Tambah Resep, Edit Resep|

## Notes
Pada bagian ci cd kami yaitu tepatnya pada stage Test unit testing kami selalu _failed_ dikarenakan error dari gitlabnya. Kami juga tidak mengetahui mengapa gitlab mengeluarkan error yang berupa **ImportError: libGL.so.1: cannot open shared object file: No such file or directory**. Dimana apabila kami jalankan unit testing di local kami unit testing tetap berjalan normal dan testing seluruh bagian berhasil, berikut buktinya :
![unittest](/uploads/310ac6e4314f60310420e093e0196428/unittest.jpg)
