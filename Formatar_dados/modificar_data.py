import pandas as pd

# Read the Excel file into a DataFrame
pvc = pd.read_excel('ENERGIA_ELETRICA.xlsx', sheet_name='ENERGIA_ELETRICA')  # Replace 'Sheet1' with the actual sheet name

# Modifica a coluna "Date"
# Convertendo as datas para o formato padrão (YYYY-MM-DD)
pvc["Date"] = pd.to_datetime(pvc["Date"], format="%d-%b-%Y", errors="coerce")
pvc["Date"] = pvc["Date"].fillna(pd.to_datetime(pvc["Date"], format="%d/%m/%Y"))

# Formatando as datas no novo formato
pvc["Date"] = pvc["Date"].dt.strftime("%Y-%m-%d")

# Salva as alterações no arquivo original
pvc.to_excel('formatado.xlsx', sheet_name='dados')
