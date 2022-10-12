# Aplikasi
- Aplikasi ini memiliki link sebagai berikut:
[Link PBP-Tugas6-Ivan](http://ivanrbnc-pbp-tugas2.herokuapp.com/todolist/)

# Jawaban dari pertanyaan yang telah diberikan (Tugas 4)

### 1. Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.
Perbedaan utama yang dimiliki oleh *synchronous* dan *asynchronous* adalah waktu. *Synchronous*, berarti berkaitan dengan waktu. *Synchronous programming* adalah kegiatan membuat program dengan berpacu pada waktu. Secara sederhana, ketika seorang *programmer* melakukan *synchronous programming*, maka mereka akan mengerjakan task yang dimilikinya satu per satu. Berkebalikan dengan itu, *asynchronous programming* akan menyelesaikan tugas secara paralel. 

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *Event-Driven Programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Sesuai pada namanya, *event-driven programming* adalah pemrograman berbasis *event*. Pada konteks materi kali ini, *event* adalah aksi yang diberikan oleh *user* sehingga ketika aksi tersebut terjadi, maka program akan mengeksekusi suatu fungsi sesuai aksi yang dilakukan. Contoh penerapan yang dimiliki tugas ini adalah submit button. Ketika *user* menekan tombol submit, maka program akan menjalankan fungsi yang akan membuat isi *user* menjadi data.

### 3. Jelaskan penerapan *asynchronous programming* pada AJAX.
Penerapan *asynchronous programming* pada AJAX memperbolehkan *user* untuk melihat perubahan yang terjadi tanpa melakukan *refresh* pada browser. Hal ini dapat terjadi karena HTML yang dimiliki sudah memuat data sehingga user tidak perlu me-*refresh*. Meskipun begitu, data yang diberi user tetap dipindahkan ke server secara tidak terlihat.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
1. Menambahkan fungsi pada **views.py** dan menyambungkannya melalui **urls.py**
2. Membuat *modals* yang isinya adalah *form* dari **create.html**
3. Membuat fungsi AJAX GET untuk menangkap data dari server, serta membuat fungsi *refresh* secara *asynchronous*
4. Membuat fungsi AJAX POST untuk menyimpan data secara *asynchronous*
5. Menyambungkan fungsi-fungsi AJAX yang terjadi antara **views.py** dan **todolist.html**