import pandas as pd

Insurance_rates = pd.read_csv('US_Homeinsurance_Rates.csv', delimiter = ',')
Insurance_rates.head ()


Insurance_rates.sort (['2013', 'state'], ascending = [1, 0])

Insurance_rates.describe ()
Insurance_rates.median ()
Insurance_rates.mean ()


Insurance_rates ['Percentage Change'] = (Insurance_rates ['2013']-Insurance_rates ['2003'])*100 / Insurance_rates ['2013']

print Insurance_rates.loc[:,['state','2003','2013','Percentage Change']]
