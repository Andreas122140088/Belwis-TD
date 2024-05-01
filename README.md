##Belwis TD

Proyek ini adalah proyek pembuatan sebuah game yang menggunakan modul pygame.
Game bertema tower defense ini mempunyai tujuan untuk mempertahankan Home player dari serangan enemy atau musuh. Untuk melindungi home, player harus menyusun sejumlah Tower yang nantinya akan menembakkan misil kepada enemy yang mengarah ke Home player. Enemy akan berjalan mengarah Home sesuai rute yang telah dibuat. Enemy akan bertambah darahnya sesuai dengan kenaikan levelnya
Dengan setiap enemy yang dihancurkan player akan mendapatkan sejumlah uang yang dapat digunakan untuk memodifikasi tower yang memiliki kemampuan khusus. Setiap musuh berhasil mencapai base maka health dari base akan berkurang dan ketika health base turun ke angka 0 maka base akan hancur dan player kalah.
 
Dependensi Paket (Library) yang Dibutuhkan Untuk Menjalankan Aplikasi
Beberapa library yang digunakan dalam pembuatan game ini antara lain:
Modul pygame
Modul os
Modul sys fungsi 'exit'
Modul random fungsi 'randint'ka
Modul math
Modul vector
Cara Bermain
Permainan dimainkan dengan mouse untuk memberikan input kepada tombol dalam game. Pada awal permainan pengguna akan ditampilkan dengan main menu dari game dan tersedia tombol untuk memulai permainan dan tombol quit untuk keluar.
Pada awal permainan pemain akan diberikan sejumlah uang untuk membeli tower basic, pemain dapat memperoleh uang tambahan dari menghancurkan musuh yang ada melalui tower yang dimilikinya. Selanjutnya pemain dapat membeli tower yang memiliki special ability dengan uang tersebut.
Permainan berakhir (game over) ketika health dari base pemain mencapai poin 0 (nol), pemain akan dialihkan ke dalam menu game over dan terdapat tombol untuk memulai permainan kembali atau kembali ke main menu.
Sedikit penjelasan:
Pygame merupakan kumpulan dari beberapa modul Python yang khusus dibuat untuk mengembangkan game, di dalam modul tersebut terdapat library simple directmedia layer yang berfungsi untuk mendukung pengembangan game.
Modul sys berfungsi untuk membantu mengakses variabel lingkungan, mengelola argumen baris perintah dan menangani eksepsi pada python.
Modul random, modul ini menyediakan berbagai fungsi yang bersifat acak, seperti memilih angka dari rentan tertentu atau pada aplikasi ini untuk memilih secara acak enemy yang akan keluar.
Modul math, modul ini digunakan untuk operasi matematika sederhana dan di dalamnya menyediakan fungsi-fungsi matematika dasar.
Modul vector 
