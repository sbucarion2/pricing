import sqlite3


daily_prices_schema = """
    CREATE TABLE daily_prices(
        price_date text,
        security text,
        open real,
        high real,
        low real,
        close real,
        price_source text
    );
"""

securities_schema = """
    CREATE TABLE securities(
        security text,
        asset_type text
    );
"""

pairs_schema = """
    CREATE TABLE pairs(
        security_a text,
        security_b text
    );
"""


def init_db():

    connection = sqlite3.connect(r"C:\Users\sbuca\Desktop\2025-projects\pricing\prices.db")
    cursor = connection.cursor()

    # prices close is already adjusted for cacs on yfinance api
    for schema in [daily_prices_schema, securities_schema, pairs_schema]:

        try: 

            cursor.execute(schema)

            print(schema, " created in db\n")

        except Exception as e:

            print("*** BUILD ERROR: ", e, " ***")


init_db()
