import pandas as pd

def load(df, engine) :
    try :
        df.to_sql('Amazon_CleanData' 
                , con=engine ,
                index=False ,
                if_exists='replace')
    except Exception as e :
        print('Error Coming From Load : ' , e)