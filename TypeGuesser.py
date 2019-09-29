from csv import reader
import pandas as pd


def parseCSV(filename="pokemon.csv"):  #return (fields, rows)
    return pd.read_csv(filename)
