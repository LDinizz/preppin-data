import pandas as pd

df = pd.read_csv('../inputs/PD2023W01.csv')

## Split Transaction code to Bank
df['Bank'] = df['Transaction Code'].str.split('-', 1).str[0]
df_by_bank = df.groupby(['Bank'])['Value'].sum()
## By bank Output
df_by_bank.to_csv('./outputs/PD2023W01_01.csv')

df['Online or In-Person'] = df['Online or In-Person'].replace([21,],['Online','In-Person'])
## Transaction Date to Weekday
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Transaction Date'] = df['Transaction Date'].dt.day_name()

df_by_bank_online_date = df.groupby(['Bank','Online or In-Person','Transaction Date'])['Value'].sum()
## By Bank, Online or In Person and Transaction Date
df_by_bank_online_date.to_csv('./outputs/PD2023W01_02.csv')

df_by_bank_Customercode = df.groupby(['Bank','Customer Code'])['Value'].sum()
## By Bank, Online or In Person and Transaction Date
df_by_bank_Customercode.to_csv('./outputs/PD2023W01_03.csv')
