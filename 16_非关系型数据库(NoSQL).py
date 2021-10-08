''
'''
非关系型数据库(NoSQL)：保存海量数据，速度更快
- 文档数据库 - MongoDB/ElasticSearch 
- 键值对数据库 - Redis
- 列族数据库
- 图数据库
Redis主要把数据存储在内存中，其“缓存”的性质远大于其“数据存储“的性质，
其中数据的增删改查也只是像变量操作一样简单；
Redis（Remote Dictionary Server )，即远程字典服务，是一个开源的使用ANSI C语言编写、支持网络、
可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。从2010年3月15日起，
Redis的开发工作由VMware主持。从2013年5月开始，Redis的开发由Pivotal赞助。


MongoDB却是一个“存储数据”的系统，增删改查可以添加很多条件，就像SQL数据库一样灵活，
这一点在面试的时候很受用。

'''
'''
Redis 一般在Linux下使用，把数据全部放在内存，保存在文件里作持久化，最适合做高速缓存

在windows里的Redis:   #有两个配置文件，我使用redis.windows.conf
需要在redis的目录下打开命令行
启动服务：redis-server.exe redis.windows.conf\配置文件  


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


Redis文件夹下有一个.rdb或.aof文件，该文件是保存已敲入的命名的。
下次启动Redis只要再执行这些命令，数据库就会恢复。
若.aof文件被破坏，可以执行：redis-check-aof --fix 文件名.aof   来修复该文件
.rdb 修复  redis-check-rdb --fix 文件名.rdb
'''

