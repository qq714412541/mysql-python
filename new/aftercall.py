import sys
sys.path.append('/Users/yuanz/PycharmProjects/pymysql')
from afterpro import pyc
from data import data


data = data()

d = data.d  # jsondata

r = data.r  # reportid

s = data.saft  # status after process




connect = pyc()
connect.pytomy(d,r,s)
