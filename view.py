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
        elif COMMAND == 'EXIT':
            return
        else:
            print('Command tersebut tidak dikenali')


if __name__ == "__main__":
    app()
