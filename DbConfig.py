# pip3 install -r requirements.txt
import pymysql


class DbConfig:
    db_config = {}
    db = None
    cursor = None

    def __init__(self, db_info=None):
        if str(type(db_info)) == "<class 'str'>":
            sysNm = str(db_info)
            if sysNm == 'app':
                self.db_config = {
                    'host': '10.20.10.61'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'torder'
                }
            elif sysNm == 'jasonb':
                self.db_config = {
                    'host': '10.20.10.81'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonb'
                }
            elif sysNm == 'jasonb_dev':
                self.db_config = {
                    'host': '192.168.0.101'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonb'
                }
            elif sysNm == 'treport':
                self.db_config = {
                    'host': '10.20.10.122'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'treport'
                }
            elif sysNm == 'treport_dev':
                self.db_config = {
                    'host': '192.168.0.113'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'treport'
                }
            elif sysNm == 'po':
                self.db_config = {
                    'host': '10.20.10.94'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasond'
                }
            elif sysNm == 'mdm':
                self.db_config = {
                    'host': '10.20.10.45'
                    , 'user': 'MDM_Admin'
                    , 'password': 'wpdltms123!@#'
                    , 'db': 'MDM'
                }
            elif sysNm == 'sale_live':
                self.db_config = {
                    'host': '10.20.10.61'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp014'
                }
            elif sysNm == 'sale_dev':
                self.db_config = {
                    'host': '192.168.0.101'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp014'
                }
            elif sysNm == 'sim_live':
                self.db_config = {
                    'host': '10.20.10.61'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp018'
                }
            elif sysNm == 'sim_dev':
                self.db_config = {
                    'host': '192.168.0.101'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp018'
                }
            elif sysNm == 'market_live':
                self.db_config = {
                    'host': '10.20.10.61'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp019'
                }
            elif sysNm == 'market_dev':
                self.db_config = {
                    'host': '192.168.0.101'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp019'
                }
            elif sysNm == 'torder_live':
                self.db_config = {
                    'host': '10.20.10.61'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'torder'
                }
            elif sysNm == 'torder_dev':
                self.db_config = {
                    'host': '192.168.0.101'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'torder'
                }
            elif sysNm == 'app_data_export':
                self.db_config = {
                    'host': '10.20.10.91'
                    , 'user': 'jason_da'
                    , 'password': 'da@0417'
                    , 'db': 'jasonapp018'
                }
            elif sysNm == 'zero':
                self.db_config = {
                    'host': "zerosum.cqjm9uq4vsof.ap-northeast-2.rds.amazonaws.com"
                    , 'user': 'zero'
                    , 'password': 'rladudgns!1'
                    , 'db': 'sql_test'
                }
            else:  # 로컬에서 테스트 진행 시
                self.db_config = {
                    'host': "10.20.10.45"
                    , 'user': 'MDM_Admin'
                    , 'password': 'wpdltms123!@#'
                    , 'db': 'MDM'
                }
        elif str(type(db_info)) == "<class 'dict'>":
            print(type(db_info))

    def opendb(self):
        self.db = pymysql.connect(**self.db_config)
        self.db.set_charset('utf8mb4')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def closedb(self):
        self.db.close()

    def select(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def update(self, sql):
        return self.cursor.execute(sql)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
