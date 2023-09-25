from sqlite3 import connect

def select_database(sql,li=""):
    conn = connect("database.db")
    pointer = conn.cursor()
    if not li:
        pointer.execute(sql)
        list_array = pointer.fetchall()
    else:
        pointer.execute(sql,li)
        list_array = pointer.fetchall()
    conn.commit()
    conn.close()
    return list_array

def execute_database(sql,dic=""):
    conn = connect("database.db")
    pointer = conn.cursor()
    if not dic:
        pointer.execute(sql)
    else:
        pointer.execute(sql,dic)
    conn.commit()
    conn.close()
