import pandas as pd

def load_data(filename):
    dataframe = pd.read_csv(filename)
    return dataframe

'''
df = load_data()

df.info()

'''