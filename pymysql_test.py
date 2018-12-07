import pymysql
import json

#字段
d = {'name': 'xpleaf'}

r = "DEMO-00001"


#数据库连接
con = pymysql.connect(host='192.168.126.129', port=3306, user='root', db='mysql', passwd='qq714142541')
mycur=con.cursor()


#字段打包成json
d_json = json.dumps(d)


#生成sql语句写入sql
#tsql = "insert into jsontest(data) values('{json}')";
#sql = tsql.format(json=pymysql.escape_string(d_json));#insert into jsontest(data) values('{\"name\": \"xpleaf\"}')

sql1 = "insert into jsontest(reportid) values("+'"'+ r +'"'+")"

tsql2 = "update jsontest set data='{json}' where reportid="

sql2 = tsql2.format(json=pymysql.escape_string(d_json));

sql3 = sql2 +'"'+ r +'"'

#执行写入操作
#mycur.execute(sql)
mycur.execute(sql1)
mycur.execute(sql3)
mycur.connection.commit()#必须写这段数据库才有显示

print("1")
print(type(d_json),type(d))
print(sql1,sql3)

mycur.execute("SHOW DATABASES")

for x in mycur:
    print(x)
