import pandas as pd

def cleanData(file):
    # Read in the data to pandas dataframe
    df = pd.read_excel(file,
                       skiprows=5,                  # Skip first 5 rows of excel file
                       skipfooter=6,                # Skip last 6 rows of excel file
                       header=[0],                  # Header is in the first row
                       index_col=[0])               # Use first column as the index

    # Drop the empty rows
    df.dropna(how='all', inplace=True)

    # Pivot years and reset the index so the old index is added as a column
    df = df.stack([0]).reset_index()

    # Rename the columns by using their index position
    # Set inplace to True so you don't have to assign it back to dataframe
    df.rename(columns={df.columns[0]: 'State',
                       df.columns[1]: 'Year',
                       df.columns[2]: 'Divorce Rate'}
              , inplace=True)

    # Export the dataframe to excel file
    df.to_excel(excel_writer= 'DivorceRates_clean.xls',             # Name the excel file "DivorceRates_clean"
                sheet_name='Divorce Rates',                         # Name the sheet "Divorce Rates"
                na_rep='null',                                      # Treat n/a as null
                index=False)                                        # Don't include index



# Call the function with uncleaned file
#cleanData('state-divorce-rates.xlsx')
