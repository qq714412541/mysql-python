import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.126.129",
    user="root",
    passwd="*"
)

print(mydb)
