import sys,time
sys.path.append('../db_fixture')
from db.mysql_db import DB




# Inster table datas
def ua_emp_insert(count):
    table = 'ua_employee'
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    try:


        if  count==1:
            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.close()

        elif  count==2:

            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
               'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}



            emp2 = {'EMP_NO':'99992','EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
           'EMP_STATUS': '1', 'CELL_PHONE': '1010123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()

        elif count == 9:
            table_name = table
            emp = {'EMP_NO': '99991', 'EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2',
                   'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                   'EMP_STATUS': '0', 'CELL_PHONE': '9898123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            emp2 = {'EMP_NO': '99992', 'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1',
                    'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                    'EMP_STATUS': '1', 'CELL_PHONE': '1010123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()
    except Exception as err:
        return  err
    finally:
        return "good"

def ua_emp_search(value,type):
    semp = {'EMP_CNAME': '测试账号α'}
    semp2 = {'EMP_CNAME': '测试账号β'}
    table_name = "ua_employee"


    if   type=='α':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp)
        db.close()
    elif type == 'β':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp2)
        db.close()
    return s

def ua_emp_delete(type,id):
    table_name = "ua_employee"
    table_name2 = "ua_online_employee"
    table_name3 ="ua_logon_log"
    table_name4 = 'ua_operation_log'
    data = {'EMP_CNAME': '测试账号α'}
    data2 = {'EMP_CNAME': '测试账号β'}
    data_id = {'EMP_ID': id}
    data_id2 = {'EMP_ID': id}
    data_id3 = {'EMP_ID': id}

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name4, table_data=data_id3)
        db.clear(table_name=table_name2, table_data=data_id)
        db.clear(table_name=table_name3, table_data=data_id2)
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name4, table_data=data_id3)
        db.clear(table_name=table_name2, table_data=data_id)
        db.clear(table_name=table_name3, table_data=data_id2)
        db.clear(table_name=table_name, table_data=data2)
        db.close()




if __name__ == '__main__':
    dtb_clause_inser(count=1)
    s=dtb_clause_search(value='NAME',type='α')


    print(s)