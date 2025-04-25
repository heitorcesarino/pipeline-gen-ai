from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProductEnum(str, Enum):
    product1 = "Produto A"
    product2 = "Produto B"
    product3 = "Produto C"

class Vendas(BaseModel):
    """Delivery model for the application."""
    email: EmailStr
    data_hora: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProductEnum
