import redis
def main():
    client = redis.Redis(host='192.168.244.1',port=6379,
    )
    print(client)
    client.set('username','hellokitty',ex=300)  #ex为超时，超过300秒消失
    print(client.ttl('username'))   #ttl可用来查看键值对的存活时间
    print(client.get('username'))  #由键取值  结果：b'hellokitty' b代表: bytes 字节串
    print(client.get('username').decode())  #解码

    client.set('jj','100')
    client.incr('jj') #值自增
    client.incrby('jj',50)  #值加50
    print(int(client.get('jj').decode()))

    client.hset('stu1','id','001')
    print(client.hgetall('stu1'))
    print(client.hget('stu1','id').decode())

    client.rpush('list1',10,20,30,40)
    print(client.lrange('list1',0,-1))
if __name__ == '__main__':
    main()