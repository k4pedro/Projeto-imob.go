import streamlit as st
import pandas as pd
from services.database import run_query

def view_main_page(conn):
    st.set_page_config(page_title="IMOB.GO", page_icon="🔍")
    st.title("IMOB.GO")
    st.subheader("Sua ferramenta de pesquisas imobiliarias")
    
    with open("estilo.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
   
    buscador = st.text_input("Digite o termo de busca:")
    
    if st.button("Buscar"):
        query = f"""
        SELECT * FROM cadastrados
        WHERE 
            numero_do_contribuinte LIKE '%{buscador}%' OR
            nome_de_logradouro_do_imovel LIKE '%{buscador}%' OR
            numero_do_imovel LIKE '%{buscador}%' OR
            complemento_do_imovel LIKE '%{buscador}%' OR
            bairro_do_imovel LIKE '%{buscador}%' OR
            cep_do_imovel LIKE '%{buscador}%' OR
            area_do_terreno LIKE '%{buscador}%' OR
            valor_do_m2_do_terreno LIKE '%{buscador}%'
        """
        resultado = run_query(query, conn)

        if resultado:
            st.success("Resultados encontrados:")
            df = pd.DataFrame(resultado, columns=['Numero do Contribuinte', 'Nome do Logradouro', 'Numero do Imovel', 'Complemento do Imovel', 'Bairro do Imovel', 'Cep do Imovel', 'Area do Terreno', 'Valor do M2 do Terreno'])

            df = df.applymap(lambda x: f"<span style='background-color:yellow;'>{x}</span>" if buscador.lower() in str(x).lower() else x)

            st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.error("Nenhum resultado encontrado.")

    if st.button("Limpar barra de pesquisa"):
        st.experimental_rerun()
