# Aplikasi
- Aplikasi ini memiliki link sebagai berikut:
[Link PBP-Tugas4/5-Ivan](http://ivanrbnc-pbp-tugas2.herokuapp.com/todolist/)

# Jawaban dari pertanyaan yang telah diberikan (Tugas 4)

### 1. Apa kegunaan **{% csrf_token %}** pada elemen **<form>**? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen **<form>**?

**csrf_token** berguna untuk memvalidasi bahwa user tertentu telah benar-benar melakukan kegiatan yang menyangkut pada token tersebut. Untuk form, **csrf_token** digunakan untuk menyatakan bahwa registrasi user dengan username dan password tertentu telah terjadi dengan bukti token terkait. Ketika **csrf_token** tidak tersedia, server tidak dapat memvalidasi kegiatan yang telah dilakukan. Oleh karena itu, registrasi atau pun kegiatan yang menggunakan **csrf_token** akan mengalami error.

### 2. Apakah kita dapat membuat elemen **<form>** secara manual (tanpa menggunakan *generator* seperti **{{ form.as_table }}**)? Jelaskan secara gambaran besar bagaimana cara membuat **<form>** secara manual.

*Form* yang dibuat melalui *generator* telah tersedia secara *built-in* oleh Django. Pembuatan *form* secara manual tentunya dapat dilakukan. Gambaran besar terkait pembuatannya adalah dengan melakukan *override* terhadap *method-method* terkait, seperti **form.save()**. *Override* yang dilakukan akan "mengganti" *default form* yang telah dimiliki Django. Dengan ini, *override* memperbolehkan *programmer* untuk mengkreasikan *form* manual yang ingin dibuatnya.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada *database*, hingga munculnya data yang telah disimpan pada *template* HTML.

1. Menangkap *input* yang diberikan *user* sebagai data yang akan diolah
2. Data tersebut ditangkap dan disimpan pada *database* oleh fungsi yang menjalankan aktivitas tersebut, misal *input* data dari **create.html** akan ditangkap oleh fungsi **ask_todo_creation(request)** dari **views.py**.
3. Data yang telah ditangkap akan diolah sesuai kebutuhan.
4. Setelah pengolahan telah dilakukan, data tersebut akan dilemparkan atau di-*render* pada **html** terkait.
5. *Render* yang telah terjadi akan menampilkan data tersebut.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.

1.  Mula-mula, saya perlu membuat aplikasi baru pada proyek di repositori tugas 2 dan melakukan pengaturan dasar, seperti menyambungkan **urls.py** di project_django dan mengisi aplikasi todolist di pengaturan project_django.
2. Setelah itu, saya memodelkan data yang akan ditampilkan melalui **models.py**, seperti mengatur variabel *date* sebagai *DateField* yang disesuaikan dengan kebutuhan dan variabel-variabel lainnya.
3. Melakukan migrasi sehingga model tersebut tersedia pada *database* Django lokal.
4. Menyediakan *path* di **urls.py** untuk menampung kebutuhan-kebutuhan aktivitas yang dilakukan, seperti registrasi, *login*, *logout*, penambahan *task*, dan penampilan *task*.
5. Mengonfigurasi fungsi-fungsi yang dibutuhkan agar aktivitas yang disebutkan sebelumnya dapat terjadi, serta tidak lupa untuk menambahkan **@login_required** pada fungsi yang memaksa *user* telah melakukan *login*.
6. Pembuatan *template* dari **html** yang dibutuhkan. Mulai dari komponen-komponen yang akan ditampilkan, tombol, *input*, dan lain sebagainya. Pastikan tiap elemen yang mengarah ke *template* lain dan/atau menjalankan fungsi untuk dikonfigurasi dengan benar.
7. *Deployment* yang dilakukan bersifat otomatis karena telah dilakukan pada tugas sebelumnya.

# Jawaban dari pertanyaan yang telah diberikan (Tugas 5)

### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing *style*?

- Internal CSS : Meletakkan CSS pada <style></style> yang terdapat di <head></head> suatu HTML. Kelebihan yang diberikan adalah keefektivitasan metode untuk halaman spesifik. Metode ini tidak efektif ketika seseorang ingin merancang HTML dengan *style* yang sama dengan file HTML lainnya karena harus mengulangi kodenya. Selain itu, ketika halaman yang diberi internal CSS dimuat, halaman cenderung akan memakan waktu lebih lama.

- External CSS : Membuat file dengan extension .css dan meletakkan seluruh kode CSS di dalamnya. Dengan ini, kelebihan yang didapat adalah kemudahan dalam menghias HTML dalam jumlah banyak. Dikarenakan oleh file CSS yang terpisah dengan HTML, halaman terkait memiliki kemungkinan untuk tidak *render* dengan sempurna hingga file CSS benar-benar termuat.

- Inline CSS : Menambahkan *style* langsung pada elemen tertentu di suatu HTML. Kelebihan dari Inline CSS sendiri adalah kemudahan dalam aktivitas *testing*. Pemberian *style* satu per satu untuk tiap elemen tentunya memakan waktu lama sehingga Inline CSS tidak direkomendasikan kegunaannya secara umum. 

### 2. Jelaskan tag HTML5 yang kamu ketahui.

- <head> : kepala HTML
- <body> : isi HTML
- <a> : hyperlink
- <b> : bold
- <button> : tombol
- <div> : divisi atau bagian
- <form> : formulir user input
- <h1> s. d. <h6> : heading besar hingga kecil
- <i> : italic
- <img> : gambar
- <input> : user input spesifik
- <label> : label untuk deskripsi input
- <nav> : navigation bar
- <p> : paragraf
- <span> : bagian kecil dari div
- <style> : informasi dari dekorasi yang ingin diberikan
- <table> : tabel
- <th> : kolom dari suatu tabel
- <tr> : baris dari suatu tabel
- <title> : judul dari HTML
- <u> : garis bawah

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- "*" : seluruh elemen
- .class : seluruh class dengan nama yang diinginkan
- element : seluruh elemen yang diinginkan
- element1 element2 : elemen2 dari suatu elemen1 yang diinginkan
- ::before : konten sebelum bertemu elemen yang ditentukan
- ::after : konten setelah bertemu elemen yang ditentukan
- :hover : ketika mouse berada pada elemen yang ditentukan
- :-nth-child(n) : menangkap anak elemen ke-n dari suatu elemen
- ::placeholder : elemen input dengan atribut "placeholder"

### 4. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.

1. Memberi bootstrap pada tiap file HTML sehingga halaman menjadi responsif
2. Mencari referensi yang cocok untuk dimasukkan pada file HTML yang diinginkan
3. Mengaplikasikan referensi-referensi tersebut sehingga *checklist* terpenuhi, mulai dari cards, dekorasi, dan lain sebagainya