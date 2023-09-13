import streamlit as st
st.set_page_config(page_title='7LM-GPT', layout='wide', page_icon='🤖')
def calcular_pagamento(agendamentos, visitas, propostas, vendas, tempo_medio):
    dinheiro_agendamento = 1
    dinheiro_visita = 2
    dinheiro_proposta = 60

    if tempo_medio <= 5:
        dinheiro_venda = vendas * (100*3)
    elif 6 <= tempo_medio <= 7:
        dinheiro_venda = vendas * (100*2)
    else:
        dinheiro_venda = vendas * 100

    dinheiro_total = (agendamentos * dinheiro_agendamento) + (visitas * dinheiro_visita) + (propostas * dinheiro_proposta) + dinheiro_venda

    return {
        'Agendamentos': agendamentos * dinheiro_agendamento,
        'Visitas': visitas * dinheiro_visita,
        'Propostas': propostas * dinheiro_proposta,
        'Vendas': dinheiro_venda,
        'Total': dinheiro_total
    }

st.title("Simulador para Corretores Imobiliários")
with st.sidebar:
    st.image("https://7lm.com.br/wp-content/uploads/2023/03/logo_branca_aprovada_final_slogan.svg",use_column_width=True, width=30 , caption="Seja bem-vindo ao nosso simulador!")  # Adicione uma imagem de sua escolha

agendamentos = st.number_input("Digite o número de agendamentos:", min_value=0, value=0, step=1)
visitas = st.number_input("Digite o número de visitas:", min_value=0, value=0, step=1)
propostas = st.number_input("Digite o número de propostas:", min_value=0, value=0, step=1)
vendas = st.number_input("Digite o número de vendas:", min_value=0, value=0, step=1)
tempo_medio = st.number_input("Digite o tempo médio em dias para concluir a venda:", min_value=1, value=5, step=1)

if st.button("Calcular"):
    extrato = calcular_pagamento(agendamentos, visitas, propostas, vendas, tempo_medio)
    
    st.write(f"**Agendamentos:** {agendamentos} x R$1 = R${extrato['Agendamentos']:.2f}")
    st.write(f"**Visitas:** {visitas} x R$2 = R${extrato['Visitas']:.2f}")
    st.write(f"**Propostas:** {propostas} x R$60 = R${extrato['Propostas']:.2f}")
    st.write(f"**Vendas:** {vendas} x valor de venda (baseado no tempo médio) = R${extrato['Vendas']:.2f}")
    
    st.success(f"**Pagamento Total:** R${extrato['Total']:.2f}")


