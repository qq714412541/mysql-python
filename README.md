# mysql-python

#pycharm  install  mysql-connect

#question: no modoule like mysql       
#solution: change mysql.py to mysqltest.py


#question:eror1130
#solution:      update user set host='%' where host = 'localhost';    #提供远程访问
#之后 flush pricilges    #意为更新
#create table jsontest( id int(24) not null primary key auto_increment, data blob, reportid varchar(12), status int(6), genre int(6) );
#GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '你设置的密码' WITH GRANT OPTION;
flush privileges;

#/sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT   写入修改
/etc/init.d/iptables save   保存修改
service iptables restart

#开启远程访问
https://www.cnblogs.com/weifeng1463/p/7941625.html
