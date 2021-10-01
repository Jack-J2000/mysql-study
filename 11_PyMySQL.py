import pymysql

def main():
    #1.连接数据库
    conn = pymysql.connect(host='192.168.244.1',port=3306,
                           user='root',password='123456',
                            db='school',charset='utf8')
    try:
        #上下文语法，可自动关闭游标
        with conn.cursor() as cursor:  #2.获取cursor(游标对象)
            #3.执行SQL得到结果
            result = cursor.execute(    #在cursor.execute里写入SQL语句
                'insert into tb_college (collid,collname,collmaster,collweb) values (4,"皮特沃夫","凯瑟琳","http://www.func.com")')
            if result==1:
                print('添加成功！')
                # 4.手动提交，此时数据库里的内容也会相应改变
                conn.commit()
            else:
                print('添加失败！')
    except pymysql.MySQLError as error:
        print(error)
        #4.操作失败进行回滚
        conn.rollback()
    finally:
        #关闭连接释放资源
        conn.close()
    print(conn)

if __name__ == '__main__':
    main()