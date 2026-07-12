import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # employee['rank'] = employee['salary'].rank(method = 'dense',ascending = False)
    # nthhighest = employee[employee['rank'] == N]
    # return pd.DataFrame({f"getNthHighestSalary({N})":[None if len(nthhighest) == 0 else nthhighest['salary'].iloc[0]]})
    unique_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)

    if N <=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    if N > len(unique_salary):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    nthsalary = unique_salary.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nthsalary]})