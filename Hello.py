import DbConfig as dbConf
import multiprocessing as mp
import math
import dw_collect_data as getData


if __name__ == '__main__':
    # MDM DB 연결
    zeroDb = dbConf.DbConfig("zero")
    zeroDb.opendb()
    print("접속완료")

    # cast(aes_decrypt(unhex(db.user_pwd), 'jasonmdm' ) as char) as password\n"
    sql = ("""SELECT	db.extn_db_sno
           		, db.srvr_ip_adrs as host
                   , db.srvr_nm as db
                   , db.user_nm as user
           		, db.user_pwd as password
           		, tab.trgt_tab_nm
           		, replace(clct_sql, '[interval]',  case clct_cond_col_nm  when 'clct_perd_mins' then clct_perd_mins 
           				                                                  when 'clct_pk_val'    then clct_pk_val
           				                                                  else ''
           		                                                           end) clct_sql
           		, befr_sql
           		, aftr_sql
           		, finl_clct_dtm, tab.tab_sno, tab.pk_col_nm, tab.eai_stus_nm
           FROM	extn_db db, dw_tab_list tab
           WHERE	db.extn_db_sno = tab.sorc_db_sno
           AND		tab.clct_yn = 'Y'"""
           )

    # 수집 대상 DB정보 및 테이블, 쿼리 조회
    print(sql)
    source = zeroDb.select(sql)
    print(source)

    # 병렬처리 진행 전처리
    num_cores = mp.cpu_count()  # cpu의 코어 수를 반환

    # 조회 대상 테이블을 cpu 코어수 만큼 분할
    unit_num = math.ceil(len(source) / num_cores)
    # multiArr = [source[i * unit_num:(i + 1) * unit_num] for i in range((len(source) + unit_num - 1) // unit_num)]

    procs = []
    for i in range(num_cores):
        if i == len(source):
            break
        # print(source[i * unit_num: (i + 1) * unit_num])
        proc = mp.Process(target=getData.getdata, args=(source[i * unit_num: (i + 1) * unit_num],))
        procs.append(proc)
        proc.start()

    # 조회 대상 항목들에 대하여 상태값 변경
    sql = """update dw_tab_list
               set eai_stus_nm = "전송 대기중"
             where clct_yn = 'Y'"""
    zeroDb.update(sql)
    zeroDb.closedb()
    for proc in procs:
        proc.join()

    #print('전체 작업 완료')
