import pandas as pd
from sklearn.tree import DecisionTreeRegressor

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

file_path = "states_all.csv"
education_data = pd.read_csv(file_path)

print(education_data.describe())
print(f"\n{education_data}")

updated_education_data = education_data.dropna(axis=0)
print(f"\n{updated_education_data.describe()}")

year_and_state = updated_education_data[['YEAR', 'STATE', 'TOTAL_REVENUE', 'INSTRUCTION_EXPENDITURE', 'AVG_MATH_8_SCORE',
                                         'AVG_READING_8_SCORE']]
print(f"\n{year_and_state}")

# grab just the year 2015 with truth value, using bitwise operators
year_2015 = year_and_state[(year_and_state['YEAR'] == 2015)]
print(f"\n{year_2015}")

year_2015_features = ['STATE', 'TOTAL_REVENUE', 'INSTRUCTION_EXPENDITURE']
X = year_2015[year_2015_features]
Y = year_2015.TOTAL_REVENUE
print(f"\n{X.head()}")
print(f"\n{Y.head()}")