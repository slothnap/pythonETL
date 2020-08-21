# python insert_mdm.py

import DbConfig as dbConf

def insertdata(list):
    # zero DB 연결
    mdmDB = dbConf.DbConfig('mdm')
    mdmDB.opendb()

    for row in list:
        insertSql = "insert into MDM.da_jannifer_log values(\"" + row + "\");"

        #print(insertSql)

        try:
            mdmDB.update(insertSql)
            mdmDB.commit()
        except Exception as ex:
            print(ex)
            break

    mdmDB.closedb()


