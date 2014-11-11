import pymysql
from gmpy2 import is_prime

try:
    conn=pymysql.connect(host='127.0.0.1',user='root',db='test')
    cur=conn.cursor()
except Exception:
    print("ERROR: Could not connect to mySQL database.")
index=1
print("|    Hex    |      Dec      |        Oct        |            Bin            |")
print("=============================================================================")
while True:
    try:
        query=("SELECT Primes FROM primes WHERE Number="+str(index))
        cur.execute(query)
        row=cur.fetchone()
        prime=int(row[0])
        primes=[hex(prime),prime,oct(prime),bin(prime)]
        buffer=[11,15,19,27]
        strOut=""
        
        for i in range(0,4):
            temp=""
            for j in range(0, (buffer[i]-len(str(primes[i])))):
                temp=(temp+" ")        
            strOut=(strOut+"|"+temp+str(primes[i]))

        #buffer=[(11-len(primes[0])),(15-len(primes[1])),(19-len(primes[2])),(27-len(primes[3]))]
        strOut=strOut+"|"
        print(strOut)
    except Exception:
        print("ERROR: mySQL database error.")
        break        
    except KeyboardInterrupt:
        break
    index+=1
