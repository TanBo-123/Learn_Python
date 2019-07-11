# learn_flask
##ubuntu下mysql操作方式：
###登录：mysql -u root -p   
- 登录远程主机：mysql [-h 192.168.205.129 –P 3306] –uroot -p
　　　　- h 连接服务端数据库的IP地址
　　　　- P(大写) 连接的端口号，一般为3306
　　　　- u 用户权限
　　　　- p(小写) 输入密码，一般为mysql

###退出数据库客户端
　　-  exit、quit、ctrl+d

###数据库操作
    使用命令创建数据库
        create database 数据库名;
        create database 数据库名 character set utf8;
        show create database 数据库名;
    修改数据库编码
        alter database 数据库名 character set utf8;
    删除数据库
        drop database 数据库名;
    切换、使用数据库
        use 数据库名;
    显示当前数据库
        select database();
    展示所有数据库
        show databases;
    删除数据库
        drop database 数据库名;
        
###数据表操作
    创建数据表
        create table 表名(
    　　　　字段1 字段类型,
    　　　　字段2 字段类型,
    　　　　字段3 字段类型……);
    查询数据表中部分/全部的行和列
        select col1,col2,col3….from table;
        select * from table;