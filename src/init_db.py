import sqlite3


daily_prices_schema = """
    CREATE TABLE daily_prices(
        price_date text,
        ticker text,
        open real,
        high real,
        low real,
        close real,
        price_source text
    );
"""

tickers_schema = """
    CREATE TABLE tickers(
        ticker text
    );
"""

pairs_schema = """
    CREATE TABLE pairs(
        ticker_a text,
        ticker_b text
    );
"""


def init_db():

    connection = sqlite3.connect(r"C:\Users\sbuca\Desktop\2025-projects\pricing\prices.db")
    cursor = connection.cursor()

    # prices close is already adjusted for cacs on yfinance api
    for schema in [daily_prices_schema, tickers_schema, pairs_schema]:

        try: 

            cursor.execute(daily_prices_schema)

        except Exception as e:

            print("*** BUILD ERROR: ", e, " ***")
