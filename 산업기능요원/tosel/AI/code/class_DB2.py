import pymysql
import class_Student

class DB_search:
    conn = pymysql.connect(host='121.125.64.190',user='root',password='dlfha!@#', db="tosel",charset='utf8')
    cur = conn.cursor()

    st = class_Student.Student()

    def __init__(self):
        pass
    
    def get_receiptNo_by_name(self, name, exam_no):#이름 : 작은따옴표
        base_query = "SELECT receipt_no, exam_no FROM receipt_2 where name = %s and exam_no = %s;"
        self.cur.execute(base_query,(name,exam_no))
        result = self.cur.fetchall()
        return result

    def get_data_by_name(self, name):
        num = self.get_receiptNo_by_name(name)
        base_query = "select * from exam_result_table where receipt_no=%s"
        self.cur.execute(base_query, num)
        result = self.cur.fetchall()
        return result

    def __del__(self):        
        self.conn.commit()
        self.conn.close()



db = DB_search()

print(db.get_receiptNo_by_name('홍길순','44'))
#print(db.get_data_by_name('최준혁', '44'))
