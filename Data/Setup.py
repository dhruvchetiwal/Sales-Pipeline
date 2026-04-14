import sqlalchemy as sq 
from config import masterengine

engine_setup = sq.create_engine(masterengine)
def create_db() :
    with engine_setup.connect().execution_options(isolation_level='AUTOCOMMIT') as connection :
        connection.execute(sq.text("""
    IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'AmazonData')
    BEGIN
        CREATE DATABASE AmazonData
    END
    """))


    print('DataBase Work Done Successfully......')


