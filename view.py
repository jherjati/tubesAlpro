from datetime import date
from sqlmodel import Session
from controller import CALCULATE_STRUK, CREATE_STRUK, DISPLAY_PEAK, DISPLAY_STRUK, INSERT
from controller import engine


session = Session(engine)
# struk = CREATE_STRUK(session=session)
# INSERT(session, struk, "Pepsodent", 2)
# CALCULATE_STRUK(struk)
# DISPLAY_STRUK(session, date(2021, 11, 25), date(2021, 11, 28))
DISPLAY_PEAK(session, date(2021, 11, 29))
