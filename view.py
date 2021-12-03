import typer
from datetime import date
from sqlmodel import Session
from controller import (
    CANCEL_STRUK,
    PAYMENT,
    engine,
    BEST_PRODUCT,
    CALCULATE_STRUK,
    CREATE_STRUK,
    DISPLAY_PEAK,
    DISPLAY_STRUK,
    INSERT,
)
from model import T_Struk


def green_style_text(text):
    return typer.style(text, fg=typer.colors.GREEN, bold=True)


def choice_app():
    session = Session(engine)
    menu = {
        1: "CREATE STRUCK",
        2: "INSERT",
        3: "CALCULATE_STRUCK",
        4: "PAYMENT",
        5: "CANCEL_STRUK",
        6: "DISPLAY_STRUK",
        7: "DISPLAY_PEAK",
        8: "BEST_PRODUCT",
        9: "EXIT",
        10: "HELP",
    }
    while True:
        try:
            typer.secho(
                "{:<20} {:<2}".format("Pilihan", "Menu"),
                fg=typer.colors.BLUE,
                bold=True,
            )
            for key, value in menu.items():
                print("{:<20} {:<2}".format(key, value))

            operasi = int(
                input(green_style_text("Masukan operasi pilihan (dalam angka): "))
            )
            if operasi == 1:
                struk = CREATE_STRUK(session=session)
            elif operasi == 2:
                x = str(input(green_style_text("Masukkan nama barang: ")))
                y = int(input(green_style_text("Masukkan jumlah barang: ")))
                INSERT(session=session, struk=struk, nama_barang=x, jumlah_barang=y)
            elif operasi == 3:
                CALCULATE_STRUK(struk=struk)
            elif operasi == 4:
                x = int(input(green_style_text("Masukkan nominal: ")))
                struk = PAYMENT(session=session, struk=struk, nominal=x)
            elif operasi == 5:
                struk = CANCEL_STRUK(session=session, struk=struk)
            elif operasi == 6:
                x = str(input(green_style_text("Masukkan date awal, DD-MM-YYYY: ")))
                y = str(input(green_style_text("Masukkan date akhir, DD-MM-YYYY: ")))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    DISPLAY_STRUK(
                        session=session,
                        tanggal_awal=date(awal[2], awal[1], awal[0]),
                        tanggal_akhir=date(akhir[2], akhir[1], akhir[0]),
                    )
                else:
                    DISPLAY_STRUK(
                        session=session, tanggal_awal=date(awal[2], awal[1], awal[0])
                    )
            elif operasi == 7:
                x = str(input(green_style_text("Masukkan date awal, DD-MM-YYYY: ")))
                y = str(input(green_style_text("Masukkan date akhir, DD-MM-YYYY: ")))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    DISPLAY_PEAK(
                        session=session,
                        tanggal_awal=date(awal[2], awal[1], awal[0]),
                        tanggal_akhir=date(akhir[2], akhir[1], akhir[0]),
                    )
                else:
                    DISPLAY_PEAK(
                        session=session, tanggal_awal=date(awal[2], awal[1], awal[0])
                    )
            elif operasi == 8:
                x = str(input(green_style_text("Masukkan date awal, DD-MM-YYYY: ")))
                y = str(input(green_style_text("Masukkan date akhir, DD-MM-YYYY: ")))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    BEST_PRODUCT(
                        session=session,
                        tanggal_awal=date(awal[2], awal[1], awal[0]),
                        tanggal_akhir=date(akhir[2], akhir[1], akhir[0]),
                    )
                else:
                    BEST_PRODUCT(
                        session=session, tanggal_awal=date(awal[2], awal[1], awal[0])
                    )
            elif operasi == 9:
                typer.echo(
                    typer.style(
                        "Anda Berhasil Keluar",
                        fg=typer.colors.WHITE,
                        bg=typer.colors.GREEN,
                        bold=True,
                    )
                )
                break
            elif operasi == 10:
                typer.echo(
                    """
Berikut ini merupakan menu yang tersedia beserta penjelasan singkatnya:

1. CREATE_STRUK
Membuat struk baru di memori. Struk yang baru dibuat adalah struk yang aktif.

2. INSERT
Menambah barang pada struk yang sedang aktif. Perintah ini memeriksa apakah nama barang yang diinput ada di dalam database.
Jika barang ada di database, proses input barang dilanjutkan. Jika barang tidak ada di dalam database, barang tidak diinput.
Parameter nama_barang dalam string sedang jumlah_barang dalam integer.

3. CALCULATE_STRUK
Menghitung total pembelian pada struk yang sedang aktif.

4. PAYMENT
Menyimpan nilai uang pembayaran dari konsumen, menghitung jumlah kembalian, dan menyimpan struk dalam database.
Struk ini dihapus dari struk aktif.
Parameter nominal dalam float.

5. CANCEL_STRUK
Menghapus struk aktif dari memori.

6. DISPLAY_STRUK
Menampilkan semua struk yang dibuat pada rentang tanggal awal dan tanggal akhir.
Jika hanya ada satu tanggal saja, maka semua struk yang dibuat pada tanggal tersebut dan sesudah tanggal tersebut ditampilkan ke layar.
Kedua parameter tanggal dalam format DD-MM-YYYY.

7. DISPLAY_PEAK
Menampilkan top 10 hari-hari terjadinya peak transaksi dan jumlah transaksi yang terjadi pada rentang waktu tertentu.
Jika rentang tidak diberikan maka top 10 diambil dari keseluruhan transaksi.
Jika hanya satu tanggal yang diberikan maka pencarian top 10 dilakukan mulai tanggal tersebut.
Kedua parameter tanggal dalam format DD-MM-YYYY.

8. BEST_PRODUCT
Menampilkan top 5 barang yang paling laris pada rentang waktu tertentu.
Jika rentang waktu tidak diberikan maka pencarian top 5 dilakukan pada semua transaksi.
Jika hanya satu tanggal yang diberikan maka pencarian top 5 dilakukan mulai dari transaksi yang ada sejak tanggal tersebut.
Kedua parameter tanggal dalam format DD-MM-YYYY.

9. EXIT
Keluar dari aplikasi.

10. HELP
Menampilkan bantuan terkait fungsionalitas aplikasi.
                """
                )
            else:
                typer.echo(
                    typer.style(
                        "Pilihan Operasi Tidak Dikenali",
                        fg=typer.colors.WHITE,
                        bg=typer.colors.RED,
                        bold=True,
                    )
                )

            print(green_style_text("-----"))
        except UnboundLocalError:
            typer.echo(
                typer.style(
                    "Terjadi kesalahan: Tidak ada Struck aktif, silahkan CREATE_STRUCK terlebih dahulu",
                    fg=typer.colors.WHITE,
                    bg=typer.colors.RED,
                    bold=True,
                )
            )
        except Exception as err:
            typer.echo(
                typer.style(
                    f"Terjadi kesalahan: {err}",
                    fg=typer.colors.WHITE,
                    bg=typer.colors.RED,
                    bold=True,
                )
            )


def command_app():
    session = Session(engine)

    def toInt(n):
        return int(n)

    COMMAND: str = None
    struk: T_Struk = None

    while COMMAND != "EXIT":
        FULL_COMMAND = typer.prompt(
            "Mohon isikan command dan argument (HELP untuk melihat command yg tersedia)"
        )
        ARGUMENT_LIST = FULL_COMMAND.split()
        COMMAND = ARGUMENT_LIST[0]
        if COMMAND == "CREATE_STRUK":
            struk = CREATE_STRUK(session=session)
        elif COMMAND == "INSERT":
            INSERT(
                session=session,
                struk=struk,
                nama_barang=ARGUMENT_LIST[1],
                jumlah_barang=ARGUMENT_LIST[2],
            )
        elif COMMAND == "CALCULATE_STRUK":
            CALCULATE_STRUK(struk=struk)
        elif COMMAND == "PAYMENT":
            struk = PAYMENT(session=session, struk=struk, nominal=ARGUMENT_LIST[1])
            # kalau PAYMENT berhasil struk jadi None, kalau nggak tetep struk, lihat return value fungsi di atas
        elif COMMAND == "CANCEL_STRUK":
            struk = CANCEL_STRUK(session=session, struk=struk)
            # pasti jadi null mengingat CANCEL_STRUK selalu return null
        elif COMMAND == "DISPLAY_STRUK":
            DISPLAY_STRUK(
                session=session,
                tanggal_awal=date(*map(toInt, ARGUMENT_LIST[1].split("-"))),
                tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split("-")))
                if len(ARGUMENT_LIST) > 2
                else None,
            )
        elif COMMAND == "DISPLAY_PEAK":
            DISPLAY_PEAK(
                session=session,
                tanggal_awal=date(*map(toInt, ARGUMENT_LIST[1].split("-"))),
                tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split("-")))
                if len(ARGUMENT_LIST) > 2
                else None,
            )
        elif COMMAND == "BEST_PRODUCT":
            BEST_PRODUCT(
                session=session,
                tanggal_awal=date(*map(toInt, ARGUMENT_LIST[1].split("-"))),
                tanggal_akhir=date(*map(toInt, ARGUMENT_LIST[2].split("-")))
                if len(ARGUMENT_LIST) > 2
                else None,
            )
        elif COMMAND == "HELP":
            typer.echo(
                """
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

            9. EXIT
            Keluar dari aplikasi
            """
            )
        elif COMMAND == "EXIT":
            break
        else:
            print("Command tersebut tidak dikenali")


if __name__ == "__main__":
    typer.echo(
        green_style_text(
            "Interface 1: Easy Choice Approach\nInterface 2: Command approach"
        )
    )
    interface = int(input(green_style_text("Masukkan Pilihan (1 atau 2): ")))
    choice_app() if interface == 1 else command_app() if interface == 2 else typer.echo(
        typer.style(
            "Pilihan Operasi Tidak Dikenali",
            fg=typer.colors.WHITE,
            bg=typer.colors.RED,
            bold=True,
        )
    )
