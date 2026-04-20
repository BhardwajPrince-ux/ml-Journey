#DAY - 2
#Pandas is used for data manipulation in ML
import pandas as pd
#Creating Dictionary with sample data
data = { 
    "Name":["Lucky","Prince","Jarvis"],
    "Age":[20,22,23],
    "City":["Gurugram","Dehradun","Las Vegas"]
}
#Converting Dictionary into a DataFrame (like a Table)
df = pd.DataFrame(data)

#Printing the Full table
print(df)

#Checking numbers of Rows and Columns
print("\nShape:",df.shape)

print("\nInfo:")

#Printing Basic Statistics of the data
print(df.describe())
