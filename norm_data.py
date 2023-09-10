import pandas as pd

def convert_to_float(value):
    try:
        return round(float(value.replace(',', '.')), 2)
    except ValueError:
        return value
df = pd.read_csv('data\SALES.csv')
df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date']).dt.date

df['Sales Liter'] = df['Sales Liter'].apply(convert_to_float)

df.to_csv('data\\new_sales.csv', index=False)
