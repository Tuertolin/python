first_name = "ada"
last_name = "lovelace"

full_name = format("{first_name} {last_name}")
print(full_name)
      
full_name = f"{first_name} {last_name}"
print(full_name)

full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("\tPython\n")
print("Lenguages:\n\tPython\n\tC#\n\tJavaScript\n")


#Remove whitespaces Left lstrip() or Right rstrip()
favorite_language = '     python '
print(favorite_language)

favorite_language = favorite_language.lstrip()

print(favorite_language)
favorite_language.lstrip()
favorite_language.strip()


