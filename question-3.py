import json
string = {'4': 5, '6': 7, '1': 3, '2': 4}
print("String:")
print(string)
print("\nJSON data:")
print(json.dumps(string, sort_keys=True, indent=4))
