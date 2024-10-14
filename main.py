from pandas import DataFrame


# F I R S T
# data_frame = pd.DataFrame({"A": [1, 2, 3]})
# print(data_frame)

# WAY 1
# d = {'column-1': [1, 2], "column-2": [3, 4], 'column-3': [5, 6]}
# df = pd.DataFrame(data=d)
# print(df)

# WAY 2
# d = pd.DataFrame(
#     {"Name": ["John"],
#      "Age": [23.5],
#      "Hobbies": [["Coding", "Gym"]],
#      "is_life": [True]
#      }
#     )
# print(d.dtypes)
# print(d)



# def create_user_dataframe(names: list[str], ages: list[int], hobbies: list[list[str]], is_life_values: list[bool]):
#     df = pd.DataFrame({
#         "name": names,
#         "age": ages,
#         "hobbies": hobbies,
#         "is_life": is_life_values
#     })
#     return df


# names = []
# ages = []
# hobbies_list = []
# is_life_values = []

# while True:
#     name = input("Enter name (or type 'quit' to stop): ")
#     if name.lower() == 'quit':
#         break
    
#     age = int(input("Enter age: "))
#     hobbies = input("Enter hobbies separated by , : ").split(",")
#     is_life = input("Enter (True/False): ").strip().lower() == 'true'

#     names.append(name)
#     ages.append(age)
#     hobbies_list.append(hobbies)
#     is_life_values.append(is_life)


# df = create_user_dataframe(names, ages, hobbies_list, is_life_values)
# print(df)
