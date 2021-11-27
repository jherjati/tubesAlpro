from datetime import date
from sqlmodel import Session
from controller import engine, BEST_PRODUCT, CALCULATE_STRUK, CREATE_STRUK, DISPLAY_PEAK, DISPLAY_STRUK, INSERT


session = Session(engine)
# struk = CREATE_STRUK(session=session)
# INSERT(session, struk, "Pepsodent", 2)
# CALCULATE_STRUK(struk)
# DISPLAY_STRUK(session, date(2021, 11, 5), date(2021, 11, 30))
DISPLAY_PEAK(session, date(2021, 11, 5))
BEST_PRODUCT(session, date(2021, 11, 5))
