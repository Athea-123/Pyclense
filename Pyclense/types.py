import pandas as pd

class TypeCleaner:
  def __init__(self, df):
    self.df = df

  def object_to_int(self, column):
    # errors= 'coerce' turns text like 'missing' or 'N/A' into NaN
    self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
    return self.df

  def object_to_datetime(self, column):
    self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
    return self.df

  def object_to_float(self, column):
    self.df[column] = pd.to_numeric(self.df[column], downcast='float', errors='coerce')
    return self.df
