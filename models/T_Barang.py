from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from models.T_Daftar import T_Daftar
from models.T_Struk import T_Struk


class T_Barang(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nama: str
    harga: float
    daftar_struk: List[T_Struk] = Relationship(
        back_populates="daftar_barang", link_model=T_Daftar)
