import pandas as pd

# Ler os dados do arquivo Excel especificando o nome da planilha e o engine
df = pd.read_excel('HIPO.xlsx', sheet_name='HIPO')  # Replace 'Sheet1' with the actual sheet name

# Modifica a coluna "Date"
df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")

# Salva as alterações em um novo arquivo:
df.to_excel('formatado.xlsx', sheet_name='ENERGIA_ELETRICA')

print("Arquivo formatado salvo com sucesso!")
