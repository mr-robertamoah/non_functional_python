from people import Person
from character import discipline, perseverance

robertAmoah = Person.get('Robert Amoah')

characters = [discipline, perseverance]

robertAmoah.present.addCharacters(characters)

robertAmoah.future.load()

achieved = robertAmoah.future.achievedGoals()

if achieved:
    print(f"I achieved my goals.")
else:
    print(f"I did not achieve my goals.")

# Output: I achieved my goals.


by Robert Amoah (https://www.robertamoah.com)