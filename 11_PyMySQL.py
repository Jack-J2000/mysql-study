import pymysql

def main():
    conn = pymysql.connect(host='192.168.244.1',port=3306,
                           user='root',password='123456',
                            db='school',charset='utf8')
    try:
        #上下文语法，可自动关闭游标
        with conn.cursor() as cursor:  #cursor游标
            result = cursor.execute(
                'insert into tb_student values (1234,"卡萨丁",1,"1890-1-1","广东东莞",3)')
            if result==1:
                print('添加成功！')
                # 需要手动提交，此时数据库里的内容也会相应改变
                conn.commit()
            else:
                print('添加失败！')
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


    print(conn)




if __name__ == '__main__':
    main()