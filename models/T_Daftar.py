from typing import List, Optional
from sqlmodel import Field, SQLModel


class T_Daftar(SQLModel, table=True):
    t_barang_id: Optional[int] = Field(
        default=None, foreign_key="t_barang.id", primary_key=True)
    t_struk_id: Optional[int] = Field(
        default=None, foreign_key="t_struk.id", primary_key=True)
    jumlah_barang: int
    subtotal: float
