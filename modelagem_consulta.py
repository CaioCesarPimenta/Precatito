import pandas as pd
import streamlit as st

#qual altora ?
#   filtrar altora
#qual proc?



def consulta_modelagem():

    haders = {
    "autorisation": st.secrets["csv_file_path"],
    "content-type": "application/json"
}


    cola = ["Periodos.Periodo",	"Reserva de produtos",	"PROC",	"Bloco",	"TRANCHE",	"CLASSIFICAÇÃO DO PERÍODO",	"CLASSIFICAÇÃO",	"NÚMERO DO PROCESSO",	"AUTORA",	"DESMEMBRAMENTO",	"Nº DO DESMEMBRAMENTO",	"CPF",	"CLASSIFICAÇÃO DO ATIVO",	"STATUS AUTORA",	"DATA FALECIMENTO",	"HABILITAÇÃO",	"DATA DA HABILITAÇÃO",	"NOME DO HABILITADO",	"Tese",	"HC",	"HS",	"EXPEDIÇÃO OU ESTIMATIVA DE EXPEDIÇÃO",	"INÍCIO",	"FIM",	"NÚMERO DO PRECATÓRIO",	"DATA DO CÁLCULO",	"VALOR TOTAL",	"PRINCIPAL",	"JUROS",	"DESCONTO PREVIDENCIÁRIO",	"CUSTAS",	"TAXA JUDICIÁRIA",	"DATA DO PAGAMENTO DE PRIORIDADE",	"VALOR DO PAGAMENTO DE PRIORIDADE",	"TIPO DE CESSÃO",	"CESSÃO AUTORA",	"CESSÃO AUTORA2",	"AUTORA CEDIDO PARA",	"CESSÃO HC",	"HC CEDIDO PARA",	"CESSÃO HS",	"HS CEDIDO PARA",	"STATUS DO ATIVO",	"OBS",	"PROBALIDADE DO ÊXITO DA EXECUÇÃO",	"OPORTUNIDADE",	"ESTIMATIVA DE DATA DE PAGAMENTO",	"DATA DO MANDADO DE PAGAMENTO",	"VALOR DO MANDADO DE PAGAMENTO",	"DATA DO RECIBO DE LEVANTAMENTO",	"VALOR LEVANTADO",	"IMPOSTO RETIDO",	"Atualização Jurídica",	"Droom_Digital",	"Adv",	"Ver",	"Razões",	"Posição na Fila",	"Situação na Fila",	"Valor atualizado Bruto 1",	"Desconto Previdenciário 1",	"HC + imposto 1",	"IR - RRA 1",	"Pgto Parcial e Prioridade 1",	"Recolhimento Legal 1",	"Valor atualizado Liquido 1",	"CJP Total",	"Outros Total",	"BOFA",	"Autoras Total",	"GAE Total",	"Atlas 7 Total",	"Droom Total",	"DISP Autoras",	"DISP HC",	"DISP HS",	"DISP HC e HS",	"DISP TOTAL"]
    csv_file_path=st.secrets["csv_file_path"]

    df = pd.read_csv(csv_file_path, names=cola, sep=';',decimal=".")
    df = df.drop(index=0)

    df[["HC",	"HS",	"VALOR TOTAL",	"PRINCIPAL",	"JUROS",	"DESCONTO PREVIDENCIÁRIO",	"CUSTAS",	"TAXA JUDICIÁRIA",	"VALOR DO PAGAMENTO DE PRIORIDADE",	"CESSÃO AUTORA",	"CESSÃO AUTORA2",	"CESSÃO HC",	"CESSÃO HS",	"Valor atualizado Bruto 1",	"Desconto Previdenciário 1",	"HC + imposto 1",	"IR - RRA 1",	"Pgto Parcial e Prioridade 1",	"Recolhimento Legal 1",	"Valor atualizado Liquido 1",	"CJP Total",	"Outros Total",	"BOFA",	"Autoras Total",	"GAE Total",	"Atlas 7 Total",	"Droom Total",	"DISP Autoras",	"DISP HC",	"DISP HS",	"DISP HC e HS",	"DISP TOTAL"]] = (
    df[["HC",	"HS",	"VALOR TOTAL",	"PRINCIPAL",	"JUROS",	"DESCONTO PREVIDENCIÁRIO",	"CUSTAS",	"TAXA JUDICIÁRIA",	"VALOR DO PAGAMENTO DE PRIORIDADE",	"CESSÃO AUTORA",	"CESSÃO AUTORA2",	"CESSÃO HC",	"CESSÃO HS",	"Valor atualizado Bruto 1",	"Desconto Previdenciário 1",	"HC + imposto 1",	"IR - RRA 1",	"Pgto Parcial e Prioridade 1",	"Recolhimento Legal 1",	"Valor atualizado Liquido 1",	"CJP Total",	"Outros Total",	"BOFA",	"Autoras Total",	"GAE Total",	"Atlas 7 Total",	"Droom Total",	"DISP Autoras",	"DISP HC",	"DISP HS",	"DISP HC e HS",	"DISP TOTAL"]].astype(float)
    )



 
    autora_options = sorted(df.AUTORA.unique().tolist())

    # Display selectbox with authors
    autora_value =  st.selectbox('Autora', autora_options)

    clasificacao_option = sorted(df['CLASSIFICAÇÃO DO PERÍODO'][df.AUTORA == autora_value].unique().tolist())

    clasificacao_value =  st.selectbox(clasificacao_option)

    PROC_option = sorted(df['PROC'][df.AUTORA == autora_value][df['CLASSIFICAÇÃO DO PERÍODO'] == clasificacao_value].unique().tolist())

    PROC_value =  st.selectbox('PROC', PROC_option)

    

    VALORES = st.selectbox('INFO', ['VALOR PRESENTE','CESSOES','DISPONIVEL',"HC/HS"])

    if VALORES == 'VALOR PRESENTE':

       st.write(df[['Valor atualizado Bruto 1','Desconto Previdenciário 1','HC + imposto 1','IR - RRA 1','Pgto Parcial e Prioridade 1','Recolhimento Legal 1','Valor atualizado Liquido 1']][df.AUTORA == autora_value][df['CLASSIFICAÇÃO DO PERÍODO'] == clasificacao_value])
    
    elif VALORES == 'CESSOES':
       st.write(df[['CJP Total','Outros Total','BOFA','Autoras Total','GAE Total','Atlas 7 Total','Droom Total']][df.AUTORA == autora_value][df['CLASSIFICAÇÃO DO PERÍODO'] == clasificacao_value])

    elif VALORES == 'DISPONIVEL':
        st.write(df[['DISP Autoras','DISP HC','DISP HS','DISP HC e HS']][df.AUTORA == autora_value][df['CLASSIFICAÇÃO DO PERÍODO'] == clasificacao_value])
    
    elif VALORES == "HC/HS":
        st.write(df[['CLASSIFICAÇÃO DO ATIVO','HC','HS']][df.AUTORA == autora_value][df['CLASSIFICAÇÃO DO PERÍODO'] == clasificacao_value])
