import seaborn as sns
import plotly.express as px


class Plotter:
    
    def __init__(self, df):
        self.df = df

    def histogram(self, variable, bars=10):
        self.df[variable].hist(bins=bars)
    
    def pdf (self, variable):
        sns.histplot(data=self.df, x=variable, kde=True)
        sns.despine()

    def box (self, variable):
        fig = px.box(self.df, y=variable,width=600, height=500)
        fig.show()