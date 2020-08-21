# python jennifer_log.py

import sql_filter
import insert_mdm

# 파일 위치
read_file  = "C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/test.sql"
write_file = "C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/result.sql"

# 출력 받은 배열
list = sql_filter.filter_sql(read_file)


# DB에 넣기
# insert_mdm.insertdata(list)


# 결과 보기
f_write = open(write_file, "w")
for temp in list:
    f_write.write(temp)

f_write.close()



