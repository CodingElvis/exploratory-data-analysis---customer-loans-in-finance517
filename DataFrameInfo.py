class DataFrameInfo:
    
    def __init__ (self, dataframe):
        self.df = dataframe

    def print_shape (self):
        print(f"The shape of the dataframe is {self.df.shape}")
        #print(self.df.shape)

    def print_description(self):
        print(f"The dataframe has the following columnns, with datatypes and non-null datapoints stated")
        print(df.info())

    def summarise_numeric(self):
        print (f"The dataframe has these numeric datatypes, with these summary statistics")
        ##########print (self.df.describe())
        summary = self.df.describe()
        display(summary.transpose())
        #print (self.df.describe.transpose())

    def count_categories(self):
        for column in self.df.columns:
            if (self.df[column].dtype) == 'category':
                print("-------------------------------------")
                print(f"Categorical Data Column: {column}")
                print(self.df[column].value_counts())
                print ("-----------------------------------")
    
    def count_nulls (self):
        print("percentage of missing values in each column:")
        print(self.df.isna().mean() * 100 )
