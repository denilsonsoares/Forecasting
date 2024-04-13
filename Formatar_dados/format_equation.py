from Utils.Interpolate import Interpolate
from Utils.DataCollector import DataCollector
import Utils.teste_funcoes as tf
start_date = '2023-01-01'
end_date = '2023-12-31'

collector = DataCollector()

pvc_brl = collector.name_date('PVC_BRL', start_date, end_date)
pvc_usa = collector.name_date('PVC_USA', start_date, end_date)

data_dict = {
    'pvc_usa': pvc_usa,
    'pvc_brl': pvc_brl,
}

for name in data_dict:
    data_dict[name] = data_dict[name].set_index("Date")

interp = Interpolate(data_dict)
df = interp.process_data()
df.fillna(method='bfill', inplace=True)
df = df.dropna()

print(df)
print(tf.analyze_relationship(df))
