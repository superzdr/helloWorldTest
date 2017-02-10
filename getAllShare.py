import pandas as pd
from sqlalchemy.engine import create_engine
import tushare as ts

engine = create_engine("mysql://root:ok123@localhost/allShares?charset=utf8")
connection = engine.connect()

df1 = ts.get_stock_basics()
df1 = df1.reset_index()
df1.to_sql("shareBasics",connection,if_exists="replace")

df0 = ts.get_today_all()
df0.to_sql("all20170209",connection,index = False,if_exists="replace")

print 'ok,done'