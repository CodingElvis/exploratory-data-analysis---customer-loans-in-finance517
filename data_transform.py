import pandas as pd

class DataTransform:
    '''
    This class is used to transform data inside a dataframe.
    Methods focus on assigning datatypes and related tasks 

    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.df : a Pandas dataframe
        the dataframe on which transformations will take place
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe

    
    def col_to_category (self, col_name):
        '''
        This method assigns a specified column to the category datatype

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''                
        self.dataframe = self.dataframe.astype({col_name : 'category'})

    def col_to_object (self, col_name):
        '''
        This method assigns a specified column to the object datatype

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.dataframe = self.dataframe.astype({col_name : 'object'})
        

    def strip_months (self, col_name):
        '''
        This method strips the text "months" from data in a nominated column
        It can be used to prepare a column with this text for transform to numeric

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''        
        self.dataframe[col_name] = self.dataframe[col_name].str.replace(" months", "")


    def col_to_float (self, col_name):
        '''
        This method assigns a specified column to the float datatype

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.dataframe = self.dataframe.astype({col_name : 'float'})


    def drop_col(self, col_name):
        '''
        This method drops a specified column from the dataframe

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.dataframe.drop(col_name, axis = 'columns', inplace = True)


    def add_day_15 (self, col_name):
        '''
        This method adds the text "15-" at the start of (string) values in a column

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe

        Updates
        -------
        self.df
        '''
        self.dataframe[col_name] = '15-' + self.dataframe[col_name].astype(str)


    def col_to_date (self, col_name):
        '''
        This method assigns a specified column to the date time datatype

        Parameters
        ----------
        col_name : a string that forms a column name in our dataframe, with string dates DD-Month-YYYY

        Updates
        -------
        self.df
        '''
        self.dataframe[col_name] = pd.to_datetime(self.dataframe[col_name], dayfirst=True)