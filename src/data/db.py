from peewee import SqliteDatabase, PostgresqlDatabase
import os

if os.environ.get('POSTGRES_USER'):
    pg_db = PostgresqlDatabase(
        os.environ.get('POSTGRES_BASE'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('POSTGRES_HOST'),
        port=os.environ.get('POSTGRES_PORT'))
else:
    # SQLite database using WAL journal mode and 64MB cache.
    database = SqliteDatabase(
        database='../resources/bot_persistence.db',
        pragmas={
            'journal_mode': 'wal',
            'cache_size': -1024 * 64
        }
    )
