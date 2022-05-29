from ntpath import join
import sqlite3
from sqlite3 import Error
import pandas as pd
from typing import List


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
    cur.execute("SELECT * FROM statement")

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows


def get_col_names(file_name: str, table_name: str) -> List[str]:
    conn = sqlite3.connect(file_name)
    col_data = conn.execute(f'PRAGMA table_info({table_name});').fetchall()
    return [entry[1] for entry in col_data]


def get_comp_code():
    comp_code = pd.read_excel("../result_files/회사고유번호.xlsx")
    comp_code["corp_code"] = comp_code["고유번호"].apply(lambda x: str(x).zfill(8))
    return comp_code


def main():
    database = r"C:/my_develop2/my_api/api_db.db"
    table_name = "statement"

    col_names = get_col_names(database, table_name)

    # create a database connection
    conn = create_connection(database)
    with conn:
        return col_names, select_all_tasks(conn)


if __name__ == '__main__':
    db_data = main()    # 전체 데이터
    col_names = db_data[0]   # 칼럼명
    data = db_data[1]    # 칼럼명 제외 데이터
    # 고유번호, 회사이름 데이터프레임으로 재정리
    df_corp_code = get_comp_code()[["corp_code", "회사이름", "종목코드"]]
    df = pd.DataFrame(data, columns=col_names)

    # print(db_data[0])
    # print(df_corp_code.head())
    # print(df.head())

    joined_df = pd.merge(df, df_corp_code, left_on='corp_code', right_on='corp_code', how="left")   # 한글회사명 조인으로 붙이기
    print(joined_df.head())
    print(joined_df["회사이름"].unique())


    # joined_df.to_excel(r"C:/my_develop2/my_api/result_files/재무재표.xlsx", index=False)
