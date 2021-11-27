from typing import List, Optional
from datetime import date
from sqlmodel import Field, SQLModel, Relationship

# from models.T_Barang import T_Barang
from models.T_Daftar import T_Daftar


class T_Struk(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total_pembelian: float = 0
    total_pembayaran: Optional[float]
    kembalian: Optional[float]
    tanggal_pembuatan: date = date.today()
    daftar_barang: List['T_Barang'] = Relationship(
        back_populates="daftar_struk", link_model=T_Daftar)
