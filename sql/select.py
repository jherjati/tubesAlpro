import sqlite3

conn = sqlite3.connect('shop.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, nama, harga from T_BARANG")
for row in cursor:
    print("ID = ", row[0])
    print("NAMA = ", row[1])
    print("HARGA = ", row[2], "\n")

print("Operation done successfully")
conn.close()
