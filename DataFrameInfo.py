class DataFrameInfo:
    '''
    This class is used to print information about the dataframe

    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.df : a Pandas dataframe
        the dataframe on which transformations will take place
    '''
    def __init__ (self, dataframe):
        self.df = dataframe


    def print_shape (self):
        '''
        This method prints shape of the dataframe

        Prints
        -------
        shape of dataframe
        '''
        print(f"The shape of the dataframe is {self.df.shape}")


    def print_description(self):
        '''
        This method prints information about each column of the dataframe

        Prints
        -------
        title, datatype and number of non-null datapoints for each column
        '''
        print(f"The dataframe has the following columnns, with datatypes and non-null datapoints stated")
        print(df.info())


    def summarise_numeric(self):
        '''
        This method prints information about each numeric column of the dataframe

        Prints
        -------
        statistical summary measures for each column with the numeric datatype
        '''
        print (f"The dataframe has these numeric datatypes, with these summary statistics")
        summary = self.df.describe()
        display(summary.transpose())


    def count_categories(self):
        '''
        This method prints information about each categorical column of the dataframe

        Prints
        -------
        counts of each value in each column with categorical datatype
        '''

        for column in self.df.columns:
            if (self.df[column].dtype) == 'category':
                print("-------------------------------------")
                print(f"Categorical Data Column: {column}")
                print(self.df[column].value_counts())
                print ("-----------------------------------")
    
    def count_nulls (self):
        '''
        This method prints information about the share of null values in each column

        Prints
        -------
        counts of each value in each column with categorical datatype
        '''
        print("percentage of missing values in each column:")
        print(self.df.isna().mean() * 100 )
