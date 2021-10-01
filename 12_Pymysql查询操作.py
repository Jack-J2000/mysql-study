import pymysql

class College(object):    #建立学院对象
    def __init__(self,collid,collname,collmaster,collweb):
        self.collid=collid
        self.collname = collname
        self.collmaster = collmaster
        self.collweb = collweb
    def __str__(self):
        return f'{self.collid}\t{self.collname}\t{self.collmaster}\t{self.collweb}'


#存放查询到的数据时，适合用字典存放，需要在connect参数里修改游标的类型
def main():

    #1.连接数据库
    conn = pymysql.connect(host='192.168.244.1',port=3306,
                           user='root',password='123456',
                            db='school',charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)   #修改游标类型为字典
    try:
        #上下文语法，可自动关闭游标
        with conn.cursor() as cursor:  #2.获取cursor(游标对象)
            #3.执行SQL得到结果
            cursor.execute(  # 在cursor.execute里写入SQL语句
                'select collid,collname,collmaster,collweb from tb_college')
            for row in cursor.fetchall():
                college = College(**row)
                print(college)   #通过类进行调用数据库里的数据
            # print(cursor.fetchone())   #由于游标的移动，拿不到数据了，因为现在游标已经在最后一行了
            # print(cursor.fetchmany())
    except pymysql.MySQLError as error:
        print(error)
    finally:
        #关闭连接释放资源
        conn.close()
    print(conn)

if __name__ == '__main__':
    main()