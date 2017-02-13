import pandas as pd
from sqlalchemy.engine import create_engine
import tushare as ts
import re

engine = create_engine("mysql://root:ok123@localhost/allSharesTick?charset=utf8")
connection = engine.connect()

engineDayline = create_engine("mysql://root:ok123@localhost/allSharesDayline?charset=utf8")
connectionDayline = engineDayline.connect()

df1 = pd.read_sql("show tables",connectionDayline)

checklist = 'good'
dfCheckExist = pd.read_sql('show tables',connection)
for checkOne in dfCheckExist['Tables_in_allSharesTick']:
    checklist = checklist + checkOne

selectedCode = []
for i in range(len(df1['Tables_in_allSharesDayline'])):
    if i%20 == 1:
        print i
        print df1.iloc[i,0]
        selectedCode.append(df1.iloc[i,0])
print selectedCode

for i in selectedCode:
    code = re.search(r'\d{6}',i)
    code = code.group(0)
    print type(code)
    print code

    if re.search(code,checklist):
        print 'Already Exists'
        continue

    dfi = pd.read_sql('select date from ' + i+ ' order by date',connectionDayline)
    print dfi
    controlFirstDF = 1;
    for everyday in dfi['date']:
        everyday = re.match(r'(\d{4})-(\d{2})-(\d{2})',str(everyday))
        everydayDash = everyday.group(1) + '-' + everyday.group(2)+ '-' + everyday.group(3)
        everyday = everyday.group(1) + everyday.group(2) + everyday.group(3)

        print int(everyday)
        if int(everyday) < 20041008:
            continue
            print 'heppen'

        print everydayDash
        print code

        dfeveryday = ts.get_tick_data(code,everydayDash,retry_count= 10, pause = 1)
        dfeveryday['date'] = everyday
        dfeveryday['keyTime'] = dfeveryday['date'] + '-' + dfeveryday['time']
        if controlFirstDF == 1:
            mdf = dfeveryday
            controlFirstDF = controlFirstDF + 1
            print len(dfeveryday)
        else:
            mdf = mdf.append(dfeveryday)
            print len(dfeveryday)

    #print mdf
    mdf.to_sql('tick' + code,connection,if_exists = 'replace',chunksize = 1000)

