#!/usr/bin/python

import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',db='test')
cur=conn.cursor()

def Remove_multiples(startNum):
    try:
        cur.execute("SELECT * FROM `possibleprimes` ORDER BY Numbers DESC LIMIT 1")
        x=cur.fetchone()
        lastNum=x[0]
    except Exception as err:
        print("Could not connect to mySQL database.\nERROR:", str(err),"\n")
    print("Removing multiples of",startNum,"...\n")
    try:
        cur.execute("SELECT * FROM `possibleprimes` ORDER BY Numbers")
        x=cur.fetchone()
        while x[0]<startNum:
            x=cur.fetchone()
        baseNum=x[0]
        remList=[]
        
        while x is not None and len(x):
            remList.append(baseNum*x[0])
            x=cur.fetchone()
        try:
            cur.execute("DELETE FROM `possibleprimes` WHERE Numbers IN "+str(remList).replace("[","(").replace("]",")"))
        except Exception as err:
            print("Could not remove value\nERROR:", str(err))
        conn.commit()
    except Exception as err:
        print("Database error.\nERROR:", str(err))
    except KeyboardInterrupt:
        exit(KeyboardInterrupt)
q=[7]
try:
    while q is not None and len(q):
        Remove_multiples(int(q[0]))        
        cur.execute("SELECT * FROM `possibleprimes` WHERE Numbers>"+str(q[0]))
        q=cur.fetchone()
except Exception:
    print("Could not select from ",str(q[0]))
except KeyboardInterrupt:
    print("User terminated proccess.")
conn.close()
print("...done.")
