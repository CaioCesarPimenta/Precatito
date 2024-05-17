from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st
import pandas as pd

headers = {
    "Authorization": f"Bearer {st.secrets['OPENAI_API_KEY']}",
    "Content-Type": "application/json"
}

def CSV():
    csv_file_path = st.secrets["csv_file_path"]
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    
    if os.path.exists(csv_file_path):
        column_names = ['Periodos.Periodo', 'Reserva de produtos', 'PROC', 'CLASSIFICAÇÃO DO PERÍODO', 'CLASSIFICAÇÃO', 'AUTORA', 'DESMEMBRAMENTO', 'Nº DO DESMEMBRAMENTO', 'CLASSIFICAÇÃO DO ATIVO', 'HC', 'HS', 'EXPEDIÇÃO OU ESTIMATIVA DE EXPEDIÇÃO', 'INÍCIO', 'FIM', 'NÚMERO DO PRECATÓRIO', 'TIPO DE CESSÃO', 'CESSÃO AUTORA', 'CESSÃO AUTORA2', 'AUTORA CEDIDO PARA', 'CESSÃO HC', 'HC CEDIDO PARA', 'CESSÃO HS', 'HS CEDIDO PARA', 'STATUS DO ATIVO', 'ESTIMATIVA DE DATA DE PAGAMENTO', 'Valor atualizado Bruto 1', 'Desconto Previdenciário 1', 'HC + imposto 1', 'IR - RRA 1', 'Pgto Parcial e Prioridade 1', 'Recolhimento Legal 1', 'Valor atualizado Liquido 1', 'CJP Total', 'Outros Total', 'BOFA', 'Autoras Total', 'GAE Total', 'Atlas 7 Total', 'Droom Total', 'DISP Autoras', 'DISP HC', 'DISP HS', 'DISP HC e HS', 'DISP TOTAL']
        df = pd.read_csv(csv_file_path, names=column_names, sep=';')
        df['CESSÃO HC'] = df['CESSÃO HC'].astype(float)
        df['Valor atualizado Liquido 1'] = df['Valor atualizado Liquido 1'].astype(float)
        
        user_question = st.text_input("Pergunte ao Precatito sobre a modelagem: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="Em progresso..."):
                # Temporarily save the DataFrame as a CSV file
                temp_csv_file = "temp.csv"
                df.to_csv(temp_csv_file, index=False)
                
                # Pass the CSV file path to create_csv_agent
                agent = create_csv_agent(
                    OpenAI(api_key=OPENAI_API_KEY, temperature=0, model="gpt-3.5-turbo-0125"),
                    temp_csv_file,
                    names=column_names,
                    sep=';'
                )
                
                # Delete the temporary CSV file after use
                os.remove(temp_csv_file)
                
                response = agent.run(user_question)
                st.write(response)
    else:
        st.error("Arquivo CSV não encontrado.")

CSV()
