# python sampl.py
import os

fileDir = 'C:/Users/ChoiYouJin/Desktop/업무/8. 요일별/AP02'
fileList = os.listdir(fileDir)
tblList = {}
# file = open("C:/Users/KimYoungHun/Desktop/da/col_chk_log/mysql-bin.000706.sql_dml.log", "r")
for fileNm in fileList:
    file = open(fileDir + '/' + fileNm, "r")
    print("{} 오픈".format(fileNm))

while True:
    val = file.readline()
    print(val)
    if not val:
        break
    db = val[val.find(",") + 2:val.find(",", val.find(",") + 1)]
    table = val[val.find(",", val.find(",") + 1) + 1:val.find(",", val.find(",", val.find(",") + 1) + 1)]
    if not tblList.get(db):
        tblList[db] = {}
        if not tblList[db].get(table):
            tblList[db][table] = True
    elif not tblList[db].get(table):
        tblList[db][table] = True

#print(tblList)