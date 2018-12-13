import pymysql
import json

class pyc:

  def pytomy(self,d,r,s):
    # 数据库连接
    con = pymysql.connect(host='192.168.126.129', port=3306, user='root', db='mysql', passwd='qq714142541')
    mycur = con.cursor()

    # 字段打包成json
    d_json = json.dumps(d)

    # 生成sql语句写入sql
    tsql2 = "update jsontest set data='{json}',status="
    sql2 = tsql2.format(json=pymysql.escape_string(d_json));
    #update jsontest set data='{\"na\": \"xp5\"}',status=1 where reportid="DEMO-00011"
    sql3 = sql2 +  s+ " "+ "where reportid=" + '"' + r + '"'

    # 执行写入操作
    mycur.execute(sql3)
    mycur.connection.commit()
    print(sql3)
    con.close()
#直接运行
'''
if __name__ == '__main__':
    import sys

    sys.path.append('/Users/yuanz/PycharmProjects/pymysql')
    from data import data
    mypyc = pyc()
    d = data.d         #jsondata

    r = data.r         #reportid

    s = data.saft      #status after process

    mypyc.pytomy(d,r,s)
'''