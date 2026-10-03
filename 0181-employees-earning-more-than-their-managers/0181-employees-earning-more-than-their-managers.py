import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Merge the DataFrame with itself to line up employees with their managers
    merged = employee.merge(
        employee, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )
    
    # 2. Filter rows where the employee's salary is greater than the manager's salary
    filtered_df = merged[merged['salary_emp'] > merged['salary_mgr']]
    
    # 3. Select the employee name column and rename it to 'Employee' as required
    result = filtered_df[['name_emp']].rename(columns={'name_emp': 'Employee'})
    
    return result
