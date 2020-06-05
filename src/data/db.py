from peewee import SqliteDatabase, PostgresqlDatabase
import os

if os.environ.get('DATABASE_URL'):
    pg_db = PostgresqlDatabase(
        os.environ.get('DATABASE_URL'),
        sslmode='require')
else:
    # SQLite database using WAL journal mode and 64MB cache.
    database = SqliteDatabase(
        database='../resources/bot_persistence.db',
        pragmas={
            'journal_mode': 'wal',
            'cache_size': -1024 * 64
        }
    )
