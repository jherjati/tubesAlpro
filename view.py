from datetime import date
from sqlmodel import Session
from controller import CANCEL_STRUK, PAYMENT, engine, BEST_PRODUCT, CALCULATE_STRUK, CREATE_STRUK, DISPLAY_PEAK, DISPLAY_STRUK, INSERT


session = Session(engine)


struk = CREATE_STRUK(session=session)
INSERT(session=session, struk=struk, nama_barang="Pepsodent", jumlah_barang=2)
INSERT(session=session, struk=struk, nama_barang="Ciptadent", jumlah_barang=4)
INSERT(session=session, struk=struk, nama_barang="Rinso", jumlah_barang=3)
INSERT(session=session, struk=struk, nama_barang="Daia", jumlah_barang=1)
CALCULATE_STRUK(struk=struk)

struk = PAYMENT(session=session, struk=struk, nominal=50000)
# kalau PAYMENT berhasil struk jadi None, kalau nggak tetep struk, lihat return value fungsi di atas

struk = CANCEL_STRUK(session=session, struk=struk)
# pasti jadi null mengingat CANCEL_STRUK selalu return null


# DISPLAY_STRUK(session=session, tanggal_awal=date(
#     2021, 11, 5), tanggal_akhir=date(2021, 11, 30))
# DISPLAY_PEAK(session=session, tanggal_awal=date(2021, 11, 5))
# BEST_PRODUCT(session=session, tanggal_awal=date(2021, 11, 5))
