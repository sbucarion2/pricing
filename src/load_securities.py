import sqlite3

from constants import SECURITIES, PAIRS


def get_securities(cursor):

    cursor.execute(
        """SELECT * FROM securities"""
    )

    securities = cursor.fetchall()

    return securities



def load_tickers():

    connection = sqlite3.connect(r"C:\Users\sbuca\Desktop\2025-projects\pricing\prices.db")
    cursor = connection.cursor()

    current_securities = get_securities(cursor)

    print(current_securities)

    for security, security_type in SECURITIES:

        if (security, security_type) in current_securities:

            print("Skipping: ", security, security_type)

            continue

        query = """
            INSERT INTO securities (security, asset_type)
            VALUES(?, ?)
        """

        print(security, security_type)

        cursor.execute(query, (security, security_type))
        connection.commit()

    cursor.close()
    connection.close()

    return


def load_pairs():

    return


def main():

    load_tickers()

main()
