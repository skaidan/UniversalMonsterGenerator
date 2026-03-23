# UniversalMonsterGenerator
This generator brings infinite creatures to your dungeon


Right now is a case base but the expected scope must include:

- Combine multiple races with types
- select combination and generate levels

# from anywhere in your project
from dynamic_loader import main

# 1) Get dict
data = main(return_json_string=False)  # type: dict
print(data["STR"])  # e.g. 14

# 2) Get JSON string
j = main(return_json_string=True)  # type: str
print(type(j))  # str
print(j)
