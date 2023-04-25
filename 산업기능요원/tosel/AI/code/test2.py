import pymysql
conn = pymysql.connect(host='121.125.64.190',user='root',password='dlfha!@#', db="tosel",charset='utf8')
cur = conn.cursor()

#cur.execute("CREATE testtable_jay userTable(id char(4),userName char(15), email char(20),birthyear int)")

#유경태 김새아나
name = '김새아나'
receipt_no = ""


name_based_search_query = "SELECT receipt_no,exam_no FROM receipt2 where name = '최준혁';"
name_based_search_query = "SELECT receipt_no,exam_no FROM receipt2 where name = %s;"
receipt_data = cur.execute(name_based_search_query,('김새아나'))
result = cur.fetchall()
print(result)

# dat = "select exam_no from receipt_2 where exam_no>78"
# receipt_data = cur.execute(dat)
# result = cur.fetchall()
# print(result)



conn.commit()
conn.close()