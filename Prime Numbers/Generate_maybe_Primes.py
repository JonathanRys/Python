#!/usr/bin/python

import pymysql
counter=[7,9,11,13]
try:
    conn=pymysql.connect(host='127.0.0.1',user='root',db='test')
    cur=conn.cursor()
    cur.execute("SELECT * FROM possibleprimes ORDER BY Numbers DESC LIMIT 1")
    row=cur.fetchone()
#Add 2,3,5
    if row[0] is None:
        cur.execute("INSERT INTO `possibleprimes` (`Numbers`) VALUES (2,3,5)")
        row[0]=5
    elif row[0]<5:
        cur.execute("DELETE * FROM `possibleprimes`")
        cur.execute("INSERT INTO `possibleprimes` (`Numbers`) VALUES (2,3,5)")
        row[0]=5
except Exception as err:
    print("Could not connect to mySQL database.\nERROR:", str(err),"\n")
#set start values based on counter[0]
last=0
counter[0]=row[0]+2
counter=[counter[0],counter[0]+2,counter[0]+4,counter[0]+6]
for index, i in enumerate(counter):
    if i%5==0 or i==last:
        counter[index]+=2
    last=counter[index]
print("Starting at:",counter[0])
try:
    while True:
        for index, i in enumerate(counter):
            if not i%3==0:
                query="INSERT INTO `possibleprimes`(`Numbers`) VALUES ("+str(i)+")"
                cur.execute(query)
                #print(i)
            counter[index]+=10
except KeyboardInterrupt:
    conn.commit()
    print("User terminated process.\nLast number stored:", i)
except Exception as err:
    print("Could not insert data in SQL database.\nERROR:", str(err),"\n")
