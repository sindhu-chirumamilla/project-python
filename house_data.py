import pandas as pd

def isfloat(x):
    try :
        float(x)
    except :
        return False
    return True

def convert_sqft_to_float(x):
    tokens = x.split('-')
    if len(tokens) == 2 :
        return (float(tokens[0])+float(tokens[1]))/2
    try :
        return float(x)
    except :
        return None

df1 = pd.read_csv("C:\\Users\\sindhu\\Downloads\\datasets_20710_26737_Bengaluru_House_Data.csv")
df2 = df1.drop(['area_type','society','balcony','availability'],axis='columns')
df3 = df2.dropna()
df3['bhk']= df3['size'].apply(lambda x : int(x.split(' ')[0]))
df3[~df3['total_sqft'].apply(isfloat)].head(10)
df4 = df3.copy()
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_float)
df5 = df4.copy()
df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']
df5.to_csv(
            "C:\\Users\\sindhu\\Downloads\\output_bangalore_real_estate.csv",
            index=False,
            header=True
        )



