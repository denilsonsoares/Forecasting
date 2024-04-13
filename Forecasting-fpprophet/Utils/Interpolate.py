import pandas as pd
import numpy as np


class Interpolate:

    def __init__(self, data_dict):
        self.data_dict = data_dict  # Store the original data in a dictionary

    def set_datetime_index(self):
        for key, df in self.data_dict.items():
            df.index = pd.to_datetime(df.index)

    def resample_to_daily(self):
        daily_data = {}
        for key, df in self.data_dict.items():
            daily_data[key] = df.resample('D').interpolate(method='linear')
        return daily_data

    def resample_to_weekly(self, daily_data):
        weekly_data = {}
        for key, df in daily_data.items():
            weekly_data[key] = df.resample('W-Mon').asfreq()
        return weekly_data

    def combine_data(self, data):
        combined_data = pd.DataFrame(index=data[list(data.keys())[0]].index)
        for key, df in data.items():
            combined_data[key] = df.iloc[:, 0]  # Assuming each df has only one column
        return combined_data

    def process_data(self):
        # Set datetime index for all dataframes
        self.set_datetime_index()

        # Resample all dataframes to daily frequency and interpolate
        daily_data = self.resample_to_daily()

        # Resample all daily data to weekly frequency
        weekly_data = self.resample_to_weekly(daily_data)

        # Combine all weekly data into a single dataframe
        combined_weekly_data = self.combine_data(weekly_data)

        return combined_weekly_data