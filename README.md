# Script Pengunjung Otomatis (Visitor-Badge Hitter)

## 🎯 Gambaran Umum

Script ini adalah utilitas Python sederhana yang dirancang untuk mengirimkan sejumlah permintaan HTTP GET ke URL tertentu secara berulang. Tujuan utamanya adalah untuk secara otomatis menaikkan hit atau jumlah kunjungan pada layanan lencana (badge) pengunjung, seperti `visitor-badge.laobi.icu`.

## 🛠️ Persyaratan

Sebelum menjalankan script, pastikan Anda telah menginstal pustaka **`requests`**. Pustaka ini menangani semua permintaan HTTP yang diperlukan oleh script.

Anda dapat menginstalnya dengan perintah berikut di terminal Anda:

```bash
pip install requests
```

Pustaka **`time`** adalah pustaka standar Python dan tidak memerlukan instalasi tambahan.

## 🚀 Cara Menggunakan

1.  **Buka file script** dengan editor teks pilihan Anda.
2.  **Ubah variabel berikut** sesuai kebutuhan Anda:
      - `url`: Ganti dengan URL lencana pengunjung yang ingin Anda hit. URL target dalam kode ini adalah `https://visitor-badge.laobi.icu/badge?page_id=gcarlo11.gcarlo11`.
      - `total_hits`: Ubah nilai `1000` menjadi jumlah total hit yang Anda inginkan.
      - `delay`: Ubah nilai `0.1` menjadi jeda dalam detik antara setiap hit. Jeda ini penting untuk menghindari membebani server target dan mengurangi risiko pemblokiran.
3.  **Simpan perubahan** pada file.
4.  **Jalankan script** dari terminal Anda:
    ```bash
    python nama_file_anda.py
    ```

## 💻 Cara Kerja Kode

Script ini bekerja dengan alur sebagai berikut:

1.  Mengimpor pustaka `requests` untuk permintaan HTTP dan pustaka `time` untuk fungsi jeda.
2.  Mendefinisikan variabel konfigurasi: `url`, `total_hits`, dan `delay`.
3.  Memulai perulangan `for` yang akan berjalan sebanyak `total_hits` kali.
4.  Di setiap iterasi, script mencoba mengirimkan permintaan **GET** ke `url` yang telah ditentukan.
5.  Setelah menerima respons, script akan mencetak pesan status:
      - Jika kode statusnya `200`, artinya permintaan **sukses**.
      - Jika kode statusnya bukan `200`, artinya permintaan **gagal**, dan script akan menampilkan kode status tersebut.
6.  Setelah setiap permintaan, script akan berhenti sejenak selama `delay` detik menggunakan `time.sleep()`.
7.  Blok `try...except` digunakan untuk menangani potensi kesalahan (misalnya, masalah koneksi jaringan) dan mencegah script berhenti secara tiba-tiba.
