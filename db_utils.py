# Contains class to support aicore eda project
import sqlalchemy
import pandas as pd
import yaml

def load_credentials():
    '''
    returns dictionary of database credentials
    '''
    with open('credentials.yaml', 'r') as file:
        cred_dic = yaml.safe_load(file)
        return cred_dic


def save_data(data):
    '''
    This method srops a specified column from the dataframe

    Parameters
    ----------
    data : pandas dataframe 

    Saves
    -------
    dataframe as csv file named 'initial_data.csv'
    '''       
    data.to_csv('initial_data.csv', index = False)


class RDSDatabaseConnector:
    '''
    This class is used to access data from the RDS database.

    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.credentials : dictionary
        dictionary with the credentials allowing access to database
    '''    
    def __init__(self, credentials):
        self.credentials = credentials

    def create_engine(self):
        '''
        This method creates an engine to connect to the database

        Returns
        -------
        connection engine
        '''

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
        '''
        This method calls create engine and uses it to access the SQL database

        Returns
        -------
        dataframe
        '''
        engine = self.create_engine()
        data = pd.read_sql('loan_payments', engine)
        return data

if __name__ == "__main__":
    creds = load_credentials()
    connector = RDSDatabaseConnector(creds)
    df = connector.get_data()
    print(df.head())
    save_data(df)
