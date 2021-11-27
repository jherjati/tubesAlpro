import sqlite3

conn = sqlite3.connect('shop.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE T_BARANG
         (ID                        INT     NOT NULL  PRIMARY KEY,
         NAMA                       TEXT    NOT NULL,
         HARGA                      REAL    NOT NULL);''')
conn.execute('''CREATE TABLE T_STRUK
         (ID                     INT            NOT NULL    PRIMARY KEY,
         TANGGAL_PEMBUATAN       DATETIME       NOT NULL,
         TOTAL_PEMBELIAN         REAL           NOT NULL,
         TOTAL_PEMBAYARAN        REAL           NOT NULL,
         KEMBALIAN               REAL           NOT NULL);''')
conn.execute('''CREATE TABLE T_DAFTAR
         (ID_BARANG                 INT    NOT NULL,
         ID_STRUK                   INT    NOT NULL,
         JUMLAH_BARANG              INT    NOT NULL,
         SUBTOTAL                   REAL   NOT NULL);''')
print("Table created successfully")

conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (1, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (2, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (3, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (4, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (5, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (6, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (7, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (8, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (9, 'Pepsodent',9000 )")
conn.execute("INSERT INTO T_BARANG (ID,NAMA,HARGA) \
      VALUES (10, 'Pepsodent',9000 )")

conn.commit()
print("Records created successfully")

conn.close()
