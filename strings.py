from typing import Concatenate


first_name = 'brian'
last_name = "Kyle"

# formatted strings

# print(f"my first name is {first_name} and my last name is {last_name}")
print(first_name.capitalize().join(last_name.capitalize()," "))