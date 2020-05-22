from peewee import SqliteDatabase

# SQLite database using WAL journal mode and 64MB cache.
database = SqliteDatabase(
    database='../resources/bot_persistence.db',
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64
    }
)
