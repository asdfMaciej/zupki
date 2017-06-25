import sqlite3 as sql3
import re

def sanitize(_str): return re.sub('[^a-zA-Z0-9ążźćłńóśĄŻŹĆŁŃÓŚ \n\.]', '', _str)

def get_query(query):
    conn = sql3.connect('baza.db')
    cur = conn.cursor()
    cur.execute(query)
    print(query)
    return list(cur.fetchall())

def get_all(parameter, _str):
    return get_query('SELECT * from jednostki_lekcyjne WHERE '+sanitize(parameter)+'="'+sanitize(_str)+'";')

def get_essential(parameter, _str):
    return get_query('SELECT class, classroom, teacher, d_monday, d_tuesday, d_wednesday, d_thursday, d_friday, period, period_end, period_start, subject from jednostki_lekcyjne WHERE ' + sanitize(parameter) + '="' + sanitize(_str) + '";')

def get_column_names():
    return list(zip(*get_query('PRAGMA table_info(jednostki_lekcyjne);')))[1]

def get_teachers():
    return get_query('SELECT DISTINCT teacher_id, teacher from jednostki_lekcyjne;')