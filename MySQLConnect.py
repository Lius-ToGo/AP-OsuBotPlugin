import pymysql


class MySQLConnect:
    __excount = 0

    # 数据库连接方法（闭包方法MySQLConn）
    @staticmethod
    def __MySQLConn():
        MySQLConnect.__excount += 1
        try:
            conn = pymysql.connect(host="127.0.0.1", user="osusql", passwd="123M", port=3306, db="osusql", charset="utf8")
            if MySQLConnect.__excount < 2\
                    :
                print("数据库连接成功")
            return conn
        except Exception as e:
            print("数据库连接失败")
            MySQLConnect.__excount = 0
            print(e)
            conn.close()


    # 数据库命令执行方法excute
    @staticmethod
    def execute(sql):
        conn = MySQLConnect.__MySQLConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            e='0'
            conn.close()
            return e
        except Exception as e:
            conn.rollback()
            conn.close()
            return e



    # 查询命令执行executeselect
    @staticmethod
    def executeselect(sql):
        def returnrec():
            records = []
            for row in cur.fetchall():
                records.append(row)
            return row

        conn = MySQLConnect.__MySQLConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            print("查询命令执行成功")
            row = returnrec()
            conn.close()
            return row
        except Exception as e:
            conn.rollback()
            e=str(e)+"命令执行失败 0"
            conn.close()
            return e
