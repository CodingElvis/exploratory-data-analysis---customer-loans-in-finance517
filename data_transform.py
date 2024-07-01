import pandas as pd

class DataTransform:
    
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def col_to_category (self, col_name):
        self.dataframe = self.dataframe.astype({col_name : 'category'})

    def col_to_object (self, col_name):
        self.dataframe = self.dataframe.astype({col_name : 'object'})
        
        '''for entry in col_list:
            self.dataframe.entry = self.dataframe.entry.astype('object') '''

    def strip_months (self, col_name):
        self.dataframe[col_name] = self.dataframe[col_name].str.replace(" months", "")

    def col_to_float (self, col_name):
        self.dataframe = self.dataframe.astype({col_name : 'float'})

    def drop_col(self, col_name):
        self.dataframe.drop(col_name, axis = 'columns', inplace = True)

    def add_day_15 (self, col_name):
        self.dataframe[col_name] = '15-' + self.dataframe[col_name].astype(str)

    def col_to_date (self, col_name):
        self.dataframe[col_name] = pd.to_datetime(self.dataframe[col_name], dayfirst=True)