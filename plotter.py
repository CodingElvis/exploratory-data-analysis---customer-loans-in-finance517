import seaborn as sns
import plotly.express as px


class Plotter:
    '''
    This class is used to plot data stored in a dataframe.

    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.df : a Pandas dataframe
        the dataframe on from which data for plots will be drawn
    '''
    def __init__(self, df):
        self.df = df


    def histogram(self, variable, bars=10):
        '''
        This method plots a histogram of a variable in the dataframe

        Parameters
        ----------
        variable : a string that forms a column name in our dataframe
        bars : int, bins to use, defaults 10
        
        '''
        self.df[variable].hist(bins=bars)
    
    def pdf (self, variable):
        '''
        This method plots a pdf of a variable in the dataframe

        Parameters
        ----------
        variable : a string that forms a column name in our dataframe
               
        '''
        sns.histplot(data=self.df, x=variable, kde=True)
        sns.despine()

    def box (self, variable):
        '''
        This method makes a box-whiskers plot of a variable in the dataframe

        Parameters
        ----------
        variable : a string that forms a column name in our dataframe         
        '''
        fig = px.box(self.df, y=variable,width=600, height=500)
        fig.show()