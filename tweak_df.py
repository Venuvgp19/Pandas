#fixing columns and tweeking data

import pandas as pd

def fix_col(colname):
    return colname.strip().replace(' ', '_')  # replace spaces with _ on columns

def tweak_df(df_):
    return df_.rename(columns=fix_col)
    .assign(somecolumn = lambda df2 : some expression that reflects on entire column)

df = pd.read_excel('Some_sheet.xlsx',sheet_name = 'Corp')
df2 = tweak_df(df)
print(df2['somecolumn'])

