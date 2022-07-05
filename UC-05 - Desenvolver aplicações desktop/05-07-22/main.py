import mysql.connector as mys

conecta = mys.connect(host='local', user='root', password='q1w2e3', database='sus')
cursor = conecta.cursor()
