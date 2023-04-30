import pymysql
import class_Student

class DB_search:
    conn = pymysql.connect(host='121.125.64.181',user='root',password='tosel!@#', db="jtosel",charset='utf8')
    cur = conn.cursor()

    st = class_Student.Student()

    def __init__(self):
        pass
    
    def get_receiptNo_by_mobile(self, mobile, exam_date):#이름 : 작은따옴표
        base_query = "SELECT receipt_no FROM receipt where mobile = %s and exam_date = %s"
        self.cur.execute(base_query,(mobile,exam_date))
        result = self.cur.fetchall()
        print(result)
        return result

    def get_data_by_mobile(self, mobile,exam_date):
        num = self.get_receiptNo_by_mobile(mobile,exam_date)
        base_query = "select * from exam_result_table where receipt_no=%s"
        self.cur.execute(base_query, num)
        result = self.cur.fetchall()
        return result

    def __del__(self):        
        self.conn.commit()
        self.conn.close()



db = DB_search()

print(db.get_data_by_mobile('010-3841-8268', '2018-05-19'))



