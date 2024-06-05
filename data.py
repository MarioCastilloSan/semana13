import pandas as pd


def get_data():
    return pd.read_excel('Datos_Aleatorios.xlsx')


def get_row(df:pd.DataFrame, row:int):
    return df.iloc[row]