import pandas as pd 

class StringCleaner: 
  def __init__(self, df):
    self.df = df

  def to_lowercase(self, column):
    self.df[column] = self.df[column].str.lower()
    return self.df

  def to_uppercase(self, column):
    self.df[column] = self.df[column].str.upper()
    return self.df

  def to_titlecase(self, column):
    self.df[column] = self.df[column].str.title()
    return self.df

  def strip_whitespace(self, column):
    self.df[column] = self.df[column].str.strip()
    return self.df
