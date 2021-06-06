def greet_user(username):
    """Display a simple gretting."""
    print(f"Hello, {username.title()}!")

def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#Default value
def describe_pet_v2(pet_name, animal_type='dog'):
    """Display information about pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#greet_user('gaston')
describe_pet('dog', 'rame')
describe_pet('fish', 'nemo')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet_v2(pet_name='harry', animal_type='hamster')
describe_pet_v2(pet_name='harry')