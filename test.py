import mysql.connector
def write_date():
    print ('hello')
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
    mycu = mydb.cursor()
    sql = "insert into text (name,context) values (%s,%s)"
    val = ('tankie','Hello,your guy!')
    mycu.execute(sql,val)
    mydb.commit()
    print('done')
    mycu.close()
    mydb.close()
    return 0
write_date()
