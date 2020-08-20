

# sql만 발라내기
def filter_sql(file_location):
    f_read = open(file_location, "rt", encoding='UTF8')
    print_on = 0
    list = []

    while True:
        val = f_read.readline()
        if not val:
            break

        # 마지막줄 출력 off
        if val.find("FETCH") > 0:
            print_on = 0


        # SELECT ~ FETCH 중간 데이터 출력
        if print_on == 1:
            if val.find("param1") > 0:
                #list.append(val.lstrip())
                list.append('')
                print_on = 0
            else:
                list.append(val)


        # 첫줄 출력 후 출력 on
        if val.find("SELECT") > 0:
            print_on = 1
            list.append(val.lstrip())

    f_read.close()
    return list