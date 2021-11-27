from datetime import date
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship


class T_Daftar(SQLModel, table=True):
    t_barang_id: Optional[int] = Field(
        default=None, foreign_key="t_barang.id", primary_key=True)
    t_struk_id: Optional[int] = Field(
        default=None, foreign_key="t_struk.id", primary_key=True)
    jumlah_barang: int
    subtotal: float


class T_Barang(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nama: str
    harga: float
    daftar_struk: List['T_Struk'] = Relationship(
        back_populates="daftar_barang", link_model=T_Daftar)


class T_Struk(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total_pembelian: float = 0
    total_pembayaran: Optional[float]
    kembalian: Optional[float]
    tanggal_pembuatan: date = date.today()
    daftar_barang: List[T_Barang] = Relationship(
        back_populates="daftar_struk", link_model=T_Daftar)
