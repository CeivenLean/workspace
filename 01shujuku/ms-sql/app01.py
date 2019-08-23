import pymssql


conn=pymssql.connect(
    host='192.168.100.2',
    user='sa',
    password='Sql2008',
    database='opuhis'
)
cur=conn.cursor()

SQL='''
select * from view_sh_depart
'''

cur.execute(SQL)
r = cur.fetchall()
print(r)