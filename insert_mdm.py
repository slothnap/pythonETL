import DbConfig as dbConf


# def insertdata(list):
#     # zero DB 연결
#     mdmDB = dbConf.DbConfig('mdm')
#     mdmDB.opendb()
#
#     for row in list:
#         insertSql = "insert into MDM.da_jannifer_log values(\"" + row + "\");"
#
#         try:
#             mdmDB.update(insertSql)
#             print(insertSql)
#         except Exception as ex:
#             print(ex)
#             break
#
#
# list = ["SELECT cf_ship,cf_order_url_type,cf_rb_type,cf_twodivi_cnt,cf_rolling_time from su_config", "SELECT COUNT(*) AS count ", ""]
#
# insertdata(list)


mdmDB = dbConf.DbConfig('mdm')
mdmDB.opendb()

#print(mdmDB.db_config)
sql = "insert into MDM.da_jannifer_log values(\"SELECT cf_ship,cf_order_url_type,cf_rb_type,cf_twodivi_cnt,cf_rolling_time from su_config\");"
print(sql)
mdmDB.update(sql)

mdmDB.closedb()