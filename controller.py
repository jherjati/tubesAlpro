from datetime import date
from typing import Optional
from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy import func

from models.T_Barang import T_Barang
from models.T_Struk import T_Struk
from models.T_Daftar import T_Daftar

engine = create_engine("sqlite:///database.db", echo=True)


def init():
    # Create DB and tables
    barang_1 = T_Barang(nama="Pepsodent", harga=7500)
    barang_2 = T_Barang(nama="Ciptadent", harga=5500)
    barang_3 = T_Barang(nama="Daia", harga=6500)
    barang_4 = T_Barang(nama="Rinso", harga=4500)
    barang_5 = T_Barang(nama="Sunlight", harga=5000)

    # struk_1 = T_Struk()

    SQLModel.metadata.create_all(engine)

    # Create records
    with Session(engine) as session:
        session.add(barang_1)
        session.add(barang_2)
        session.add(barang_3)
        session.add(barang_4)
        session.add(barang_5)

        # session.add(struk_1)
        session.commit()


def CREATE_STRUK(session: Session):
    struk = T_Struk()
    session.add(struk)
    session.commit()
    print(
        f"CREATE_STRUK sukses. ID Struk: {struk.id}. Struk aktif: {struk.id}.")
    return struk


def INSERT(session: Session, struk: T_Struk, nama_barang: str, jumlah_barang: int):
    barang: T_Barang = session.exec(select(T_Barang).where(
        T_Barang.nama == nama_barang)).first()
    if(barang):
        struk.total_pembelian += jumlah_barang*barang.harga
        session.commit()
        print(
            f"INSERT pada struk {struk.id} sukses. Barang {nama_barang}. Jumlah barang {jumlah_barang}.")
    else:
        print('INSERT pada struk gagal. Barang tidak dikenal')


def CALCULATE_STRUK(struk: T_Struk):
    print(
        f"CALCULATE_STRUK pada struk {struk.id} berhasil. Total pembelian adalah {struk.total_pembelian}.")


def PAYMENT(session: Session, struk: T_Struk, nominal: float):
    if(nominal > struk.total_pembelian):
        struk.total_pembayaran = nominal
        struk.kembalian = nominal = struk.total_pembelian
        session.commit()
        print(
            f"PAYMENT pada struk {struk.id} berhasil. Pembayaran {nominal}. Total Pembelian {struk.total_pembelian}. Kembalian {struk.kembalian}. Struk berhasil disimpan dan dihapus dari struk aktif.")
        return None
    else:
        print(f"PAYMENT pada struk {struk.id} gagal. Pembayaran tidak cukup.")
        return struk


def CANCEL_STRUK(session: Session, struk: T_Struk):
    session.delete(struk)
    session.commit()
    struk = None


def DISPLAY_STRUK(session: Session, tanggal_awal: date, tanggal_akhir: Optional[date] = None):
    where_clause: list = [T_Struk.tanggal_pembuatan >= tanggal_awal] if tanggal_akhir == None else [
        T_Struk.tanggal_pembuatan >= tanggal_awal, T_Struk.tanggal_pembuatan <= tanggal_akhir]
    daftar_struk = session.exec(select(T_Struk).where(*where_clause))
    print("ID   Tanggal Pembuatan   Total Pembelian     Total Pembayaran    Kembalian")
    for struk in daftar_struk:
        print(f"{struk.id}  {struk.tanggal_pembuatan}   {struk.total_pembelian}     {struk.total_pembayaran}    {struk.kembalian}")


def DISPLAY_PEAK(session: Session, tanggal_awal: date, tanggal_akhir: Optional[date] = None):
    where_clause: list = [T_Struk.tanggal_pembuatan >= tanggal_awal] if tanggal_akhir == None else [
        T_Struk.tanggal_pembuatan >= tanggal_awal, T_Struk.tanggal_pembuatan <= tanggal_akhir]
    results = session.query(T_Struk.tanggal_pembuatan, func.count(
        T_Struk.tanggal_pembuatan)).where(*where_clause).group_by(T_Struk.tanggal_pembuatan)
    print("Tanggal      Jumlah Transaksi")
    for result in results:
        print(f"{result[0]}     {result[1]}")


def BEST_PRODUCT():
    return


if __name__ == "__main__":
    init()
