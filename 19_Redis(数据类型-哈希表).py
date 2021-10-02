''
'''
##哈希存储###
性能非常好的存储方案 - set
obj ---> 哈希函数 ---> 哈希码(散列码) ---> 标示对象在内存中存储的位置

哈希存储关键在于哈希函数；
文件 ---> MD5 / SHA1 / SHA256 --->哈希码(数字指纹/签名)
'''
#计算哈希摘要
import hashlib
def main():
    digester = hashlib.md5()
    with open(r'requirement.txt', 'rb') as file_stream:
        data = file_stream.read(1024)
        while data:
            digester.update(data)
            data = file_stream.read(1024)
    file_stream.close()
    print(digester.hexdigest())  #16形式字符串


if __name__ == '__main__':
    main()