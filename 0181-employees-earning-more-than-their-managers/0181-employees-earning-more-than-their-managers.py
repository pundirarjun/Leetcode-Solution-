import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee,how = 'inner',left_on='managerId',right_on='id',suffixes=('_e','_m'))
    return df[df['salary_e'] > df['salary_m']][['name_e']].rename(columns = {'name_e':'Employee'})