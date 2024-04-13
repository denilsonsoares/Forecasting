import pandas as pd

# Ler os dados do arquivo Excel especificando o nome da planilha e o engine
df = pd.read_excel('PETROLEO.xlsx', sheet_name=' BrentUS', engine='openpyxl')

# Modifica a coluna "Date"
df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")

# Salva as alterações em um novo arquivo:
df.to_excel('.xlsx', sheet_name='Cl2')