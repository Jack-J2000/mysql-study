''
'''
非关系型数据库(NoSQL)：保存海量数据，速度更快
- 文档数据库 - MongoDB/ElasticSearch 
- 键值对数据库 - Redis
- 列族数据库
- 图数据库
'''
'''
Redis 一般在Linux下使用，把数据全部放在内存，保存在文件里作持久化，最适合做高速缓存
在windows里的Redis:
D:\>cd Redis

D:\Redis>redis-cli.exe
127.0.0.1:6379> ping
PONG   #系统回复 
127.0.0.1:6379> get username
"jackfrued"
127.0.0.1:6379> set 130123456 jjj ex 300  #ex 设置300秒的存活时间
OK
127.0.0.1:6379> ttl 130123456      #ttl命令
(integer) 289   #显示的是还可以存活的时间 289秒
127.0.0.1:6379>exit   #退出客户端


D:\Redis>redis-benchmark     #该命令可检验Redis的性能
'''

