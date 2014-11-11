#!/usr/bin/python

import pymysql
try:
    print("Connecting to mySQL database...",end="")
    conn=pymysql.connect(host='127.0.0.1',user='root',db='test')
    cur=conn.cursor()
    cur.execute("SELECT * FROM `possibleprimes` ORDER BY Numbers ASC")
    testVal=cur.fetchall()
    cur.execute("SELECT Primes FROM `primes` WHERE Primes<"+str(testVal[-1][0])+" ORDER BY Primes ASC")
    print("OK\nChecking tables for inconsistencies...")
    records=0
    for val in testVal:
        prime=cur.fetchone()
        if val is None or prime is None:
            print("Records checked:",records)
            break
        elif val[0]!=prime[0]:
            print("Table mis-match:", val[0], "and", prime[0])
            response=input("Continue checking? y/n> ")
            if response!="y" and response!="Y":
                break
        records+=1
except Exception as err:
    print("ERROR:",str(err))
except KeyboardInterrupt:
    print("User terminated process.\nGoodbye.")
print("...done.")

