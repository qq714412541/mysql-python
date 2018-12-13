import sys
sys.path.append('/Users/yuanz/PycharmProjects/pymysql')
from beforepro import pyc
from data import data



data = data()

r = data.r         #reportid
s = data.sbef      #status   before process
g = data.g         #genre for ills




connect = pyc()
connect.pytomy(r,s,g)