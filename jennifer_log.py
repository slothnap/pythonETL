# python jennifer_log.py

import sql_filter


if __name__ == '__main__':
    # 파일 위치
    read_file  = "C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/jannifer_log.sql"   # jannifer_log ,test
    write_file = "C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/result.sql"
    sql_file   = "C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/sql_list.sql"


    # 제니퍼 로그 데이터 1차 가공
    #sql_filter.filter_sql(read_file, write_file)

    # 제니퍼 로그 데이터 2차 가공 및 DB 삽입
    sql_filter.manufacturing_sql(sql_file)


