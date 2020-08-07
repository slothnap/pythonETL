import DbConfig as dbConf


def getdata(arr):
    # zero DB 연결
    zeroDb = dbConf.DbConfig()
    zeroDb.opendb()
    for job in arr:
        dbinfo = {'host': job['host']
                , 'user': job['user']
                , 'password': job['password']
                , 'db': job['db']}
        dynamicdb = dbConf.DbConfig(dbinfo)
        dynamicdb.opendb()

        # 진행중인 작업 상태 변경
        statusSql = """update dw_tab_list
                        set first_clct_dtm = now()
                        , eai_stus_nm = "진행중"
                        where tab_sno = """ + str(job['tab_sno']) + ";"
        zeroDb.update(statusSql)

        sql = str(job['clct_sql'])

        # if job['finl_clct_dtm'] is None:  # 초기 적재
        page = 0
        limit = 10000
        bulk_unit = 5000
        exit_mode = 'page'

        while True:
            if job['befr_sql'] is not None:
                orStr = ''
                if job['finl_clct_dtm'] is None:  # 초기 적재
                    orStr = 'or 1=1'
                sql2 = sql.replace('[initial]', orStr + ' order by ' + str(job['pk_col_nm']) + ' LIMIT ' + str(limit))
            else:
                orStr = ''
                if job['finl_clct_dtm'] is None:  # 초기 적재
                    orStr = 'or 1=1'
                sql2 = sql.replace('[initial]', orStr + ' order by ' + str(job['pk_col_nm']) + ' LIMIT ' + str(page) + ', ' + str(limit))

            data = dynamicdb.select(sql2)

            val_group_cnt = 0
            val_group = ''

            # 데이터 이행 시작
            for rows in data:
                val_list = ''
                for key, value in dict(rows).items():
                    val_list += ",'" + str(value).replace("'", "\"").replace('"', '\"').replace("\\", "\\\\") + "'"

                val_list = val_list[1:]
                val_group += ", (" + val_list + ")"
                val_group_cnt += 1

                # 데이터 이행1 시작
                # 1 ~ 50000번까지 차면 데이터 삽입
                if val_group_cnt == bulk_unit:
                    val_group = val_group[1:]

                    # 최초/수정에 따라서 insert/replace 로 바뀐다
                    updateType = 'insert'
                    if job['finl_clct_dtm'] is not None:
                        updateType = 'replace'
                    insertSql = updateType + " into " + job['trgt_tab_nm'] + " values " + val_group
                    insertSql = insertSql.replace("None", "null")

                    try:
                        zeroDb.update(insertSql)
                    except Exception as ex:
                        print(ex)
                        break
                    val_group_cnt = 0
                    val_group = ''
                # 데이터 이행1 끝
            # End of "for rows in data"

            # 데이터 이행2
            if val_group is not None and val_group != '':
                val_group = val_group[1:]

                # 최초/수정에 따라서 insert/replace 로 바뀐다
                updateType = 'insert'
                if job['finl_clct_dtm'] is not None:
                    updateType = 'replace'
                insertSql = updateType + " into " + job['trgt_tab_nm'] + " values " + val_group
                insertSql = insertSql.replace("'None'", "null")

                try:
                    zeroDb.update(insertSql)
                except Exception as ex:
                    print(ex)
                    break
            # 데이터 이행2 끝

            # 후행SQL 존재 할 경우
            if job['aftr_sql'] is not None:
                try:
                    zeroDb.update(job['aftr_sql'])
                except Exception as ex:
                    print(ex)
                    updateSql = "update dw_tab_list " \
                                "set eai_stus_nm = '업데이트 오류' " \
                                "where tab_sno = " + str(job['tab_sno'])
                    zeroDb.update(updateSql)
                    break

            if (exit_mode == 'page' and len(data) < page) or (exit_mode == 'limit' and len(data) < limit):
                break
            page += limit
            # End of "while True:"

        updateSql = """update   dw_tab_list\n"""\
                    """set      finl_clct_dtm = now()\n"""\
                    """         , eai_stus_nm = '변경완료'\n"""\
                    """where    tab_sno = """ + str(job['tab_sno']) + ";"
        zeroDb.update(updateSql)
        dynamicdb.closedb()
        print("병렬 작업완료")

    zeroDb.closedb()
