from logging import getLogger

import pymysql

log = getLogger(__name__)


class DBSession:

    @staticmethod
    def getConn(self):
        # 커서 생성
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            db='test',
            charset='utf8',
            port=4491
        )
        return conn

    @classmethod
    def runSQL(cls, sql):
        try:
            conn = cls.getConn()
            # 커서 생성
            cur = conn.cursor()
            # sql문 실행
            cur.execute(sql)
            result = cur.fetchall()

            # DB에 반영
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            log.error(e)
