#!/usr/bin/python

import pymysql
from gmpy2 import next_prime
try:
    conn=pymysql.connect(host='mysql15.000webhost.com',user='a6617813_prime',passwd='Program&Destroy',db='a6617813_primes')
    #conn=pymysql.connect(host='localhost',user='root',db='test')
    cur=conn.cursor()
    cur.execute("SELECT * FROM prime_numbers ORDER BY Number DESC LIMIT 1")
    row=cur.fetchone()
    counter=int(row[0])
    prime=int(row[1])
    print("Starting at:",prime)
except Exception:
    print("ERROR: Could not connect to mySQL database.")
    counter=0
index=0
if counter:
    print("Press ^C to exit.\n")
    try:
        while True:
            counter+=1
            prime=next_prime(prime)
            query="INSERT INTO `prime_numbers`(`Number`, `Primes`) VALUES ("+str(counter)+","+str(prime)+")"
            cur.execute(query)
            index+=1
            if index>20000:
                conn.commit()
                index=0
    except KeyboardInterrupt:
        print("User terminated program.")
    except Exception:
        print("ERROR: Program quit unexpectedly.")
    conn.commit()
    print("Last number stored:",prime)
    cur.close()
    conn.close()
    print("Database connection closed.")
print("Goodbye.")
