import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(distinct_salary) > 1:
        second_highest_salary = distinct_salary.iloc[1]
    else:
        second_highest_salary = None
    final = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
    return final

    