user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

for name, lenguage in favorite_languages.items():
    print(f"{name.title()} favorite lenguage is {lenguage} \n")

for name in favorite_languages:
    print(f"{name.title()}")

print("\n ################## \n")

for name in favorite_languages.keys():
    print(f"{name.title()}")

print("################## \n")

for name in favorite_languages.values():
    print(f"{name.title()}")

print("################## \n")

for name in sorted(favorite_languages):
    print(f"{name.title()}")