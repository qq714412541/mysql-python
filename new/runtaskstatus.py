import sys

sys.path.append('/Users/yuanz/PycharmProjects/pymysql')
from taskstatus import pyc
from data import data

data = data()

d = data.d  # jsondata

r = data.r  # reportid

s = data.saft  # status after process

response_body = {}

connect = pyc()
response_body = connect.pytomy(r, response_body)
print(response_body)
