import pandas as pd

df_transactions = pd.read_csv('../inputs/PD2023W02_TRANSACTIONS.csv')
df_swift = pd.read_csv('../inputs/PD2023W02_SWIFT_CODES.csv')
# In the Transactions table, there is a Sort Code field which contains dashes. 
# We need to remove these so just have a 6 digit string
df_transactions['Sort Code'].replace('-', '', inplace=True, regex=True)
# Use the SWIFT Bank Code lookup table to bring in additional information about the SWIFT code 
# and Check Digits of the receiving bank account
df_merged = pd.merge(df_transactions, df_swift, on=['Bank', 'Bank'])
# Add a field for the Country Code (hint)
# Hint: all these transactions take place in the UK so the Country Code should be GB
df_merged['Country Code'] = 'GB'
# IBAN
# Country - Check - SWIFT - sort - account#
df_merged['Account Number'] = df_merged['Account Number'].astype('str')
df_merged['IBAN'] = df_merged[[ 'Country Code'
                               ,'Check Digits'
                               ,'SWIFT code'
                               ,'Sort Code'
                               ,'Account Number']].apply(''.join, axis=1)
df_merged[['Transaction ID','IBAN']].to_csv('./outputs/PD2023W02.csv')
