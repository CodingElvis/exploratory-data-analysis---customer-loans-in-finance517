import pandas as pd

def load_data(filename):
    '''
    loads a csv file, and returns as a pandas dataframe
    '''
    dataframe = pd.read_csv(filename)
    return dataframe

