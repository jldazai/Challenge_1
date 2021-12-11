import pandas as pd
from pandas.core.indexing import convert_to_index_sliceable
from requests.sessions import CaseInsensitiveDict
from sodapy import Socrata

client = Socrata('www.datos.gov.co', None)

results = client.get('sdvb-4x4j', limit=1000000)

df = pd.DataFrame.from_records(results)

print(df)

print(df.isnull().sum().sum())

print(df.dtypes)

print(df.isnull().any(1).to_numpy().nonzero())

print(df.loc[2401].isnull())

df.fillna(method='bfill',limit=2, inplace=True)

print(df.isnull().any(1).to_numpy().nonzero())

convert_dic = {'cantidad':int}

df = df.astype(convert_dic)

print(df.dtypes)

print(df[df['cantidad']>=10])
