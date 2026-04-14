import pandas as pd

def transform(df) :
    try : 

        df = df.drop_duplicates()
        df['actual_price'] = pd.to_numeric(df['actual_price'].str.replace(r'[₹,?]', '', regex=True), errors='coerce')
        df['discounted_price'] = pd.to_numeric(df['discounted_price'].str.replace(r'[₹,?]', '', regex=True), errors='coerce')
        df['discount_percentage'] = pd.to_numeric(df['discount_percentage'].str.replace('[%]', '', regex=True) , errors='coerce')
        df['rating_count'] = pd.to_numeric(df['rating_count'].str.replace(',', '') , errors='coerce')
        df['Total_Paid_Bill'] = df['actual_price'] - df['discounted_price']
        df['Discount_Level'] = 'Low'
        df.loc[((df['discount_percentage'] >=  40) & (df['discount_percentage'] <= 70)  ) , 'Discount_Level'] = 'Medium'
        df.loc[(df['discount_percentage'] >  70) , 'Discount_Level'] = 'High'
        df['category'] = df['category'].str.split('|').str[0]
        df['rating'] = pd.to_numeric(df['rating'] , errors='coerce')
        df['Rating_Level'] = 'Low'
        df.loc[((df['rating'] >= 2) & (df['rating'] < 4)) , 'Rating_Level'] = 'Medium'
        df.loc[(df['rating'] >= 4) , 'Rating_Level'] = 'High'
        
 
        df = df.fillna(0)
        return df
    except Exception as e : 
        print('Error Coming From Transformation : ' , e)
        return e
   
    
    

    