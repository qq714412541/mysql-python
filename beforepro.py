import pymysql


class pyc:

    def pytomy(self,r,s,g):
        # 数据库连接
        con = pymysql.connect(host='192.168.126.129', port=3306, user='root', db='mysql', passwd='qq714142541')
        mycur = con.cursor()


        #insert into jsontest(reportid,status,genre) values("DEMO-00011", "0", "1" )
        sql1 = "insert into jsontest(reportid,status,genre) values(" + '"' + r + '"' + ", " + '"' + s + '"' + ", " + '"' + g + '"' + " )"
        #sql2 = "insert into jsontest(status) values(" + '"' + s + '"' + ")"
        #sql3 = "insert into jsontest(genre) values(" + '"' + g + '"' + ")"

        mycur.execute(sql1)
        #mycur.execute(sql2)
        #mycur.execute(sql3)
        mycur.connection.commit()



        print(sql1)

#直接运行
if __name__ == '__main__':

    import sys
    sys.path.append('/Users/yuanz/PycharmProjects/pymysql')
    from data import data

    data = data()
    mypyc = pyc()
    r = data.r         #reportid
    s = data.sbef      #status   before process
    g = data.g         #genre for ills

    mypyc.pytomy(r,s,g)