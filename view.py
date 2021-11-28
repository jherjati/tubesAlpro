import typer
from datetime import date
from sqlmodel import Session
from controller import CANCEL_STRUK, PAYMENT, engine, BEST_PRODUCT, CALCULATE_STRUK, CREATE_STRUK, DISPLAY_PEAK, DISPLAY_STRUK, INSERT
from model import T_Struk


def app():
    session = Session(engine)

    def toInt(n):
        return int(n)

    COMMAND: str = None
    struk: T_Struk = None

    while COMMAND != 'EXIT':
        FULL_COMMAND = typer.prompt(
            "Mohon isikan command dan argument (HELP untuk melihat command yg tersedia)")
        ARGUMENT_LIST = FULL_COMMAND.split()
        COMMAND = ARGUMENT_LIST[0]
        if COMMAND == 'CREATE_STRUK':
            struk = CREATE_STRUK(session=session)
        elif COMMAND == 'INSERT':
            INSERT(session=session, struk=struk,
                   nama_barang=ARGUMENT_LIST[1], jumlah_barang=ARGUMENT_LIST[2])
        elif COMMAND == 'CALCULATE_STRUK':
            CALCULATE_STRUK(struk=struk)
        elif COMMAND == 'PAYMENT':
            struk = PAYMENT(session=session, struk=struk,
                            nominal=ARGUMENT_LIST[1])
            # kalau PAYMENT berhasil struk jadi None, kalau nggak tetep struk, lihat return value fungsi di atas
        elif COMMAND == 'CANCEL_STRUK':
            struk = CANCEL_STRUK(session=session, struk=struk)
            # pasti jadi null mengingat CANCEL_STRUK selalu return null
        elif COMMAND == 'DISPLAY_STRUK':
            DISPLAY_STRUK(session=session, tanggal_awal=date(
                *map(toInt, ARGUMENT_LIST[1].split('-'))), tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split('-'))) if len(ARGUMENT_LIST) > 2 else None)
        elif COMMAND == 'DISPLAY_PEAK':
            DISPLAY_PEAK(session=session, tanggal_awal=date(
                *map(toInt, ARGUMENT_LIST[1].split('-'))), tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split('-'))) if len(ARGUMENT_LIST) > 2 else None)
        elif COMMAND == 'BEST_PRODUCT':
            BEST_PRODUCT(session=session, tanggal_awal=date(
                *map(toInt, ARGUMENT_LIST[1].split('-'))), tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split('-'))) if len(ARGUMENT_LIST) > 2 else None)
        elif COMMAND == 'HELP':
            typer.echo("""
            1. CREATE_STRUK
            Membuat struk baru di memori. Struk yang baru dibuat adalah struk yang aktif.

            2. INSERT<spasi><nama_barang><spasi><jumlah_barang>
            Menambah barang pada struk yang sedang aktif. Perintah ini memeriksa apakah nama barang yang diinput ada di dalam database.
            Jika barang ada di database, proses input barang dilanjutkan. Jika barang tidak ada di dalam database, barang tidak diinput.
            Parameter nama_barang dalam string sedang jumlah_barang dalam integer.

            3. CALCULATE_STRUK
            Menghitung total pembelian pada struk yang sedang aktif.

            4. PAYMENT<spasi><nominal>
            Menyimpan nilai uang pembayaran dari konsumen, menghitung jumlah kembalian, dan menyimpan struk dalam database.
            Struk ini dihapus dari struk aktif.
            Parameter nominal dalam float.

            5. CANCEL_STRUK
            Menghapus struk aktif dari memori.

            6. DISPLAY_STRUK<spasi><tanggal_awal><spasi><tanggal_akhir>
            Menampilkan semua struk yang dibuat pada rentang tanggal awal dan tanggal akhir.
            Jika hanya ada satu tanggal saja, maka semua struk yang dibuat pada tanggal tersebut dan sesudah tanggal tersebut ditampilkan ke layar.
            Kedua parameter tanggal dalam format YYYY-MM-DD.

            7. DISPLAY_PEAK<spasi><tanggal_awal><spasi><tanggal_akhir>
            Menampilkan top 10 hari-hari terjadinya peak transaksi dan jumlah transaksi yang terjadi pada rentang waktu tertentu.
            Jika rentang tidak diberikan maka top 10 diambil dari keseluruhan transaksi.
            Jika hanya satu tanggal yang diberikan maka pencarian top 10 dilakukan mulai tanggal tersebut.
            Kedua parameter tanggal dalam format YYYY-MM-DD.

            8. BEST_PRODUCT<spasi><tanggal_awal><spasi><tanggal_akhir>
            Menampilkan top 5 barang yang paling laris pada rentang waktu tertentu.
            Jika rentang waktu tidak diberikan maka pencarian top 5 dilakukan pada semua transaksi.
            Jika hanya satu tanggal yang diberikan maka pencarian top 5 dilakukan mulai dari transaksi yang ada sejak tanggal tersebut.
            Kedua parameter tanggal dalam format YYYY-MM-DD.
            """)
        elif COMMAND == 'EXIT':
            break
        else:
            print('Command tersebut tidak dikenali')


if __name__ == "__main__":
    app()
