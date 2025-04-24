from datetime import datetime
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
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
    categoria: ProductEnum

    @validate_call('categoria')
    def enum_categoria(cls, v):
        return v
    