import numpy as np

class DataFrameTransform:
    '''
    This class is used to transform data inside a dataframe.

    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.df : a Pandas dataframe
        the dataframe on which transformations will take place
    '''

    def __init__(self, df):
        self.df = df

    def drop_col(self, column_name):
        '''
        This method drops a specified column from the dataframe

        Parameters
        ----------
        column_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.df.drop(columns=column_name, inplace=True)

    def drop_row (self, col_name):
        '''
        This method drops rows that have null in a specified column from the dataframe

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''        
        self.df.dropna(axis=0, subset = col_name, inplace=True)

    def impute_constant(self, col_name, constant):
        '''
        This method replaces nulls in nominated column with a nominated constant

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe
        constant : the value inserted in place of nulls

        Updates
        -------
        self.df
        '''
        self.df[col_name].fillna(value=constant , inplace = True)

    def impute_by_median (self, column):
        '''
        This method replaces nulls in nominated column with its median

        Parameters
        ----------
        column : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''

        self.df[column].fillna(self.df[column].median() , inplace = True)
        
    def impute_by_mean (self, column):
        '''
        This method replaces nulls in nominated column with its mean

        Parameters
        ----------
        column : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.df[column].fillna(self.df[column].mean() , inplace = True)

    def log_transform(self, column):
        '''
        This method performs a log transformation on a nominated column, handling zeroes

        Parameters
        ----------
        column : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        log_column = "log_"+column
        self.df[log_column] = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)


    def show_skew(self):
        '''
        This method prints information about the skewness of numerical columns in the dataframe

        Prints
        -------
        skewness values for each relevant column
        '''
        print (self.df.skew(numeric_only = True))