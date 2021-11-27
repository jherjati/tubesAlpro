import random
import typer

from datetime import date
from typing import Optional
from sqlmodel import Session, SQLModel, create_engine, select, desc, func

from model import T_Barang, T_Daftar, T_Struk

engine = create_engine("sqlite:///database.db", echo=False)


def init():
    # Create DB and tables
    barang_1 = T_Barang(nama="Pepsodent", harga=7500)
    barang_2 = T_Barang(nama="Ciptadent", harga=5500)
    barang_3 = T_Barang(nama="Daia", harga=6500)
    barang_4 = T_Barang(nama="Rinso", harga=4500)
    barang_5 = T_Barang(nama="Sunlight", harga=5000)
    barang_6 = T_Barang(nama="Sanco", harga=4000)
    barang_7 = T_Barang(nama="Bimoli", harga=6000)
    barang_8 = T_Barang(nama="Attack", harga=7000)
    barang_9 = T_Barang(nama="Formula", harga=8000)
    barang_10 = T_Barang(nama="Sunsilk", harga=8500)
    daftar_barang = [barang_1, barang_2, barang_3, barang_4, barang_5,
                     barang_6, barang_7, barang_8, barang_9, barang_10]

    daftar_struk = []
    for i in range(100):
        struk = T_Struk(tanggal_pembuatan=date(
            2021, 11, random.randint(1, 30)))
        daftar_struk.append(struk)

    SQLModel.metadata.create_all(engine)

    # Create records
    with Session(engine) as session:
        for barang in daftar_barang:
            session.add(barang)

        for struk in daftar_struk:
            session.add(struk)

        session.commit()

        for struk in daftar_struk:
            id_barang_1 = random.randint(0, 2)
            id_barang_2 = random.randint(3, 6)
            id_barang_3 = random.randint(7, 9)
            jumlah_barang = random.randint(1, 10)

            daftar_1 = T_Daftar(t_struk_id=struk.id, t_barang_id=daftar_barang[id_barang_1].id,
                                jumlah_barang=jumlah_barang, subtotal=jumlah_barang*daftar_barang[id_barang_1].harga)
            daftar_2 = T_Daftar(t_struk_id=struk.id, t_barang_id=daftar_barang[id_barang_2].id,
                                jumlah_barang=jumlah_barang, subtotal=jumlah_barang*daftar_barang[id_barang_2].harga)
            daftar_3 = T_Daftar(t_struk_id=struk.id, t_barang_id=daftar_barang[id_barang_3].id,
                                jumlah_barang=jumlah_barang, subtotal=jumlah_barang*daftar_barang[id_barang_3].harga)

            struk.total_pembelian = daftar_1.subtotal+daftar_2.subtotal+daftar_3.subtotal
            struk.total_pembayaran = struk.total_pembelian
            struk.kembalian = 0

            session.add(daftar_1)
            session.add(daftar_2)
            session.add(daftar_3)

        session.commit()


def CREATE_STRUK(session: Session):
    struk = T_Struk()
    session.add(struk)
    session.commit()
    print(
        f"CREATE_STRUK sukses. ID Struk: {struk.id}. Struk aktif: {struk.id}.")
    return struk


def INSERT(session: Session,  nama_barang: str, jumlah_barang: int, struk: Optional[T_Struk] = None):
    barang: T_Barang = session.exec(select(T_Barang).where(
        T_Barang.nama == nama_barang)).first()
    if(struk == None):
        typer.echo('INSERT '+typer.style("gagal", fg=typer.colors.WHITE, bg=typer.colors.RED,
                   bold=True)+'. Tidak ada struk aktif. Silakan membuat struk.')
        return
    if(barang):
        subtotal = jumlah_barang*barang.harga
        daftar = T_Daftar(t_struk_id=struk.id, t_barang_id=barang.id,
                          jumlah_barang=jumlah_barang, subtotal=subtotal)
        struk.total_pembelian += subtotal
        session.add(daftar)
        session.commit()
        print(
            f"INSERT pada struk {struk.id} "+typer.style("sukses", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True)+f". Barang {nama_barang}. Jumlah barang {jumlah_barang}.")
    else:
        typer.echo('INSERT pada struk '+typer.style('gagal', fg=typer.colors.WHITE, bg=typer.colors.RED, bold=True) +
                   f'. Barang {nama_barang} tidak dikenal')


def CALCULATE_STRUK(struk: T_Struk):
    typer.echo(
        f"CALCULATE_STRUK pada struk {struk.id} "+typer.style("berhasil", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True)+f". Total pembelian adalah {struk.total_pembelian}.")


def PAYMENT(session: Session, struk: T_Struk, nominal: float):
    if(nominal > struk.total_pembelian):
        struk.total_pembayaran = nominal
        struk.kembalian = nominal - struk.total_pembelian
        session.commit()
        typer.echo(
            f"PAYMENT pada struk {struk.id} "+typer.style("berhasil", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True)+f". Pembayaran {nominal}. Total Pembelian {struk.total_pembelian}. Kembalian {struk.kembalian}. Struk berhasil disimpan dan dihapus dari struk aktif.")
        return None
    else:
        typer.echo(
            f"PAYMENT pada struk {struk.id} "+typer.style("gagal", fg=typer.colors.WHITE, bg=typer.colors.RED, bold=True)+". Pembayaran tidak cukup.")
        return struk


def CANCEL_STRUK(session: Session, struk: T_Struk):
    session.delete(struk)
    session.commit()
    return None


def DISPLAY_STRUK(session: Session, tanggal_awal: date, tanggal_akhir: Optional[date] = None):
    where_clause: list = [T_Struk.tanggal_pembuatan >= tanggal_awal] if tanggal_akhir == None else [
        T_Struk.tanggal_pembuatan >= tanggal_awal, T_Struk.tanggal_pembuatan <= tanggal_akhir]
    daftar_struk = session.exec(select(T_Struk).where(*where_clause))
    typer.secho("{:<5} {:<18} {:<17} {:<17} {:<17}".format("ID", "Tanggal Pembuatan", "Total Pembelian", "Total Pembayaran", "Kembalian"),
                fg=typer.colors.BLUE, bold=True)
    for struk in daftar_struk:
        print("{:<5} {:<18} {:<17} {:<17} {:<17}".format(struk.id, str(struk.tanggal_pembuatan),
              struk.total_pembelian, struk.total_pembayaran, struk.kembalian))


def DISPLAY_PEAK(session: Session, tanggal_awal: date, tanggal_akhir: Optional[date] = None):
    where_clause: list = [T_Struk.tanggal_pembuatan >= tanggal_awal] if tanggal_akhir == None else [
        T_Struk.tanggal_pembuatan >= tanggal_awal, T_Struk.tanggal_pembuatan <= tanggal_akhir]
    results = session.query(T_Struk.tanggal_pembuatan, func.count(
        T_Struk.tanggal_pembuatan).label('jumlah')).where(*where_clause).group_by(T_Struk.tanggal_pembuatan).order_by(desc('jumlah')).limit(10)
    typer.secho("{:<20} {:<10}".format("Tanggal", "Jumlah Transaksi"),
                fg=typer.colors.BLUE, bold=True)
    for result in results:
        print("{:<20} {:<10}".format(str(result[0]), result[1]))


def BEST_PRODUCT(session: Session, tanggal_awal: date, tanggal_akhir: Optional[date] = None):
    where_clause: list = [T_Struk.tanggal_pembuatan >= tanggal_awal] if tanggal_akhir == None else [
        T_Struk.tanggal_pembuatan >= tanggal_awal, T_Struk.tanggal_pembuatan <= tanggal_akhir]
    results = session.query(T_Barang.nama, func.sum(
        T_Daftar.t_barang_id).label('jumlah')).join(T_Struk, T_Barang).where(*where_clause).group_by(T_Daftar.t_barang_id).order_by(desc('jumlah')).limit(5)
    typer.secho("{:<20} {:<10}".format("Nama Barang", "Jumlah Pembelian"),
                fg=typer.colors.BLUE, bold=True)
    for result in results:
        print("{:<20} {:<10}".format(result[0], result[1]))


if __name__ == "__main__":
    init()
