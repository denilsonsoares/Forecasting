import pandas as pd


class DataCollector:

    def __init__(self):
        pass

    def get_df_from_excel(self, file_path, sheet_name):
        return pd.read_excel(file_path, sheet_name=sheet_name)

    def get_df_filtered_by_date(self, df, start_date, end_date):
        # rename first column to Date
        df.rename(columns={df.columns[0]: 'Date'}, inplace=True)
        # convert Date column to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        return df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    def get_df_from_name(self, name):
        return self.get_df_from_excel('../../dados/' + name + '.xlsx', name)

    def name_date(self, name, start_date, end_date):
        return self.get_df_filtered_by_date(self.get_df_from_name(name), start_date, end_date)