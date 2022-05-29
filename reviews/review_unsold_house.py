import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM unsold_house")  # where 시군구='군산시'

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows


def main():
    database = r"C:/my_develop2/my_api/api_db.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        return select_all_tasks(conn)


if __name__ == '__main__':
    lst_result = main()
    df = pd.DataFrame(lst_result, columns=['id', '시군구', '구분', '미분양현황', 'date'])
    print(df.head())

    df.to_excel(r"C:/my_develop2/my_api/result_files/미분양1.xlsx")
