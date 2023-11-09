import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    countries = df.groupby("country")["marketcap"].sum()
    countries.sort_values(ascending=False,inplace=True)
    countries = countries/1000000000000
    countries = countries.iloc[:10].to_frame()
    countries.reset_index(inplace=True)
    return countries