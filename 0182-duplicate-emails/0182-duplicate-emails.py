import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df=person['email']
    df1=df[df.duplicated()]
    df2=pd.DataFrame(df1)
    return df2.drop_duplicates()