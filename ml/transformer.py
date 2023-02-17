from pandas import DataFrame


def transform_df(df:DataFrame):
    df.drop(['client_id', 'living_region'], axis=1, inplace=True)
    
    for column in ['credit_sum', 'score_shk']:
        df[column] = df[column].apply(lambda x: x.replace(',', '.')).astype('float')
        
    df['gender'] = df['gender'].map({"F": 1, "M": 0})
    df.rename(columns={'gender':'female'}, inplace=True)