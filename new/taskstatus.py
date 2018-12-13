import pymysql
import json

class pyc:

  def pytomy(self, r,response_body):

      con = pymysql.connect(host='192.168.126.129', port=3306, user='root', db='mysql', passwd='qq714142541')
      mycur = con.cursor()
      #r = "DEMO-00004"

      sql = "SELECT * FROM jsontest \
                   WHERE reportid=" + '"' + r + '"'
      print(sql)
      mycur.execute(sql)
      # 获取所有记录列表
      results = mycur.fetchall()
      print(results)

      if results == ():
          response_body = {
              'code': 10002,
              'error': 'no task'
          }
      else:

          for row in results:
              datasql = json.loads(row[1])
              status = row[3]
              print(datasql)

              # 打印结果
              if status == 0:
                  response_body = {  # pending
                      'code': 0,
                      'status': 0
                  }
              else:
                  response_body = {  # finished
                      'code': 0,
                      'status': 1,
                      'result': datasql
                  }

              print(response_body)

      return response_body
      con.close()

