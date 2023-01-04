import pymysql

conn = pymysql.connect(host='10.116.96.230', port=3306, user='root', passwd='Ssxr.com@123', charset='utf8')
cursor = conn.cursor()


cursor.execute("show databases;")
result = cursor.fetchall()
print(result)

