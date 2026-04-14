import sqlalchemy as sq
import pandas as pd
import time
from Data.Setup import create_db
from config import Amazonengine
engine = sq.create_engine(Amazonengine)
def loadtosql() :
    try : 
        create_db()
        start_time = time.time()
        df = pd.read_csv('Data/Amazon Sales Report.csv')
        df.to_sql('Amazon_RawData' , index=False , con=engine , if_exists='replace' )
        print(f'Data Loaded Successfully.\nExecution Time : {round(time.time() - start_time , 2)}sec.')
    except Exception as e :
        print('Error Coming From DataLoadToSql : ' , e)