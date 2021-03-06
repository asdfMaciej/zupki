import sqlite3 as sql3
import re
from pprint import pprint


def sanitize(_str): return re.sub('[^a-zA-Z0-9ążźćłęĘńóśĄŻŹĆŁŃÓŚ\/\- \n\.-]', '', _str)

def cCol(my_hex):
    r, g, b = tuple(int(my_hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    a = 1 - float((0.299 * r + 0.587 * g + 0.114 * b) / 255);
    return '#212121' if a < 0.5 else '#FAFAFA'
    #return '#'+''.join(comp)

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
    for it in range(10):
        for key, value in retdict.items():
            retdict[key][it] = []

    for lsn in tple:
        dzn = ar_to_dzn(lsn)
        prd = int(lsn[8])
        retdict[dzn][prd].append(lsn)

    empty = not tple
    pprint(tple)
    return retdict, empty

def actually_screw_django(dck):
    dct, empty = dck
    dictstoocomplicated = []
    n = 0
    for key, value in dct.items():
        dictstoocomplicated.append([key])
        for key, val in value.items():
            str_val = ""
            if val:
                use_table = len(val) > 1
                #if use_table:
                str_val = '<table class="in" bgcolor="'+val[0][12]+'"style="width: 100%;display: block;color:'+cCol(val[0][12])+';">'
                for value in val:
                    #if use_table:
                    str_val += '<tr class="in"><td class="in">'
                    str_val += '<i>'+value[0]+'<br/>'+value[1]+'<br/></i><b>'+value[11]+'</b><br/>'+value[2]+'<br/>'
                    #if use_table:
                    str_val += '</td></tr>'
                #if use_table:
                str_val += '</table>'
            dictstoocomplicated[n].append(str_val)
        n += 1
    return dictstoocomplicated, empty

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
                'SELECT class, classroom, teacher, d_monday, d_tuesday, d_thursday, d_wednesday, d_friday, period,' +  # im mentally retarded
                'period_end, period_start, subject, subject_color from jednostki_lekcyjne WHERE ' +
                sanitize(parameter) + '="' + sanitize(_str) + '";'
            )
        )
    )

def get_column_names():
    return list(zip(*get_query('PRAGMA table_info(jednostki_lekcyjne);')))[1]

def get_teachers():
    return list(sorted(list(get_query('SELECT DISTINCT teacher_id, teacher from jednostki_lekcyjne;')), key=lambda x: x[1]))
def get_classes():
    return list(sorted(list(get_query('SELECT DISTINCT class_teacher, class from jednostki_lekcyjne;')), key=lambda x: x[1]))
def get_classrooms():
    przed = list(sorted(list(get_query('SELECT DISTINCT classroom from jednostki_lekcyjne;')), key=lambda x: x[0]))
    po = []
    for t in przed: po.append(('', t[0]))
    return po
