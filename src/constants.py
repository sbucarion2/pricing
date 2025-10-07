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


SECURITIES = [
    ("QQQ", "equity"),
    ("TQQQ", "equity"),
    ("SQQQ", "equity"),
    ("SOXL", "equity"),
    ("CVX", "equity"),
    ("XOM", "equity"),
    ("NVDA", "equity"),
    ("AMD", "equity"),
    ("MS", "equity"), 
    ("GS", "equity"), 
    ("V", "equity"), 
    ("MA", "equity"), 
    ("UAL", "equity"), 
    ("DAL", "equity"), 
    ("WM", "equity"), 
    ("SG", "equity"),
]

PAIRS = [
    ("WM", "RSG"),
    ("UAL", "DAL"),
    ("V", "MA"),
    ("MS", "GS"),
    ("NVDA", "AMD"),
    ("CVX", "XOM"),
    ("QQQ", "TQQQ"),
    ("SQQQ", "TQQQ"),
]