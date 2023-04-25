import pymysql
conn = pymysql.connect(host='121.125.64.190',user='root',password='dlfha!@#', db="tosel",charset='utf8')
cur = conn.cursor()

#cur.execute("CREATE testtable_jay userTable(id char(4),userName char(15), email char(20),birthyear int)")

#유경태 김새아나
name = '김새아나'
receipt_no = ""


name_based_search_query = "SELECT * FROM receipt2 where name = '최준혁';"
receipt_data = cur.execute(name_based_search_query)
result = cur.fetchall()

print(result)



data_search_query = "SELECT * FROM  exam_result_table where name = '유경태';"






conn.commit()
conn.close()