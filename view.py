import typer
from datetime import date
from sqlmodel import Session
from controller import CANCEL_STRUK, PAYMENT, engine, BEST_PRODUCT, CALCULATE_STRUK, CREATE_STRUK, DISPLAY_PEAK, DISPLAY_STRUK, INSERT
<<<<<<< HEAD
import typer
=======
from model import T_Struk
>>>>>>> 349818e22a03913f0f03efebc2623359fbfc17d3

def green_style_text(text):
    return typer.style(text, 
                fg=typer.colors.GREEN, bold=True)
                
def app():
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
    }
    while True:
        try:
            typer.secho("{:<20} {:<2}".format("Pilihan", "Menu"),
                        fg=typer.colors.BLUE, bold=True)
            for key,value in menu.items():
                print("{:<20} {:<2}".format(key, value))

            operasi = int(input(green_style_text('Masukan operasi pilihan (dalam angka): ')))
            if operasi == 1:
                struk = CREATE_STRUK(session=session)
            elif operasi == 2:
                x = str(input(green_style_text("Masukkan nama barang: ")))
                y = int(input(green_style_text('Masukkan jumlah barang: ')))
                INSERT(session=session, struk=struk,
                        nama_barang=x, jumlah_barang=y)
            elif operasi == 3:
                CALCULATE_STRUK(struk=struk)
            elif operasi == 4:
                x = int(input(green_style_text('Masukkan nominal: ')))
                struk = PAYMENT(session=session, struk=struk, nominal=x)
            elif operasi == 5:
                struk = CANCEL_STRUK(session=session, struk=struk)
            elif operasi == 6:
                x = str(input(green_style_text('Masukkan date awal, DD-MM-YYYY: ')))
                y = str(input(green_style_text('Masukkan date akhir, DD-MM-YYYY: ')))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    DISPLAY_STRUK(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]), 
                                tanggal_akhir=date(akhir[2], akhir[1], akhir[0]))
                else:
                    DISPLAY_STRUK(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]))
            elif operasi == 7:
                x = str(input(green_style_text('Masukkan date awal, DD-MM-YYYY: ')))
                y = str(input(green_style_text('Masukkan date akhir, DD-MM-YYYY: ')))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    DISPLAY_PEAK(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]), 
                                tanggal_akhir=date(akhir[2], akhir[1], akhir[0]))
                else:
                    DISPLAY_PEAK(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]))
            elif operasi == 8:
                x = str(input(green_style_text('Masukkan date awal, DD-MM-YYYY: ')))
                y = str(input(green_style_text('Masukkan date akhir, DD-MM-YYYY: ')))
                awal = list(map(int, x.split("-")))
                if y:
                    akhir = list(map(int, y.split("-")))
                    BEST_PRODUCT(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]), 
                                tanggal_akhir=date(akhir[2], akhir[1], akhir[0]))
                else:
                    BEST_PRODUCT(session=session, 
                                tanggal_awal=date(awal[2], awal[1], awal[0]))
            elif operasi == 9:
                typer.echo(typer.style("Anda Berhasil Keluar", 
                    fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True))
                break
            else:
                typer.echo(typer.style("Pilihan Operasi Tidak Dikenali", 
                    fg=typer.colors.WHITE, bg=typer.colors.RED, bold=True))

            print(green_style_text("-----"))
        except Exception as err:
            typer.echo(typer.style(f"Terjadi kesalahan: {err}", 
                    fg=typer.colors.WHITE, bg=typer.colors.RED, bold=True))
            


    # struk = CREATE_STRUK(session=session)
    # INSERT(session=session, struk=struk,
    #        nama_barang="Pepsodent", jumlah_barang=2)
    # INSERT(session=session, struk=struk,
    #        nama_barang="Ciptadent", jumlah_barang=4)
    # INSERT(session=session, struk=struk,
    #        nama_barang="Rinso", jumlah_barang=3)
    # INSERT(session=session, struk=struk,
    #        nama_barang="Daia", jumlah_barang=1)
    # CALCULATE_STRUK(struk=struk)

    # struk = PAYMENT(session=session, struk=struk, nominal=50000)
    # # kalau PAYMENT berhasil struk jadi None, kalau nggak tetep struk, lihat return value fungsi di atas

    # struk = CANCEL_STRUK(session=session, struk=struk)
    # # pasti jadi null mengingat CANCEL_STRUK selalu return null

<<<<<<< HEAD
    # DISPLAY_STRUK(session=session, tanggal_awal=date(
    #     2021, 11, 5), tanggal_akhir=date(2021, 11, 20))
    # DISPLAY_PEAK(session=session, tanggal_awal=date(2021, 11, 5))
    # BEST_PRODUCT(session=session, tanggal_awal=date(2021, 11, 5))
=======
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
        elif COMMAND == 'EXIT':
            return
        else:
            print('Command tersebut tidak dikenali')
>>>>>>> 349818e22a03913f0f03efebc2623359fbfc17d3


if __name__ == "__main__":
    app()
