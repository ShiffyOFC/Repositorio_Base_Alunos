import sqlite3

try:
    con=sqlite3.connect('hospital.db')
    cur=con.cursor()

    cur.executescript("DELETE FROM medico WHERE id>11 and id<23")

    cur.close()
    con.close()
except ConnectionRefusedError as e:
    print('Erro de conexão: ', e)