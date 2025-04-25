from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProductEnum(str, Enum):
    product1 = "Produto A"
    product2 = "Produto B"
    product3 = "Produto C"

class Vendas(BaseModel):
    """
    Modelo de vendas da aplicação.

    Args:
        email (EmailStr): Email do cliente
        data_hora (datetime): Data e hora da venda
        valor (PositiveFloat): Valor da venda
        quantidade (PositiveInt): Quantidade de produtos vendidos
        produto (ProductEnum): Nome do produto vendido
    """
    email: EmailStr
    data_hora: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProductEnum
