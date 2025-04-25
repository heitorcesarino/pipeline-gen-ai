import streamlit as st
from data_contract import Vendas
from datetime import datetime
from pydantic import ValidationError
from db import salvar_no_postgres

def main():

    st.title('Bem vindo ao Sistema de CRM e Vendas Ticaracatica')
    email = st.text_input('Email do Vendedor')
    data = st.date_input('Data da venda')
    hora = st.time_input('Hora da Venda')
    valor = st.number_input('Valor da Venda')
    quantidade = st.number_input('Quantidade de Produtos')
    produto = st.selectbox('Tipo de Produto', ['Produto A', 'Produto B', 'Produto C'])
    data_hora = datetime.combine(data, hora)

    if st.button('Salvar'):
        try:
            venda = Vendas(
                email=email, 
                data_hora=data_hora, 
                valor=valor, 
                quantidade=quantidade, 
                produto=produto
            )
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro na validação: {e}")
            return

if __name__ == "__main__":
    main()
    st.write("Sistema de CRM e Vendas Ticaracatica")
    st.write("Desenvolvido por: Heitor Cesarino")
    st.write("Versão: 1.0")
    st.write("Data: 2025-04-23")