
#import pandas
import pandas as pd
#make a df from the cvs file of 5000 shuffled values
df = pd.read_csv('arcos_all_washpost_shuf5000.csv')
#collumn of just years
years = df['TRANSACTION_DATE'].astype(str).str[-4:].astype(int)
#data frame of years and counts
dfCounts = pd.DataFrame(years.value_counts())

totalOpioidCount = 178598026
cvsFileRowCount = 5000
print((dfCounts['TRANSACTION_DATE']/cvsFileRowCount)*totalOpioidCount)
