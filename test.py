import csv
import pandas as pd


def create_user_dataframe(names: list[str], ages: list[int], hobbies: list[list[str]], is_life_values: list[bool]):
    df = pd.DataFrame({
        "name": names,
        "age": ages,
        "hobbies": hobbies,
        "is_life": is_life_values
    })
    return df

names = []
ages = []
hobbies_list = []
is_life_values = []

while True:
    name = input("Enter name (or type 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    
    age = int(input("Enter age: "))
    hobbies = input("Enter hobbies separated by , : ").split(",")
    is_life = input("Enter (True/False): ")

    names.append(name)
    ages.append(age)
    hobbies_list.append(hobbies)
    is_life_values.append(is_life)


df = create_user_dataframe(names, ages, hobbies_list, is_life_values)
csv_filename = "user_data.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "hobbies", "is_life"])
    for index, row in df.iterrows():
        writer.writerow([row.get('name'), row.get('age'), row.get('hobbies'), row.get('is_life')])

print(f"Data saved to {csv_filename}")