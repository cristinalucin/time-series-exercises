import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

def prepare_sales(df):
    '''This function prepares sales data by adding columns and ensuring date time is 
    set to the index'''
    # Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date)

    # Set the index as that date and then sort index (by the date)
    df = df.set_index("sale_date").sort_index()
    
    #Adding month column
    df['month'] = df.index.month_name()
    
    #Adding week column
    df['day_of_week'] = df.index.day_name()
    
    #Adding sales total column
    df['sales_total'] = df['item_price'] * df['sale_amount']
    
    return df

#Prep power data
def prepare_ops(df):
    # Reassign the date column to be a datetime type
    df.Date = pd.to_datetime(df.Date)
    # Set the index as that date and then sort index (by the date)
    df = df.set_index("Date").sort_index()
    #Adding month column
    df['month'] = df.index.month_name()
    #Adding Year Column
    df['year'] = df.index.year
    #Impute zeroes for missing values
    df = df.fillna(value=0)
    
    return df