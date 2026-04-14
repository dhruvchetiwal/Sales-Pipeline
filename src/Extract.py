import sqlalchemy as sq
import pandas as pd

def extract(engine) :
        try :
                df = pd.read_sql('SELECT * FROM Amazon_RawData' , engine)
                return df
        except Exception as e :
                raise('Error Comes From Extraction : ' , e)

