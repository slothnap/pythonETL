# python insert_mdm.py

import DbConfig as dbConf

def insertdata(sql_list, list_cnt):

    # zero DB 연결
    mdmDB = dbConf.DbConfig('mdm')
    mdmDB.opendb()

    # 로그 데이터 넣기
    for i in range(len(sql_list)):
        insertSql = "insert into MDM.da_jannifer_log values(\"" + sql_list[i] + "\",\"" + list_cnt[i] + "\");"

        # 1000건 마다 출력
        if int(list_cnt[i]) % 100 == 0:
            print(list_cnt[i])

        try:
            mdmDB.update(insertSql)
            #print(insertSql)
        except Exception as ex:
            print(ex)
            mdmDB.rollback()
            break

    mdmDB.commit()

    # SQL 2차 가공
    # jannifer_sql = """
    #                insert into da_jannifer_sql
    #                select group_no
    #                     , group_concat(instr_sql separator ' ') as sql_list
    #                  from da_jannifer_log
    #                 group by group_no
    #                """
    # try:
    #     mdmDB.update(jannifer_sql)
    #
    # except Exception as ex:
    #     print(ex)
    #     mdmDB.rollback()

    mdmDB.commit()
    mdmDB.closedb()

