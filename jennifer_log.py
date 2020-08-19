# python jennifer_log.py

import re

# f_read = open("C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/test.sql", "r")
# sql_list = f_read.read()
# f_read.close()

# START = "select"
# END   = "FETCH"
# m = re.compile(r'%s.*?%s' % (START,END), re.S)
# print(m.search(sql_list).group(0))


f_read = open("C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/test.sql", "r")

i = 0
print_on = 0
list = []

while True:
    val = f_read.readline()
    if not val:
        break

    # 마지막줄 출력 후 출력 off
    if val.find("FETCH") > 0:
        print_on = 0
        list.append(val)

    # SELECT ~ FETCH 중간 데이터 출력
    if print_on == 1:
        list.append(val)

    # 첫줄 출력 후 출력 on
    if val.find("SELECT") > 0:
        print_on = 1
        list.append(val)

#    i = i + 1
#    if i == 60:
#        break
f_read.close()

#for temp in list:
#    print(temp)

f_write = open("C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/result.sql", "w")
for temp in list:
    f_write.write(temp)

f_write.close()