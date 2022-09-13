# Aplikasi
Aplikasi dari repo ini memiliki link sebagai berikut
[Link PBP-Tugas2-Ivan](http://ivanrbnc-pbp-tugas2.herokuapp.com/katalog/)

# Jawaban dari pertanyaan yang telah diberikan

### 1. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara **urls.py**, **views.py**, **models.py**, dan berkas **html**;

![Bagan MVT](/Bagan%20MVT.png)

1. Mula-mula, proses pertama yang dilakukan adalah mengarahkan permintaan *client* atau *user* ke **urls.py**. 
2. Dari urls akan diteruskan ke **views.py** untuk pemilihan bentuk web yang ingin ditampilkan. Di dalam views, seorang pengembang sudah menyiapkan elemen-elemen yang akan disisipkan ke dalam html. 
3. Views akan meminta kebutuhan sumber daya kepada **models.py** terkait html yang akan ditunjukkan.
4. Apabila terdapat permintaan yang melibatkan database, maka views akan memanggil query yang nantinya akan dikembalikan oleh **database** melalui models. 
5. Setelah kebutuhan yang dibutuhkan oleh views terpenuhi, views akan meneruskan elemen-elemen tadi kepada **html** yang bersangkutan.
6. Html yang sudah sesuai keinginan pengembang akan ditampilkan kembali ke *client*.

### 2. Jelaskan kenapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?

*Virtual environment* berguna untuk memisahkan antara pengaturan dan *package* yang dimiliki oleh suatu proyek Django dengan proyek lainnya. Hal ini berguna agar perubahan yang dilakukan pada *virtual environment* proyek terkait tidak memengaruhi proyek lain. Oleh karena itu, alangkah baiknya suatu proyek Django memerlukan *virtual environment* dalam penggunaannya. 
Aplikasi web berbasis Django tanpa *virtual environment* tetap dapat dijalankan. Namun, seluruh pengaturan dan *package* akan menyatu satu sama lain.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Cara pengimplementasian poin 1 hingga 4 (pembuatan fungsi **views.py**, *routing*, pemetaan html, dan *deployment*) mengikuti bagan MVT yang telah dijawab sebelumnya. 
Sebelum membuat fungsi pada **views.py**, saya harus membuat gerbang masuk ke dalam html yang diinginkan melalui urls. Pada urls, saya menyelipkan fungsi yang terdapat di dalam views sehingga keduanya tersambung. Fungsi yang dibuat di **views.py** adalah fungsi penangkapan data dari **models.py**. Data tersebut dimasukkan ke dalam variabel context yang nantinya akan dikirim ke template html bersangkutan (disini akan diberikan ke **katalog.html**). 
Terkait pemetaan html, perlu adanya pengubahan kode, seperti penambahan {{suatu variabel}}, di dalam **katalog.html** sehingga context yang dikirim sebelumnya dapat ditangkap. 
Deployment dilakukan pada platform Heroku. Saya hanya perlu melakukan push ke Github, lalu menyisipkan API key dan app name dan melakukan pengaturan sehingga sambungan antara Github dan Heroku terjadi.