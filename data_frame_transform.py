import numpy as np

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def drop_col(self, column_name):
        self.df.drop(columns=column_name, inplace=True)

    def drop_row (self, col_name):
        self.df.dropna(axis=0, subset = col_name, inplace=True)

    def impute_constant(self, col_name, constant):
        self.df[col_name].fillna(value=constant , inplace = True)

    def impute_by_median (self, column):
        self.df[column].fillna(self.df[column].median() , inplace = True)
        
    def impute_by_mean (self, column):
        self.df[column].fillna(self.df[column].mean() , inplace = True)

    def log_transform(self, column):
        log_column = "log_"+column
        self.df[log_column] = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)


    def show_skew(self):
        print (self.df.skew(numeric_only = True))