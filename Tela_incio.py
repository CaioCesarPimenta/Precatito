import streamlit as st
import Precatito_processos as processo
import Precatito_modelagem as modelagem
import modelagem_consulta as consulta
import openai

def main():
    st.header("Precatito Goul🦉")
   
    st.sidebar.title("HABILIDADES")
    skills = st.sidebar.selectbox("modelos",["Precatito Processos","Precatito modelagem","Consulta Modelagem"])

    if skills == 'Precatito Processos':
        st.header("📄")
        processo.PDF()

    elif skills == 'Precatito modelagem':
        st.header("📈")
        modelagem.CSV()
    
    elif skills == "Consulta Modelagem":
        st.header("📈")
        consulta.consulta_modelagem()
        
if __name__ == "__main__":
    main()
