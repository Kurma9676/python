# Sample dictionary
d = {"name": "Alice", "age": 25, "city": "London"}

# 1. clear()
temp = d.copy()
temp.clear()
print(temp)  # {}

# 2. copy()
d_copy = d.copy()
print(d_copy)  # {'name': 'Alice', 'age': 25, 'city': 'London'}

# 3. fromkeys()
keys = ['a', 'b', 'c']
new_d = dict.fromkeys(keys, 0)
print(new_d)  # {'a': 0, 'b': 0, 'c': 0}

# 4. get()
print(d.get("name"))        # Alice
print(d.get("country", "Not Found"))  # Not Found

# 5. items()
print(list(d.items()))  # [('name', 'Alice'), ('age', 25), ('city', 'London')]

# 6. keys()
print(list(d.keys()))   # ['name', 'age', 'city']

# 7. pop()
age = d.pop("age")
print(age)              # 25
print(d)                # {'name': 'Alice', 'city': 'London'}

# 8. popitem()
last_item = d.popitem()
print(last_item)        # ('city', 'London')
print(d)                # {'name': 'Alice'}

# Reset dictionary
d = {"name": "Alice", "age": 25}

# 9. setdefault()
print(d.setdefault("age", 30))     # 25 (already exists)
print(d.setdefault("country", "UK")) # UK (added because missing)
print(d)  # {'name': 'Alice', 'age': 25, 'country': 'UK'}

# 10. update()
d.update({"age": 26, "city": "London"})
print(d)  # {'name': 'Alice', 'age': 26, 'country': 'UK', 'city': 'London'}

# 11. values()
print(list(d.values()))  # ['Alice', 26, 'UK', 'London']
