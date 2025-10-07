import sqlite3
import yfinance as yf
from datetime import date, datetime, timedelta


def get_db_securities(cursor):

    cursor.execute(
        """SELECT * FROM securities"""
    )

    securities = cursor.fetchall()

    return securities


def get_last_price_date(cursor):

    cursor.execute(
        """
        SELECT MAX(price_date) 
        FROM daily_prices
        GROUP BY security
        """
    )

    return cursor.fetchall()


def format_price_data(security, security_pricing):
    """Formats yfinance data response to sqlite db schema"""

    format_price = lambda price: float(round(price, 3))

    prices = []
    for date, row in security_pricing.iterrows():

        prices.append(
            (                
                str(date).split()[0],
                security,
                format_price(row["Open"]),
                format_price(row["High"]),
                format_price(row["Low"]),
                format_price(row["Close"]),
                "yfinance",
            )
        )


    return prices


def get_pricing(security, start_date=None, end_date=None):

    ticker_object = yf.Ticker(security)

    # Request entire security history
    if start_date is None and end_date is None:

        security_pricing = ticker_object.history(
            start="1900-01-01",
            interval="1d"
        )

    # security_pricing = ticker_object.history(
    #     start="2025-09-12",
    #     end="2025-09-16", 
    #     interval="1d"
    # )

    security_pricing = format_price_data(security, security_pricing)

    return security_pricing


def load_prices_to_db(connection, cursor, security_pricing):

    query = """
        INSERT INTO daily_prices (price_date, security, open, high, low, close, price_source)
        VALUES(?, ?, ?, ?, ?, ?, ?)
    """

    cursor.executemany(query, security_pricing)
    connection.commit()


def load_prices():

    connection = sqlite3.connect(r"C:\Users\sbuca\Desktop\2025-projects\pricing\prices.db")
    cursor = connection.cursor()

    securities = get_db_securities(cursor)

    securities_last_price_date = get_last_price_date(cursor)

    for security, security_type in securities:

        if security_type != "equity":

            continue

        ### MAYBE instead of conditional we just define the entry point date and pass thru idk

        # Full price import
        if security not in securities_last_price_date:

            security_pricing = get_pricing(security)

        # Only import new pricing
        else:

            # Get pricing starting with last price date + 1

            pass

        print(security_pricing)

        load_prices_to_db(connection, cursor, security_pricing)

        break



    cursor.close()
    connection.close()


# load_prices()