import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    joined_df=employee.merge(department,left_on=employee['departmentId'],right_on=department['id'],how='inner')
    joined_df['rank']=joined_df.groupby('departmentId')['salary'].rank(method='dense',ascending=False)
    joined_df=joined_df[joined_df['rank']<=3]
    return joined_df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':"Salary"})
    