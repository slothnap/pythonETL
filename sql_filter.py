import insert_mdm
import datetime


# sql만 발라내기
def filter_sql(read_location, write_location):
    f_read = open(read_location, "rt", encoding='UTF8')

    print_on = 0
    list = []
    line_cnt = 0
    filter_result = ""

    # 측정 시작
    filter_sql_start_time = datetime.datetime.now()
    print("SQL 필터링 시작시간 :" + str(datetime.datetime.now()))

    while True:

        val = f_read.readline()
        line_cnt = line_cnt + 1
        if not val:
            break

        try:
            # 마지막줄 출력 off
            if "FETCH" in val:
                list.append(';\n')
                print_on = 0

            # SELECT ~ FETCH 중간 데이터 출력
            if print_on == 1:
                if "param1" in val:
                    # list.append(val.lstrip())
                    list.append(';\n')
                    print_on = 0
                else:
                    list.append(val)

            # 첫줄 출력 후 출력 on
            if "SELECT" in val:
                print_on = 1
                list.append(val.lstrip())

            filter_result = "제니퍼 로그파일 필터링 성공"
        except Exception as ex:
            print(ex)
            filter_result = "제니퍼 로그파일 필터링 실패"
            break

        # 1000건 마다 출력
        if line_cnt % 100000 == 0:
            print(line_cnt)

    f_read.close()


    # 쓰기 시작
    f_write = open(write_location, "w")
    for temp in list:
        f_write.write(temp)
    f_write.close()

    # 측정 종료
    filter_sql_end_time = datetime.datetime.now()
    print("SQL 필터링 종료시간 :" + str(datetime.datetime.now()))
    print("총 걸린 시간", filter_sql_end_time - filter_sql_start_time, "\n\n")


    print(filter_result)

# sql 집합 및 DB 넣기
def manufacturing_sql(read2_location):
    sql_list = []
    list_cnt = []
    i = 1

    # 측정 시작
    manufacturing_sql_start_time = datetime.datetime.now()
    print("SQL 그룹 지정 시작시간 :" + str(datetime.datetime.now()))

    f_read = open(read2_location, "rt", encoding='UTF8')

    while True:
        val = f_read.readline()
        if not val:
            break

        try:
            sql_list.append(str(val))
            list_cnt.append(str(i))

            if ';' in val:
                i = i + 1

        except Exception as ex:
            print(ex)
            break

    f_read.close()

    # 측정 종료
    manufacturing_sql_end_time = datetime.datetime.now()
    print("SQL 그룹 지정 종료시간 :" + str(datetime.datetime.now()))
    print("총 걸린 시간", manufacturing_sql_end_time - manufacturing_sql_start_time, "\n\n")

    # 측정 시작
    db_insert_start_time = datetime.datetime.now()
    print("DB 데이터 입력 시작시간 :" + str(datetime.datetime.now()))

    insert_mdm.insertdata(sql_list, list_cnt)

    # 측정 종료
    db_insert_end_time = datetime.datetime.now()
    print("DB 데이터 입력 종료시간 :" + str(datetime.datetime.now()))
    print("총 걸린 시간", db_insert_end_time - db_insert_start_time, "\n\n")
