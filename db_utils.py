# Contains class to support aicore eda project
import sqlalchemy
import pandas as pd
import yaml

def load_credentials():
    with open('credentials.yaml', 'r') as file:
        cred_dic = yaml.safe_load(file)
        return cred_dic

creds = load_credentials()

def save_data(data):
    data.to_csv('initial_data.csv', index = False)

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

    def create_engine(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = self.credentials['RDS_HOST']
        USER = self.credentials['RDS_USER']
        PASSWORD = self.credentials['RDS_PASSWORD']
        DATABASE = self.credentials['RDS_DATABASE']
        PORT = self.credentials['RDS_PORT']
        engine = sqlalchemy.create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine

    def get_data(self):
        engine = self.create_engine()
        data = pd.read_sql('loan_payments', engine)
        return data


creds = load_credentials()
connector = RDSDatabaseConnector(creds)
df = connector.get_data()
print(df.head())

save_data(df)
