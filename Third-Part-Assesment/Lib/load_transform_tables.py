import pandas as pd
import os
import numpy as np
import math

class PrepareTheFeatures:
    def __init__(self):
        self
        
    def encoding_columns(self, df_join_freq_sev):
        # One hot encoding or label encoding
        df_join_freq_sev['EncodeDensity'] =  df_join_freq_sev['Density'].apply(lambda x: 'SmallCity' if x <= 5000 else ('MediumCity' if x < 10000 else 'BigCity'))
        
        one_hot_encoding_columns = ['Region', 'Area', 'VehBrand', 'EncodeDensity']
        
        # encode categorical variables with more than two levels using one-hot encoding
        df_join_freq_sev = pd.get_dummies(df_join_freq_sev, columns = one_hot_encoding_columns)
        
        df_join_freq_sev['EncodeVehGas'] =  df_join_freq_sev['VehGas'].apply(lambda x: 1 if x == 'Regular' else 0)
                
        df_join_freq_sev = df_join_freq_sev.drop(columns = ['Seniority'])
        
        return df_join_freq_sev
        
    def normalize_columns(self, df_join_freq_sev):
        # min-max normalization (numeric variables)
        min_max_columns = ['VehAge', 'BonusMalus', 'DrivAge']
        
        # scale numerical variables using min max scaler
        for column in min_max_columns:
                # minimum value of the column
                min_column = df_join_freq_sev[column].min()
                # maximum value of the column
                max_column = df_join_freq_sev[column].max()
                # min max scaler
                df_join_freq_sev[column] = (df_join_freq_sev[column] - min_column) / (max_column - min_column)
                
        return df_join_freq_sev


class FreqTable:
    
    def __init__(self):
        self
        
    def read_data(self):
        return pd.read_csv('data\\input\\freMTPL2freq.csv',
                     dtype = {"IDpol" : str})
    
    def process_special_characters_in_columns(self, df_freq, 
                                              list_columns_to_process
                                              ):
        for col in list_columns_to_process:
            df_freq[col] = df_freq[col].apply(lambda x : str(x).replace("'", ""))
        
        del col, list_columns_to_process
        
        return df_freq
    
    
    def build_categ_seniority(self, df_freq):
        df_freq['CategSeniorty'] = df_freq['DrivAge'].apply(lambda x: round(x, -1))
        
        return df_freq
    
    def build_seniority(self, df_freq):
        df_freq['Seniority'] = df_freq['DrivAge'].apply(lambda x : 1 if x >= 60 else 0)
        
        return df_freq
    
    def load_data(self):
        df_freq = self.read_data()
        list_columns_to_process = ['Area', 'VehBrand', 'VehGas', 'Region']
        
        df_freq = self.build_seniority(df_freq)
        
        df_freq = self.build_categ_seniority(df_freq)
        
        return self.process_special_characters_in_columns(df_freq, list_columns_to_process)
    
class SevTable:
    def __init__(self):
        self
    
    def read_data(self):
        return pd.read_csv('data\\input\\freMTPL2sev.csv',
                     dtype = {"IDpol" : str})
    
    def load_data(self):
        df_sev = self.read_data()
        return df_sev.groupby(['IDpol']).agg({'ClaimAmount' : 'sum'}).reset_index()
        
