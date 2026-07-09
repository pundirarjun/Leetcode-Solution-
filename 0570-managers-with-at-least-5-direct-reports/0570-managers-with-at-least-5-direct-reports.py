import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(by='managerId').size().reset_index(name='count')

    managers = managers[managers['count'] >= 5]

    result = employee[employee['id'].isin(managers['managerId'])]

    return result[['name']]