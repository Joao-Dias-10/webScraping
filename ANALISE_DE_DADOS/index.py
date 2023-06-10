import pandas as pd
import os

def analiseDeDados():
            
            dir = os.getcwd()
            df = pd.read_excel(rf'{dir}/ANALISE_DE_DADOS/uploads/dados_funcionarios.xlsx')
            coluna = df['Funcionário']
            funcionarios = coluna.tolist()
            coluna = df['Alcance']
            alcances = coluna.tolist()
            coluna = df['Meta']
            metas = coluna.tolist()

            print(funcionarios)
            print(alcances)
            print(metas)

analiseDeDados()