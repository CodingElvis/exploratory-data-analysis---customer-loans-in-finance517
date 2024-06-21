import pandas as pd

def load_data():
    dataframe = pd.read_csv('initial_data.csv')
    return dataframe

df = load_data()

print (df.shape)
