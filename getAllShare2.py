from sqlalchemy.engine import create_engine
import tushare as ts
import pandas as pd
import re

engine = create_engine("mysql://root:ok123@localhost/allShares?charset=utf8")
connection = engine.connect()

df1 = pd.read_sql("select * from all20170209 order by code limit 2",connection)
df2 = pd.read_sql("select * from shareBasics order by code limit 2",connection,index_col='code')

#print df2
for i in df1['code']:
    print type(i)
    print df2.loc[i,'timeToMarket']
    x = df2.loc[i,'timeToMarket']
    itimeToMaket = re.match(r'(\d{4})+(\d{2})+(\d{2})',str(x))
    print itimeToMaket.group(3)
    imergetimeToMaket = itimeToMaket.group(1) + '-' + itimeToMaket.group(2) + '-' + itimeToMaket.group(3)
    print imergetimeToMaket
    dfi = ts.get_h_data(i,autype='qfq',start=imergetimeToMaket,end='1992-01-01')
    print dfi