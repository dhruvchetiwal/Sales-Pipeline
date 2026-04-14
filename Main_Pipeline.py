from Data.DataLoadToSql import loadtosql
from src.Extract import extract
from src.Transform import transform
from src.load import load
from Data.DataLoadToSql import engine


def pipeline() :
    try : 
        print('Pipeline Started.....')
        loadtosql()
        df = extract(engine)
        print(f'Extracted {len(df)} rows.')

        clean_df = transform(df)
        print('Data Cleaned!')

        load(clean_df , engine) 
        print('Data Loaded Successfully......')
        print("Pipleline Successfully Executed...")
    except Exception as e :
       raise Exception('Error Coming From Pipeline :' , e)


if __name__ == '__main__' :
    pipeline()