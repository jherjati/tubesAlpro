# Panduan Penggunaan

Berikut adalah cara penggunaan program dalam repo ini

## Penyiapan Environment

Clone atau download repo ini dan pastikan poetry (python package manager) telah terinstall. Cara instalasi poetry dapat Anda lihat pada [poetry homepage](https://python-poetry.org/). Inisiasi dan aktifkan poetry pada root folder lalu install seluruh dependency dengan menjalankan 'poetry install' pada terminal

## Pengisian Data (Opsional)

Repo telah berisi data pada file database.db yang berjalan dalam SQLite. Namun Anda dapat bereksperimen dengan mengganti data yang ada. Caranya dengan menghapus database.db lalu jalankan 'python controller.py' pada terminal. File database.db akan muncul kembali, data akan berisi 100 struk dengan 3 daftar barang pada tiap struk, menjadikannya berjumlah 300 daftar.

## Mulai Menjalankan

Setelah environment telah siap, Anda hanya perlu menjalankan perintah 'python view.py' pada terminal.
