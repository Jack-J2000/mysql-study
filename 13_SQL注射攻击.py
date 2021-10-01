''
'''
SQL注射攻击：
使用字符串格式化写的SQL语句容易受到注射攻击：
select * from tb_user where username='%s' and password='%s'

1.上面的SQL语句传入两个参数：admin 
                                ' or '1'='1   #此时的密码为万能密码，可见密码恒成立！！！
代入到SQL语句中：select * from tb_user where username='admin' and password='' or '1'='1' 

###故不能使用字符串格式化
2.传入参数可改为：admin 
                     '; update ... where '1'='1
代入可见：select * from tb_user where username='admin' and password=''; update ... where '1'='1'  
#此时相当于一次查询后接着数据库的内容被修改

防范SQL注射攻击：不使用字符串拼接
'''




