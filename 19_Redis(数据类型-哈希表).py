''
'''
##哈希存储###
性能非常好的存储方案 - hset
obj ---> 哈希函数 ---> 哈希码(散列码) ---> 标示对象在内存中存储的位置

哈希：
hset
hmset
hget   #由一个键看一个值
hmget #由多个键找多个值
hvals  #由对象看所有值
hgetall #由对象看所有的键值对
hdel    #删除一个键值对
hkeys  #看所有的键


哈希存储关键在于哈希函数；
文件 ---> MD5 / SHA1 / SHA256 --->哈希码(数字指纹/签名)
单向哈希函数：md5 
'''

#计算哈希摘要
import hashlib
def main():
    digester = hashlib.md5()
    with open(r'requirement.txt', 'rb') as file_stream:
        file_iter =  iter(lambda: file_stream.read(1024),b'' )   #iter的使用，转为可迭代的类型
        for data in file_iter:
            digester.update(data)

    print(digester.hexdigest())  #16进制形式字符串
    file_stream.close()

if __name__ == '__main__':
    main()