import mysql.connector
def write_date():
    print ('hello')
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="123123",database="test_for_board")
    mycu = mydb.cursor()
    temp_text = {'name':'Hello','text':'hello from test'}
    #sql = "insert into text (name,context) values (%s,%s)" % (temp_text['name'],temp_text['text'])
    sql = "insert into text (name,context) values (%s,%s)"
    val = (request.args.get('name'),request.args.get('text'))
    mycu.execute(sql,val)
    mydb.commit()
    print('done')
    mycu.close()
    mydb.close()
    return 0
write_date()
