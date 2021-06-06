favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

alien_0 = {
    'color': 'green',
    'speed': 'slow',
#    'points': 100
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)