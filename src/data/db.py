from peewee import SqliteDatabase, PostgresqlDatabase, Proxy
import os
database = Proxy()

if os.environ.get('DATABASE_URL'):
    import urllib.parse as urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    database.initialize(db)
else:
    # SQLite database using WAL journal mode and 64MB cache.
    db = SqliteDatabase(
        database='resources/bot_persistence.db',
        pragmas={
            'journal_mode': 'wal',
            'cache_size': -1024 * 64
        }
    )
    database.initialize(db)
