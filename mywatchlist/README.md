# Aplikasi
- Aplikasi ini memiliki link sebagai berikut:
[Link PBP-Tugas3-Ivan](http://ivanrbnc-pbp-tugas2.herokuapp.com/mywatchlist/)

# Jawaban dari pertanyaan yang telah diberikan

### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
- HTML memiliki perbedaan yang cukup mencolok dibandingkan JSON dan XML. HTML adalah data yang menjadi landasan suatu web, sedangkan JSON dan XML adalah data yang digunakan untuk pertukaran data dari server ke *client*, *vice versa*, dimana keduanya berbentuk hierarkis.
- JSON dan XML memiliki sintaks yang berbeda, seperti JSON tidak menggunakan *end tag*
- XML perlu diurai dengan *XML parser*, sedangkan JSON perlu diurai menggunakan *standard JavaScript function*. Oleh karena itu, ketika seseorang membuat web yang menggunaan JS, JSON lebih mudah untuk diterapkan.

### 2. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?
Pada dasarnya, ketika *client* mengakses suatu server, hal yang umum terjadi adalah perpindahan data dari server ke *client*. Salah satu kegunaan *data delivery* di tugas kali ini adalah menangkap elemen-elemen web. Dengan diperbolehkannya *data delivery*, salah satu manfaat lainnya adalah penggunaan server sebagai pusat data sehingga distribusi data dapat berjalan lebih mudah.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
1.  Mula-mula, saya perlu membuat aplikasi baru pada proyek di repositori tugas 2 dan melakukan pengaturan dasar, seperti menyambungkan **urls.py** di project_django dan mengisi aplikasi mywatchlist di pengaturan project_django.
2. Setelah itu, saya memodelkan data yang akan ditampilkan melalui **models.py**, seperti mengatur variabel *rating* sebagai *float* dan lainnya.
3. Melakukan migrasi sehingga model tersebut tersedia pada *database* Django lokal.
4. Membuat dan mengisi file JSON pada fixtures sesuai sintaks dan elemen yang dibutuhkan.
5. Melakukan loaddata di file JSON. Di akhir, saya juga perlu melakukan loaddata di Heroku karena sempat tidak termuat.
6. Menyambungkan **models.py** dengan **views.py** melalui fungsi show_watchlist yang akan menangkap data objek-objek JSON dan elemen yang diinginkan untuk muncul pada HTML, lalu melakukan *rendering* terhadap HTML tersebut.
7. Menambahkan fungsi lain, seperti show_xml, show_json, dan which_message (*bonus*). Fungsi show_xml dan show_json akan memetakan data dari JSON dengan bantuan HttpResponse dan serializers. Fungsi which_message akan menangkap variabel "*watched*" pada tiap objek JSON dan menghitung banyaknya *True False* yang muncul. Setelah itu, fungsi which_message akan mengembalikan string berisi pesan yang diinginkan.
8. Melakukan *routing* melalui **urls.py** dimana saya menambahkan url cabang tambahan, seperti /xml/, /json/, dan /html/. Tiap routing tersebut juga dilengkapi fungsi dari **views.py** sesuai kebutuhan.
9. Saya melakukan *deployment* dengan cara yang sama seperti sebelumnya, yaitu *add*, *commit*, dan *push* ke Github. Setelah itu, Github tersebut akan disambungkan dengan Heroku menggunakan API Key dan API App Name yang sesuai.
10. Di akhir, saya juga melakukan tes jalannya website melalui Postman dan **tests.py** dimana **tests.py** diisi dengan mengecek apakah *routing* bersangkutan dapat responsif. 

### *Screenshot* pengaksesan website melalui Postman

![Screenshot melalui postman 1 - URL HTML](/static/assets/mywatchlist-html.PNG)
![Screenshot melalui postman 2 - URL XML](/static/assets/mywatchlist-xml.PNG)
![Screenshot melalui postman 3 - URL JSON](/static/assets/mywatchlist-json.PNG)