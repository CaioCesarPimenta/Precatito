from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st
import pandas as pd

def CSV():
    csv_file_path = st.secrets["csv_file_path"]
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    
    if os.path.exists(csv_file_path):
        cola = ['Periodos.Periodo', 'Reserva de produtos', 'PROC', 'CLASSIFICAÇÃO DO PERÍODO', 'CLASSIFICAÇÃO', 'AUTORA', 'DESMEMBRAMENTO', 'Nº DO DESMEMBRAMENTO', 'CLASSIFICAÇÃO DO ATIVO', 'HC', 'HS', 'EXPEDIÇÃO OU ESTIMATIVA DE EXPEDIÇÃO', 'INÍCIO', 'FIM', 'NÚMERO DO PRECATÓRIO', 'TIPO DE CESSÃO', 'CESSÃO AUTORA', 'CESSÃO AUTORA2', 'AUTORA CEDIDO PARA', 'CESSÃO HC', 'HC CEDIDO PARA', 'CESSÃO HS', 'HS CEDIDO PARA', 'STATUS DO ATIVO', 'ESTIMATIVA DE DATA DE PAGAMENTO', 'Valor atualizado Bruto 1', 'Desconto Previdenciário 1', 'HC + imposto 1', 'IR - RRA 1', 'Pgto Parcial e Prioridade 1', 'Recolhimento Legal 1', 'Valor atualizado Liquido 1', 'CJP Total', 'Outros Total', 'BOFA', 'Autoras Total', 'GAE Total', 'Atlas 7 Total', 'Droom Total', 'DISP Autoras', 'DISP HC', 'DISP HS', 'DISP HC e HS', 'DISP TOTAL']
        df = pd.read_csv(csv_file_path, names=cola, sep=';')
        df['CESSÃO HC'] = df['CESSÃO HC'].astype(float)
        df['Valor atualizado Liquido 1'] = df['Valor atualizado Liquido 1'].astype(float)
        
        user_question = st.text_input("Pergunte ao Precatito sobre a modelagem: ")

        if user_question:
            with st.spinner(text="In progress..."):
                # Temporarily save the DataFrame as a CSV file
                temp_csv_file = "temp.csv"
                df.to_csv(temp_csv_file, index=False)
                
                # Create the OpenAI LLM instance with the correct model
                llm = OpenAI(api_key=OPENAI_API_KEY, model="text-davinci-002")
                
                # Pass the CSV file path to create_csv_agent
                agent = create_csv_agent(llm, temp_csv_file, column_names=cola, sep=';')
                
                # Delete the temporary CSV file after use
                os.remove(temp_csv_file)
                
                # Run the agent with the user question
                response = agent.run(user_question)
                
                # Display the response
                st.write(response)
    else:
        st.error("CSV file not found.")

if __name__ == "__main__":
    CSV()
