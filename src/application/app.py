import streamlit as st

def main():
    st.title('Bem vindo ao Sistema de CRM e Vendas Ticaracatica')
    email = st.text_input('Email do Vendedor')
    data = st.date_input('Data da venda')
    hora = st.time_input('Hora da Venda')
    valor = st.number_input('Valor da Venda')
    quantidade = st.number_input('Quantidade de Produtos')
    categoria = st.selectbox('Tipo de Produto', ['Produto A', 'Produto B', 'Produto C'])

    venda = {
        'email': email,
        'data_hora': f'{data} {hora}',
        'valor': valor,
        'quantidade': quantidade,
        'categoria': categoria
    }

    if st.button('Salvar'):
        st.success('Venda salva com sucesso!')
        st.warning(venda)



if __name__ == "__main__":
    main()
    st.write("Sistema de CRM e Vendas Ticaracatica")
    st.write("Desenvolvido por: Heitor Cesarino")
    st.write("Versão: 1.0")
    st.write("Data: 2025-04-23")