import sqlite3 as sql3
import re

def sanitize(_str): return re.sub('[^a-zA-Z0-9ążźćłńóśĄŻŹĆŁŃÓŚ \n\.]', '', _str)


def essential_to_dict(tple):
    def ar_to_dzn(ar):
        dzn = ''
        dzn = 'Poniedziałek' if ar[3] else dzn
        dzn = 'Wtorek' if ar[4] else dzn
        dzn = 'Środa' if ar[5] else dzn
        dzn = 'Czwartek' if ar[6] else dzn
        dzn = 'Piątek' if ar[7] else dzn
        return dzn

    retdict = {'Poniedziałek': {}, 'Wtorek': {}, 'Środa': {}, 'Czwartek': {}, 'Piątek': {}}
    for it in range(9):
        for key, value in retdict.items():
            retdict[key][it] = []

    for lsn in tple:
        dzn = ar_to_dzn(lsn)
        prd = int(lsn[8])
        retdict[dzn][prd] = lsn

    return retdict

def actually_screw_django(dct):
    dictstoocomplicated = []
    n = 0
    for key, value in dct.items():
        dictstoocomplicated.append([key])
        for key, value in value.items():
            str_val = ""
            if value:
                str_val = '<i>'+value[0]+'<br/>'+value[1]+'<br/></i><b>'+value[11]+'</b><br/>'+value[2]+'<br/>'
            dictstoocomplicated[n].append(str_val)
        n += 1
    return dictstoocomplicated

def get_query(query):
    conn = sql3.connect('baza.db')
    cur = conn.cursor()
    cur.execute(query)
    print(query)
    return list(cur.fetchall())

def get_all(parameter, _str):
    return get_query('SELECT * from jednostki_lekcyjne WHERE '+sanitize(parameter)+'="'+sanitize(_str)+'";')

def get_essential(parameter, _str):
    return actually_screw_django(
        essential_to_dict(
            get_query(
                'SELECT class, classroom, teacher, d_monday, d_tuesday, d_wednesday, d_thursday, d_friday, period,' +
                'period_end, period_start, subject from jednostki_lekcyjne WHERE ' +
                sanitize(parameter) + '="' + sanitize(_str) + '";'
            )
        )
    )

def get_column_names():
    return list(zip(*get_query('PRAGMA table_info(jednostki_lekcyjne);')))[1]

def get_teachers():
    return get_query('SELECT DISTINCT teacher_id, teacher from jednostki_lekcyjne;')
def get_classes():
    return get_query('SELECT DISTINCT class, class_teacher from jednostki_lekcyjne;')
