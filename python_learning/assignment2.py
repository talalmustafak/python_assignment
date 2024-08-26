
message : str = "Hi! What's up"
print(message)


message1 : str = "Hi! What's up"
message1 = "Have a good day!"
print(message1)


person_name : str = "Eric"
print(f'"Hello {person_name}, would you like to learn some Python today?"')


person_name2 : str = "Eric"
print(person_name2.lower())
print(person_name2.upper())
print(person_name2.title())


author_name : str = "Albert Einstein"
quote : str = "A person who never made a mistake never tried anything new."
print(f'{author_name} once said,"{quote}"')


famous_person : str = "Albert Einstein"
message2 : str = "A person who never made a mistake never tried anything new."
print(f'{famous_person} once said,"{message2}"')


name :str = "\t    Talal Khan       \n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


x : int = 27
y : int = 87
z : int = 91
sum : int = x+y+z
print (f"The sum of {x}, {y} and {z} is {sum}")


a : int = 11
b : int = 19
print (f"The values before swapping is {a} , {b}")
c : int = a
a = b
b = c
print (f"The values after swapping is {a} , {b}")


favorite_color="White"
print(favorite_color)
color = "White"
print(color)


pet_name : str = "Buddy"
pet_name= "Max"
print(pet_name)


nature : str = "Sunshine"
print(nature)

score : int  = 100
print(f"Score is {score}")
score = 90 
print(f"Now, Score is {score}")


city : str = "Vehari"
print(f"My city is {city}")


language : str = "python programming"
print(language.title())


town : str = "Wapda TOWN"
print(town.lower())


society: str = "bahria town"
print(society.upper())


temperature : int = 25
print(f"The current temperature is {temperature} degrees.")


poem : str = '''
 POEM NAME : "The Morning Sun"

In the sky, the morning sun,
Rises up, the day’s begun.
Golden rays, so warm and bright,
Chase away the lingering night.

Birds awaken, sing their song,
Nature’s chorus, loud and strong.
Dewdrops sparkle on the grass,
As the moments gently pass.

With the dawn, new hopes arise,
Underneath the vast blue skies.
Embrace the day with heart so free,
The world is full of mystery.'''
print(poem)
